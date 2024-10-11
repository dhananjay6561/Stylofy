from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserModel(BaseModel):
    id: Optional[PyObjectId] = None
    username: str
    email: EmailStr
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserInDB(UserModel):
    hashed_password: str

class UserOut(BaseModel):
    id: PyObjectId
    username: str
    email: EmailStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}