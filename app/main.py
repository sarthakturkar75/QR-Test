from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import qrcode
import base64
from io import BytesIO

app = FastAPI()

class QRCodeCreate(BaseModel):
    url: str
    size: int

@app.post("/create")
async def create_qr_code(qr_code_data: QRCodeCreate):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=qr_code_data.size,
            border=4,
        )
        qr.add_data(qr_code_data.url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        base64_img = base64.b64encode(buffer.read()).decode('utf-8')
        return {"image": base64_img}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
