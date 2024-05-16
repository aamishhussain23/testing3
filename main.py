from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Payload(BaseModel):
    token: str
    time: str

@app.post("/new-endpoint")
async def new_endpoint(payload: Payload):
    SPREADSHEET_ID = "1A8Mpe-dStdBKjc7DIc4WQSWRm-YK2KFB4o7qGVFBcY8"
    RANGE_NAME = "Sheet1"
    
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE_NAME}:append?valueInputOption=USER_ENTERED"

    headers = {
        'Authorization': f'Bearer {payload.token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Replace with actual data structure as per your requirement
    values = [
        ["4845158455", "AAMISH123", "04/08/2024 00:00:00", "Aamish", "-Male-", "Bihar", "8888"]
    ]

    body = {
        'values': values
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        return {"status": "success"}
    else:
        raise HTTPException(status_code=400, detail="Failed to update the spreadsheet")
