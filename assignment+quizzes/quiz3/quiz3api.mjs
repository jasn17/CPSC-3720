import https from "https";

const quizpath = "/quizapi";
const quizparampath = `${quizpath}/{id}`;

// Example data
let data = {
    items: [
        { id: 1, name: "Frozen Pizza", price: 10.99 },
        { id: 2, name: "Sunglasses", price: 15.99 },
        { id: 3, name: "Phone Case", price: 20.99 },
        { id: 4, name: "Gum", price: 2.59 },
        { id: 5, name: "Disposable Camera", price: 35.29 }
    ]
};

export const handler = async (event, context) => {
    console.log("Request event method:", event.httpMethod);
    console.log("EVENT\n", JSON.stringify(event, null, 2));

    const httpMethod = event.httpMethod;
    const httpPath = event.requestContext.resourcePath;

    // Handle GET request
    if (httpMethod === "GET" && httpPath === quizpath) {
        return {
            statusCode: 200,
            body: JSON.stringify(data)
        };
    }

    // Handle GET request with ID as a path parameter
    // STUDENTS COMPLETE THIS METHOD FOR QUIZ3
    // **** HINT you will want to parseInt from the body to get the id


    // Handle POST request
    if (httpMethod === "POST" && httpPath === quizpath) {
        const body = JSON.parse(event.body);
        data.items.push(body);
        return {
            statusCode: 200,
            body: JSON.stringify(data)
        };
    }

    // Handle PUT request
    // STUDENTS COMPLETE THIS METHOD FOR QUIZ3
    // **** HINT you will want to use data.items.map to overwrite an existing item
    

    // Handle DELETE request with ID in the body
    if (httpMethod === "DELETE" && httpPath === quizpath) {
        const body = JSON.parse(event.body);
        data.items = data.items.filter(item => item.id !== body.id);
        return {
            statusCode: 200,
            body: JSON.stringify(data)
        };
    }

  return {
        statusCode: 405,
        body: JSON.stringify({ error: "Method not allowed" })
    };
};
