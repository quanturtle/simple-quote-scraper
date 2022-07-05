from datetime import datetime
from typing import Optional
import sqlmodel as sql
import config

class Quotes(sql.SQLModel, table=True):
    id: Optional[int] = sql.Field(primary_key=True)
    quote: str
    author: str

def get_config():
    credentials = config.Config('credentials.cfg')
    return credentials

def create_sql_engine(credentials):
    engine = sql.create_engine(credentials['DATABASE_URI'])
    sql.SQLModel.metadata.create_all(engine)
    return engine

def init_sql():
    credentials = get_config()
    engine = create_sql_engine(credentials)
    return engine
