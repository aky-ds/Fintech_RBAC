from fastapi import APIRouter
from pydantic import BaseModel 
from .db import add_user

router = APIRouter()  # User management router
# User management module for creating users

class UserCreate(BaseModel): # User creation schema
    email: str
    password: str
    role: str

@router.post("/create_user")
def create_user(user: UserCreate):   # Create a new user
    success = add_user(user.email, user.password, user.role)
    if success:
        return {"status": "User created successfully"}
    return {"error": "User already exists"}