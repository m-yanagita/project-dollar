from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Hello Project Dollar"}


@app.get("/products")
def products():

    return {
        "products":[
            {
                "name":"Apple",
                "price":"$3"
            },
            {
                "name":"Orange",
                "price":"$5"
            }
        ]
    }


@app.get("/users")
def users():

    return {
        "users":[
            "Tom",
            "Mike",
            "John"
        ]
    }