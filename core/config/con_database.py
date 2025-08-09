from sqlmodel import Session, SQLModel, create_engine

LOCAL_DB_URL = "sqlite:///./test.db"
EXTERNAL_DB_URL ="sqlite:///./test.db"

enginer_local = create_engine(LOCAL_DB_URL, echo=True)
ebginer_external = create_engine(EXTERNAL_DB_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(enginer_local)

def get_local_session():
  with Session(enginer_local) as session:
      yield session
    
def get_external_session():
  with Session(ebginer_external) as session:
      yield session