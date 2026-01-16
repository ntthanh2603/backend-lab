'''
- Chuỗi hash: 
    $2b$12$tQOWpafVIry0bKdYJ0pSkuA0KtPw7.aU1Mq16RSf8ScG5g8X9zLl6
    $<version>$<cost>$<salt>$<hash>

    <version>: Loại mã hóa
    <cost>: Số lần lặp
    <salt>: Giá trị ngẫu nhiên
    <hash>: Giá trị hash

- Khi kiểm tra lại mật khẩu thì chuỗi salt sẽ được lấy từ hash cũ
    rồi hash lại với mật khẩu mới với cost+verion cũ rồi so sánh.
    Nếu giống thì trả về True, không giống thì trả về False
'''
import bcrypt

password = b"my_password"

hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))

print(hash)

print(bcrypt.checkpw(b"my_password", hash))

print(bcrypt.checkpw(b"wrong_password", hash))