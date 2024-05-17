# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from datetime import datetime

# app = FastAPI()

# class TokenData(BaseModel):
#     token: str
#     time: str

# @app.post("/receive-token")
# async def receive_token(data: TokenData):
#     # Extract and log the token and time for debugging
#     print(f"Received token: {data.token}")
#     print(f"Received time: {data.time}")

#     # Generate a row of dummy data
#     row_data = {
#         "Order Code": 123456789,
#         "Ticker": "EURINR24AUGFUT",
#         "Sale Date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#         "Customer Name": "John Doe",
#         "Gender": "-Male-",
#         "City": "New York",
#         "Order Amount": 1234
#     }

#     # Return the row data as JSON
#     return row_data

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class TokenData(BaseModel):
    token: str
    time: str

@app.post("/receive-token")
async def receive_token(data: TokenData):
    print(f"Received token: {data.token}")
    print(f"Received time: {data.time}")

    row_data = {
        "Order Code": 123456789,
        "Ticker": "EURINR24AUGFUT",
        "Sale Date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Customer Name": "John Doe",
        "Gender": "-Male-",
        "City": "New York",
        "Order Amount": 1234
    }

    return row_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
