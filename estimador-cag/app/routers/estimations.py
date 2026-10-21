from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import LLMService

router = APIRouter(prefix="/estimations", tags=["estimations"])


class EstimationRequest(BaseModel):
    description: str


class EstimationResponse(BaseModel):
    estimation: str


@router.post("", response_model=EstimationResponse)
async def create_estimation(payload: EstimationRequest) -> EstimationResponse:
    result = await LLMService().estimate(payload.description)
    return EstimationResponse(estimation=result)
