from sqlmodel import Field, SQLModel
from typing import Optional

def Series(SQLModel, table=True):
  id:Optional[int] = Field(default=None, primary_key=True)
  activate_notification: int
  backdrop_path: str
  created_by: str
  episodes_number: int
  genres: str
  in_production: int
  last_air_date: str
  last_episode_number: str
  manual: int
  new_release: int
  next_air_date: str
  original_title: str
  overview: str
  poster_path: str
  recent_change: int
  release_date: str
  seasons_number: int
  soon_release: int
  status: str
  tagline: str
  watched: int
  year_title: str