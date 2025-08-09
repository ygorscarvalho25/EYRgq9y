from sqlmodel import Field, SQLModel
from typing import Optional

def Seasons(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    episodes_number: int
    overview: str
    poster_path: str
    season_number: int
    show_id: int
    title: str