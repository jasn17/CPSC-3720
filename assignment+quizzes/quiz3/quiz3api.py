# https://7e4p0468jg.execute-api.us-east-1.amazonaws.com/jlin22

import json

quizpath = "/quizapi"
quizparampath = f"{quizpath}/{{id}}"

# Example data
data = {
    "items": [
        {"id": 1, "name": "Frozen Pizza", "price": 10.99},
        {"id": 2, "name": "Sunglasses", "price": 15.99},
        {"id": 3, "name": "Phone Case", "price": 20.99},
        {"id": 4, "name": "Gum", "price": 2.59 },
        {"id": 5, "name": "Disposable Camera", "price": 35.29 }
    ]
}

def lambda_handler(event, context):
    # Print statements to help with debugging if needed
    print("Request event method:", event.get("httpMethod"))
    print("EVENT\n", json.dumps(event, indent=2))

    # Determine the HTTP method of the request
    http_method = event["httpMethod"]
    http_path = event["requestContext"]["resourcePath"]

    # Handle GET request
    if http_method == "GET" and event["requestContext"]["resourcePath"] == quizpath:
        # Return the data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # jlin22
    #### Handle GET request with ID as a path parameter
    #### STUDENTS ADD THIS METHOD FOR QUIZ 3
    #### HINT you will want enumerate through the item data object looking for the id match
    elif http_method == "GET" and event["requestContext"]["resourcePath"] == quizparampath:
        for item in data["items"]:
            if item["id"] == int(event["pathParameters"]["id"]):
                response = {
                    "statusCode": 200,
                    "body": json.dumps(item) # return the item found
                }
                return response
        response = {
            "statusCode": 404,
            "body": json.dumps({"error": "Item not found"})
        }
        return response
   


    # Handle POST request
    elif http_method == "POST" and event["requestContext"]["resourcePath"] == quizpath:
        # Retrieve the request's body and parse it as JSON
        body = json.loads(event["body"])
        # Add the received data to the example data
        data["items"].append(body)
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # jlin22
    #### Handle PUT request to update an data object sent in the body
    #### STUDENTS COMPLETE THIS METHOD FOR QUIZ3
    #### HINT you will need to get the id from the body similar to the DELETE and then item.update
    #### Give back appropriate error code and "Item does not exist." if PUTting to a non-existant item
    elif http_method == "PUT" and event["requestContext"]["resourcePath"] == quizpath:
        body = json.loads(event["body"])
        for i, item in enumerate(data["items"]):
            if item["id"] == body["id"]:
                data["items"][i].update(body) # updates the item 
                break;
        else:
            response = {
                "statusCode": 404,
                "body": json.dumps({"error": "Cannot find the itemt to update."})
            }
            return response
        response = {
            "statusCode": 200,
            "body": json.dumps(data) # return the updated data
        }
        return response
    

    # Handle DELETE request
    elif http_method == "DELETE" and event["requestContext"]["resourcePath"] == quizpath:
        # Retrieve the request's body and parse it as JSON
        body = json.loads(event["body"])
        # Find the item with the specified id in the example data
        for i, item in enumerate(data["items"]):
            if item["id"] == body["id"]:
                # Remove the item from the example data
                del data["items"][i]
                break
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Handle DELETE request by passing in an ID as a path parameter
    elif http_method == "DELETE" and event["requestContext"]["resourcePath"] == quizparampath:
        # Find the item with the path parameter id in the example data
        for i, item in enumerate(data["items"]):
            if item["id"] == int(event["pathParameters"]["id"]):
                # Remove the item from the example data
                del data["items"][i]
                break
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    else:
        # Return an error message for unsupported methods
        response = {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
        return response
