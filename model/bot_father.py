from sqlmodel import SQLModel, Field
from typing import Optional

class BotFather(SQLModel, table=True):
    id_bot:Optional[int] = Field(default=None, primary_key=True)
    command_bot: str = Field(default=None)
    description_bot: str = Field(default=None)
    name_bot: str= Field(default=None)
    token_bot: str= Field(default=None)
    username_bot: str= Field(default=None)
    