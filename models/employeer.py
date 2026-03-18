from sqlalchemy import Column, Integer, String, Date
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    birth_year = Column(Date)
    position = Column(String)
    degree = Column(String)
    title = Column(String)