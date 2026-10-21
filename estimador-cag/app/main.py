from fastapi import FastAPI

from app.config import get_settings
from app.routers import estimations

settings = get_settings()

app = FastAPI(title="Estimador CAG", debug=settings.APP_ENV == "development")

app.include_router(estimations.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
