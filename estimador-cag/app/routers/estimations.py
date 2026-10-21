from fastapi import APIRouter

from app.schemas.estimations import EstimationRequest, EstimationResponse
from app.services.llm_service import LLMService

router = APIRouter(prefix="/api/v1", tags=["estimations"])


@router.post("/estimate", response_model=EstimationResponse)
async def create_estimation(payload: EstimationRequest) -> EstimationResponse:
    result = await LLMService().estimate(payload.transcription)
    return EstimationResponse(**result)
