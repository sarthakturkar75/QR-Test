from pydantic import BaseModel

class QRCodeCreate(BaseModel):
    url: str
    size: int
