from sqlalchemy import create_engine, String, Date, ForeignKey, DateTime
from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime
from dotenv import load_dotenv, find_dotenv
import os

from rich import print as printc
from rich.console import Console
console = Console()

load_dotenv(find_dotenv())

user = os.getenv("PG_USER")
passwrd = os.getenv("PG_PASSWORD")
db_name = os.getenv("PG_DB")
port = os.getenv("PORT")

def db_connect():
    return create_engine(f"postgresql+psycopg2://{"mari"}:{"lulita"}@localhost:{"5433"}/{"passman"}")

    
class Base(DeclarativeBase):
    pass

def create_table(engine):
    Base.metadata.create_all(engine)

class PassManUser(Base):
    __tablename__ = "passman_user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64),unique=True)
    phone: Mapped[str] = mapped_column(String(64),unique=True)
    masterkey_hash: Mapped[str] = mapped_column(String(255))
    device_secret: Mapped[str] = mapped_column(String(255))
    websites: Mapped[List["Website"]] = relationship(cascade="all, delete-orphan", lazy="noload")

class Selenium(Base):
    __tablename__ = "selenium"
    id: Mapped[int] = mapped_column(primary_key=True)
    sitename: Mapped[str] = mapped_column(String(64),unique=True)
    url: Mapped[str] = mapped_column(String(100))
    username_id: Mapped[str] = mapped_column(String(64))
    password_id: Mapped[str] = mapped_column(String(64))
    button_id: Mapped[str] = mapped_column(String(64))
    websites: Mapped[List["Website"]] = relationship(cascade="all, delete-orphan", lazy="noload")

class Website(Base):
    __tablename__ = "website"
    id: Mapped[int] = mapped_column(primary_key=True)
    sitename: Mapped[str] = mapped_column(String(64))
    username: Mapped[str] = mapped_column(String(64)) 
    passwd: Mapped[str] = mapped_column(String(64))
    user_id: Mapped[int] = mapped_column(ForeignKey("passman_user.id"))
    selenium_id: Mapped[int] = mapped_column(ForeignKey("selenium.id"))


