'''
JWT là chuẩn token trong xác thực người dùng
- Token bao gồm 3 phần: header, payload, signature
    - Header: chứa thông tin về thuật toán và loại token
    - Payload: chứa thông tin về người dùng và thời gian hết hạn
    - Signature: Là chữ ký mật mã để đảm bảo token không bị chỉnh sửa

- JWT có 3 loại:
    - Access token: Token ngắn hạn, thường dùng để xác thực người dùng
    - Refresh token: Token dài hạn, thường dùng để refresh access token
    - ID token: Token chứa thông tin về người dùng

- Cơ chế xác thực khi người dùng đăng nhập:
    - Người dùng đăng nhập
    - Server kiểm tra thông tin người dùng
    - Nếu thông tin đúng thì server tạo access token và refresh token
    - Server trả về access token và refresh token cho người dùng
    - Người dùng lưu access token và refresh token

- Cơ chế kiểm tra token: 
    - Tách token làm 3 phần
    - Giải mã header và payload
    - Tự tính lại signature từ header và payload và secret key
    - So sánh signature
    - Kiểm tra exp, nbf, iat
    - Hợp lệ → trả payload
    - Không hợp lệ → trả None
'''
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "secret-key"  
ALGORITHM = "HS256"

def create_access_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
        "iat": datetime.now(timezone.utc),
        "type": "access"
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

print("access_token: ", create_access_token("019bbf3d-4ab5-7449-8879-c4c7ac35c6ee"))

print("verify_token: ", verify_token(create_access_token("019bbf3d-4ab5-7449-8879-c4c7ac35c6ee")))

print("verify_token: ", verify_token("019bbf3d-c0af-7277-ac86-8781d5ba4623"))
