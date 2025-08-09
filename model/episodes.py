from sqlmodel import Field, SQLModel
from typing import Optional

def Episodes(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  episode_number: int
  episode_title: str
  overview: str
  runtime: int
  season_number: str
  show_id: int
  still_path: str
  watched: int
  title: str