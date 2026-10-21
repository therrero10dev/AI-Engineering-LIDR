from app.config import Settings, get_settings
from app.context.examples import EXAMPLES


class LLMService:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def build_prompt(self, description: str) -> str:
        examples = "\n\n".join(EXAMPLES)
        return f"{examples}\n\nEstima lo siguiente:\n{description}"

    async def estimate(self, description: str) -> str:
        # TODO: llamar al LLM con self.build_prompt(description)
        raise NotImplementedError
