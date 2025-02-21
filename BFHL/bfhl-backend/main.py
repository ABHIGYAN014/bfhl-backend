from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class DataInput(BaseModel):
    data: list[str]

def process_input(data):
    numbers = [x for x in data if re.fullmatch(r'\d+', x)]
    alphabets = [x for x in data if re.fullmatch(r'[a-zA-Z]', x)]
    highest_alphabet = max(alphabets, key=lambda c: c.lower(), default="") if alphabets else []

    return {
        "is_success": True,
        "user_id": "abhigyan_singh_21022025",
        "email": "your_email@example.com",
        "roll_number": "CU12345",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }

@app.post("/bfhl")
async def process_post(input_data: DataInput):
    return process_input(input_data.data)

@app.get("/bfhl")
async def process_get():
    return {"operation_code": 1}
