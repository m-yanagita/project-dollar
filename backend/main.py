from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import generator
from pydantic import BaseModel
from services.name_generator import generate_names
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInput(BaseModel):
    text: str

class NameRequest(BaseModel):
    industry: str
    keyword: str


@app.get("/")
def root():
    return {"message": "Hello Project Dollar"}


@app.get("/users")
def users():
    return {
        "users": [
            "Tom",
            "Mike",
            "John"
        ]
    }


@app.post("/analyze")
def analyze(user_input: UserInput):

    text = user_input.text

    return {

        "business":
        f"Business : {text}",

        "casual":
        f"Casual : {text}",

        "friendly":
        f"Friendly : {text}",

        "tips":
        "Keep your sentences short."

    }

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

app.include_router(generator.router)

@app.post("/name-generator")
def name_generator(data: NameRequest):

    results = generate_names(
        data.industry,
        data.keyword
    )

    return {
        "results": results
    }