# Hướng dẫn sử dụng Git

## Giới thiệu

Git là hệ thống quản lý phiên bản phân tán (distributed version control system) giúp theo dõi thay đổi trong mã nguồn và hỗ trợ làm việc nhóm hiệu quả.

## Cài đặt Git

### Windows

- Tải Git từ [git-scm.com](https://git-scm.com)
- Chạy file cài đặt và làm theo hướng dẫn

### macOS

```bash
brew install git
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

## Cấu hình ban đầu

Sau khi cài đặt, cấu hình thông tin cá nhân:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

Kiểm tra cấu hình:

```bash
git config --list
```

## Các lệnh Git cơ bản

### Khởi tạo repository

**Tạo repository mới:**

```bash
git init
```

**Clone repository từ xa:**

```bash
git clone https://github.com/username/repository.git
```

### Làm việc với thay đổi

**Kiểm tra trạng thái:**

```bash
git status
```

**Thêm file vào staging area:**

```bash
git add <tên-file>           # Thêm file cụ thể
git add .                     # Thêm tất cả file
git add *.js                  # Thêm tất cả file .js
```

**Commit thay đổi:**

```bash
git commit -m "Mô tả thay đổi"
```

**Xem lịch sử commit:**

```bash
git log                       # Xem đầy đủ
git log --oneline            # Xem rút gọn
git log --graph              # Xem dạng đồ thị
```

### Làm việc với remote repository

**Thêm remote repository:**

```bash
git remote add origin https://github.com/username/repo.git
```

**Xem danh sách remote:**

```bash
git remote -v
```

**Push code lên remote:**

```bash
git push origin main         # Push lên nhánh main
git push -u origin main      # Push và set upstream
```

**Pull code từ remote:**

```bash
git pull origin main
```

**Fetch thông tin từ remote:**

```bash
git fetch origin
```

### Làm việc với branches

**Tạo branch mới:**

```bash
git branch <tên-branch>
```

**Chuyển sang branch khác:**

```bash
git checkout <tên-branch>
```

**Tạo và chuyển sang branch mới:**

```bash
git checkout -b <tên-branch>
```

**Xem danh sách branch:**

```bash
git branch                   # Branch local
git branch -a                # Tất cả branch
```

**Xóa branch:**

```bash
git branch -d <tên-branch>   # Xóa an toàn
git branch -D <tên-branch>   # Xóa cưỡng chế
```

**Merge branch:**

```bash
git checkout main
git merge <tên-branch>
```

### Hoàn tác thay đổi

**Bỏ file khỏi staging area:**

```bash
git reset HEAD <tên-file>
```

**Hoàn tác thay đổi chưa commit:**

```bash
git checkout -- <tên-file>
```

**Hoàn tác commit gần nhất:**

```bash
git reset --soft HEAD~1      # Giữ thay đổi
git reset --hard HEAD~1      # Xóa thay đổi
```

**Revert một commit:**

```bash
git revert <commit-hash>
```

### Stash - Lưu tạm thay đổi

**Lưu thay đổi hiện tại:**

```bash
git stash
git stash save "Mô tả"
```

**Xem danh sách stash:**

```bash
git stash list
```

**Áp dụng stash:**

```bash
git stash apply              # Giữ stash
git stash pop                # Xóa stash sau khi apply
```

**Xóa stash:**

```bash
git stash drop stash@{0}
git stash clear              # Xóa tất cả
```

## Quy trình làm việc cơ bản

### Làm việc cá nhân

1. Tạo/clone repository
2. Thực hiện thay đổi
3. `git add .`
4. `git commit -m "Mô tả"`
5. `git push origin main`

### Làm việc nhóm

1. Clone repository: `git clone <url>`
2. Tạo branch mới: `git checkout -b feature/ten-tinh-nang`
3. Thực hiện thay đổi và commit
4. Push branch: `git push origin feature/ten-tinh-nang`
5. Tạo Pull Request trên GitHub/GitLab
6. Review và merge vào main

## File .gitignore

Tạo file `.gitignore` để loại trừ các file không cần track:

```
# Node modules
node_modules/

# Log files
*.log

# Environment variables
.env

# IDE
.vscode/
.idea/

# Build
dist/
build/
```

## Các lệnh hữu ích khác

**Xem thay đổi:**

```bash
git diff                     # Thay đổi chưa staged
git diff --staged            # Thay đổi đã staged
```

**Tìm kiếm:**

```bash
git grep "từ-khóa"
```

**Gắn tag:**

```bash
git tag v1.0.0
git push origin v1.0.0
```

**Rebase:**

```bash
git rebase main
```

## Mẹo và thủ thuật

- Commit thường xuyên với message rõ ràng
- Sử dụng branch cho mỗi tính năng mới
- Pull code trước khi bắt đầu làm việc
- Review code trước khi merge
- Không commit file nhạy cảm (passwords, API keys)

## Tài nguyên học thêm

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)

---

_Chúc bạn sử dụng Git hiệu quả!_
