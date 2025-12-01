import qrcode
import base64
from io import BytesIO

def generate_qr_code(url: str, size: int) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    base64_img = base64.b64encode(buffer.read()).decode('utf-8')
    return base64_img
