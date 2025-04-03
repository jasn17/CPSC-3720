# *Instructions for Quiz 3*

For this quiz there are three main steps - 1) deploy an API in AWS Lambda (code below) with some code updates to the lambda function, 2) deploy the code in AWS API Gateway, and 3) test the API in Postman.  You will turn in a URL for your API and the updated node or python file.  Details for each step are below as well as submission details:

---

# 1) Deploy and update Lambda code

You can use either the node or python code below.  Add a handler for the GET method by ID, and a handler for the PUT method.  The file indicates where to add the code as well as some hints.  

Node function (use v18 of node in Lambda): *quiz3api.mjs* [Download quiz3api.mjs]
Python function: *quiz3api.py* [Download quiz3api.py]

# 2)  Set up a deployment in AWS API Gateway

You can use the following .yaml file to create the API in AWS API Gateway: *quizapi.yaml* [Download quizapi.yaml]
Import the yaml file definition to set up the API and it will include all the endpoints/methods you need (reminder to ignore errors on import).
Integrate the API methods to your lambda code.  I recommend that you test your code in API Gateway after you integrate to see that it all works before testing in Postman.
Deploy the API.  For the stage name of your deployment use your clemson username.  
Example: https://pni22yst3dr9.execute-api.us-east-1.amazonaws.com/adkins4Links to an external site.

# 3) Test your API in Postman

Import the following collection into your PRIVATE WORKSPACE: *Quiz3Collection.json* [Download Quiz3Collection.json]
Modify the collection variable to you be your URL from the AWS API deployment above.
Run each test in the collection to see that your code works.  If you have an error, don't panic.  Run the test in API Gateway to see where you have an issue and correct it.

---

# SUBMISSION:

Include your AWS URL as the FIRST LINE OF YOUR CODE FILE
Comment it out with a single # (python) or // (js)
Use the naming convention indicated in part 2
Upload your updated python or node file
RULES AND REFERENCES:

You can only reference your notes and past work to guide what you need to do for the quiz or look things up in a reference library -  you CANNOT use an AI application (ChatGPT, Claude, Grok, etc.) to work on the code.  

---

Node reference libraries:

JSON: https://developer.mozilla.org/en-US/docs/Web/JavaScript/ReferenceLinks to an external site.
Arrays: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayLinks to an external site. 
Python reference libraries:

JSON: https://docs.python.org/3/library/json.htmlLinks to an external site.
Arrays: https://docs.python.org/3/library/array.htmlLinks to an external site. 