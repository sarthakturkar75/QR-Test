from pydantic import BaseModel

class QRCodeResponse(BaseModel):
    image: str
