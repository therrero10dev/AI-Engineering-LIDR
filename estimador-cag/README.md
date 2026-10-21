# estimador-cag

API FastAPI para estimaciones con CAG (Cache-Augmented Generation).

## Setup

```bash
uv sync
cp .env.example .env  # completar LLM_API_KEY
uv run fastapi dev app/main.py
```

Docs: http://127.0.0.1:8000/docs

## Configuración

Gestionada con Pydantic `BaseSettings` en `app/config.py`, leyendo variables de `.env`.
