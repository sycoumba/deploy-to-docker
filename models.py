from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER


Base = declarative_base()

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(INTEGER, primary_key=True, index=True)
    first_name = Column(String,)
    last_name = Column(String)
    age = Column(INTEGER) 