import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# DynamoDB configuration
dynamo_table_name = "demoapi"
dynamo_table_region = "us-east-1"

# DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name=dynamo_table_region)
table = dynamodb.Table(dynamo_table_name)

# Constants for request methods and status codes
REQUEST_METHOD = {
    "POST": "POST",
    "GET": "GET",
    "DELETE": "DELETE",
    "PATCH": "PATCH",
}

STATUS_CODE = {
    "SUCCESS": 200,
    "NOT_FOUND": 404,
}

# Paths
user_path = "/users"
user_param_path = f"{user_path}/{{id}}"

# Custom JSON encoder for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert Decimal to float or int
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)  # Convert to int if it's a whole number, else float
    return obj

def lambda_handler(event, context):
    print("Request event method:", event.get("httpMethod"))
    print("EVENT\n", json.dumps(event, indent=2))

    response = None

    try:
        if event["httpMethod"] == REQUEST_METHOD["POST"] and event["requestContext"]["resourcePath"] == user_path:
            response = save_user(json.loads(event["body"]))
        elif event["httpMethod"] == REQUEST_METHOD["GET"] and event["requestContext"]["resourcePath"] == user_param_path:
            response = get_user(int(event["pathParameters"]["id"]))
        elif event["httpMethod"] == REQUEST_METHOD["PATCH"] and event["requestContext"]["resourcePath"] == user_path:
            response = modify_user(json.loads(event["body"]))
        elif event["httpMethod"] == REQUEST_METHOD["DELETE"] and event["requestContext"]["resourcePath"] == user_path:
            response = delete_user(int(event.get("queryStringParameters", {}).get("id")))
        elif event["httpMethod"] == REQUEST_METHOD["GET"] and event["requestContext"]["resourcePath"] == user_path:
            response = get_users()
        else:
            response = build_response(STATUS_CODE["NOT_FOUND"], event["requestContext"]["resourcePath"])
    except Exception as e:
        print("Error handling request:", e)
        response = build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error processing request"})

    return response

# Save a new user
def save_user(request_body):
    try:
        # Convert 'id' to int if it's a number
        if "id" in request_body:
            request_body["id"] = int(request_body["id"])

        table.put_item(Item=request_body)
        response_body = {
            "Operation": "SAVE",
            "Message": "SUCCESS",
            "Item": request_body,
        }
        return build_response(STATUS_CODE["SUCCESS"], response_body)
    except Exception as e:
        print("Error saving user:", e)
        return build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error saving user"})

# Get a user by ID
def get_user(member_id):
    try:
        response = table.get_item(Key={"id": member_id})
        if "Item" in response:
            # user = convert_decimals(response["Item"])  # Convert Decimal values
            user = response["Item"]
            return build_response(STATUS_CODE["SUCCESS"], user)
        else:
            return build_response(STATUS_CODE["NOT_FOUND"], {"message": "User not found"})
    except Exception as e:
        print("Error getting user:", e)
        return build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error retrieving user"})

# Modify a user
def modify_user(request_body):
    try:
        # Convert 'id' to int if it's a number
        if "id" in request_body:
            request_body["id"] = int(request_body["id"])

        update_expression = f"SET {request_body['updateKey']} = :value"
        expression_attribute_values = {":value": request_body["updateValue"]}

        response = table.update_item(
            Key={"id": request_body["id"]},  # ID must be int
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW",
        )

        response_body = {
            "Operation": "UPDATE",
            "Message": "SUCCESS",
            "UpdatedAttributes": response.get("Attributes", {}),
        }
        return build_response(STATUS_CODE["SUCCESS"], response_body)
    except Exception as e:
        print("Error modifying user:", e)
        return build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error updating user"})

def delete_user(user_id):
    try:
        response = table.delete_item(
            Key={"id": user_id},
            ReturnValues="ALL_OLD",
        )

        # Convert Decimal values before returning the response
        deleted_item = response.get("Attributes", {})  # convert_decimals()

        response_body = {
            "Operation": "DELETE",
            "Message": "SUCCESS",
            "Item": deleted_item,
        }
        return build_response(STATUS_CODE["SUCCESS"], response_body)
    except Exception as e:
        print("Error deleting user:", e)
        return build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error deleting user"})

def get_users():
    try:
        response = table.scan()
        users = response.get("Items", []) #convert_decimals()  # Convert Decimal values
        return build_response(STATUS_CODE["SUCCESS"], {"users": users})
    except Exception as e:
        print("Error retrieving users:", e)
        return build_response(STATUS_CODE["NOT_FOUND"], {"message": "Error retrieving users"})

# Utility function to build the response
def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(body, cls=DecimalEncoder),
    }
