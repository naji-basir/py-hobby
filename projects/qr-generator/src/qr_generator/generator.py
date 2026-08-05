import qrcode

def generate_qr(data:str, filename: str= 'qrcode.png')->None:
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"✅ QR code saved as '{filename}'")