from sqlmodel import Field, SQLModel
from typing import Optional

def ChannelConfig(SQLModel, table=True):
  chat_id:Optional[str] = Field(default=None, primary_key=True)
  channel_name: str = Field(default=None)
  channel_type: str = Field(default=None)
  message_id_start: int = Field(default=None)
  message_id_end: int = Field(default=None)