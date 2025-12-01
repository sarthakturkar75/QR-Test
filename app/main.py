from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.qrcode_utils import generate_qr_code

app = FastAPI()

class QRCodeCreate(BaseModel):
    url: str
    size: int

@app.post("/create")
async def create_qr_code(qr_code_data: QRCodeCreate):
    try:
        base64_img = generate_qr_code(qr_code_data.url, qr_code_data.size)
        return {"image": base64_img}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
