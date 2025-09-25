import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass(frozen=True)
class Settings:
    bot_token: str = os.environ["bot_token"]
    openai_token: str = os.environ["openai_token"]

settings = Settings()
