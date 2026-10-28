from collections.abc import AsyncIterator

from openai import AsyncOpenAI, OpenAI

from app.config import Settings, get_settings
from app.context.examples import EXAMPLES

class LLMService:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.client = OpenAI(api_key=self.settings.OPENAI_API_KEY)
        self.async_client = AsyncOpenAI(api_key=self.settings.OPENAI_API_KEY)

    def build_prompt(self) -> str:
        examples = "\n\n".join(
            f"Resumen de reunión:\n{e['meeting_summary']}\n\nEstimación:\n{e['estimation']}"
            for e in EXAMPLES
        )
        return f"""Eres un experto en estimación de proyectos de software.
            Utiliza los siguientes presupuestos históricos como referencia:
            {examples}
            Genera una estimación detallada para el proyecto descrito."""

    async def estimate(self, description: str) -> dict[str, str]:
        response = self.client.chat.completions.create(
            model=self.settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": self.build_prompt()},
                {"role": "user", "content": description},
            ],
            temperature=0.5,
        )
        return {
            "estimation": response.choices[0].message.content or "",
            "model": self.settings.LLM_MODEL,
            "provider": self.settings.LLM_PROVIDER,
        }


    async def estimate_stream(self, description: str) -> AsyncIterator[str]:
        stream = await self.async_client.chat.completions.create(
            model=self.settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": self.build_prompt()},
                {"role": "user", "content": description},
            ],
            temperature=0.5,
            stream=True,
        )
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
