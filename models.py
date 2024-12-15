"""models"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, String, Column, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime


load_dotenv()

DB_URL = os.getenv('DB_URL')
engine = create_engine(DB_URL)

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks1'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    create_at = Column(DateTime(), default=datetime.now())
    done = Column(Boolean, default=False)


Base.metadata.create_all(engine)
