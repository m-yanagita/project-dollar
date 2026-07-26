from fastapi import APIRouter
from pydantic import BaseModel

from services.name_generator import generate_names


router = APIRouter()


class GeneratorRequest(BaseModel):
    industry: str
    keyword: str



@router.post("/name-generator")
def name_generator(
    request: GeneratorRequest
):

    result = generate_names(
        request.industry,
        request.keyword
    )

    return {
        "results": result
    }