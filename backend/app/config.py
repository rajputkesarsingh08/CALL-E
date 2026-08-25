import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    CALL_E_API_KEY: str = os.getenv(
        "CALL_E_API_KEY",
        ""
    )

    CALL_E_BASE_URL: str = os.getenv(
        "CALL_E_BASE_URL",
        "https://api.heycall-e.com"
    )

    LLM_API_KEY: str = os.getenv(
        "LLM_API_KEY",
        ""
    )

    LLM_BASE_URL: str = os.getenv(
        "LLM_BASE_URL",
        "https://api.openai.com/v1"
    )

    LLM_MODEL: str = os.getenv(
        "LLM_MODEL",
        "gpt-4.1-mini"
    )

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./campusconnect.db"
    )


settings = Settings()
