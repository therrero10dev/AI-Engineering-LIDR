from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.estimations import EstimationRequest, EstimationResponse
from app.services.llm_service import LLMService

router = APIRouter(prefix="/api/v1", tags=["estimations"])


@router.post("/estimate", response_model=EstimationResponse)
async def create_estimation(payload: EstimationRequest) -> EstimationResponse:
    result = await LLMService().estimate(payload.transcription)
    return EstimationResponse(**result)


@router.post("/estimate/stream")
async def create_estimation_stream(payload: EstimationRequest) -> StreamingResponse:
    return StreamingResponse(
        LLMService().estimate_stream(payload.transcription),
        media_type="text/plain; charset=utf-8",
    )
