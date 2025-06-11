from fastapi import FastAPI
from pydantic import BaseModel
from .auth import authenticate
from .rag_engine import generate_response
from .user_mgmt import router as user_router
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

app = FastAPI()
app.include_router(user_router)    # Include user management router
load_dotenv()  # Load environment variables from .env file

llm = ChatGroq(model='gemma2-it')

class QueryRequest(BaseModel): # Schema for chat query requests
    email: str
    password: str
    query: str

@app.post("/chat")
def chat(request: QueryRequest): # Handle chat queries
    role = authenticate(request.email, request.password)
    if not role:
        return {"error": "Unauthorized"}
    response = generate_response(request.query, role, llm)
    return {"response": response}