from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    full_name: str
    birth_year: int
    position: str
    degree: str
    title: str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True