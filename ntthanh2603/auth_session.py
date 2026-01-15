'''
- Session là cơ chế quản lý trạng thái (state) của người dùng sau khi xác thực
- Session có 2 cách triển khai phổ biến:
    - Server-side session:
        - Dữ liệu session lưu trên server
        - Client chỉ giữ session_id
    - Client-side state (thường gọi nhầm là client-side session):
        - Dữ liệu nằm trong client (JWT, signed/encrypted cookie)
        - Server không lưu session
- Cơ chế xác thực khi người dùng đăng nhập:
    - Người dùng đăng nhập
    - Server kiểm tra thông tin người dùng
    - Nếu thông tin đúng thì server tạo session và trả về session cookie
    - Người dùng lưu session cookie
    - Người dùng truy cập vào trang web
    - Server kiểm tra session cookie
    - Nếu session cookie hợp lệ thì server trả về thông tin người dùng
- Cơ chế kiểm tra session cookie:
    - Tách session cookie thành session_id và signature
    - Kiểm tra chữ ký bằng secret key
    - Nếu chữ ký không hợp lệ → reject
    - Nếu hợp lệ → lấy session_id gốc
    - Dùng session_id tra SESSION_STORE
    - Có session → trả session data
    - Không có session → trả None
'''
from itsdangerous import Signer
import uuid

signer = Signer("super-secret-key")
SESSION_STORE = {}

def create_session(data: dict):
    session_id = str(uuid.uuid4())
    SESSION_STORE[session_id] = data
    return signer.sign(session_id.encode()).decode()

def get_session(session_cookie: str):
    try:
        session_id = signer.unsign(session_cookie.encode()).decode()
        return SESSION_STORE.get(session_id)
    except:
        return None

new_session_cookie = create_session({"user_id": "019bbf3d-4ab5-7449-8879-c4c7ac35c6ee"})

print("session_cookie: ", new_session_cookie)

print("session: ", get_session(new_session_cookie))
