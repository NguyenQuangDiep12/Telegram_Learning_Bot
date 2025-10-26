# 🚀 HƯỚNG DẪN DEPLOY MIỄN PHÍ

## 📋 CÁC NỀN TẢNG MIỄN PHÍ TỐT NHẤT

### 1. ⭐ **Render.com** (Khuyến nghị - Dễ nhất)

**Ưu điểm:**
- ✅ Miễn phí forever
- ✅ Tự động deploy từ GitHub
- ✅ Dễ setup
- ✅ Có free PostgreSQL
- ⚠️ Sleep sau 15 phút không hoạt động (để tránh sleep: setup uptime robot)

**Cách deploy:**

1. **Đẩy code lên GitHub:**
```bash
cd telegram_learning_bot
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/telegram-learning-bot.git
git push -u origin main
```

2. **Tạo file `Procfile`:**
```
worker: python bot.py
```

3. **Tạo file `runtime.txt`:**
```
python-3.11.0
```

4. **Deploy trên Render:**
   - Truy cập: https://render.com
   - Sign up với GitHub
   - New → Web Service
   - Connect GitHub repo
   - Settings:
     - Name: `telegram-learning-bot`
     - Region: Singapore (gần VN nhất)
     - Branch: `main`
     - Root Directory: `telegram_learning_bot`
     - Runtime: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python bot.py`
     - Plan: `Free`
   - Click "Create Web Service"

---

### 2. ⭐ **Railway.app** (Tốt nhất cho Python)

**Ưu điểm:**
- ✅ $5 credit miễn phí mỗi tháng (đủ dùng)
- ✅ Không sleep
- ✅ Hỗ trợ tốt cho Python
- ✅ Auto-deploy từ GitHub

**Cách deploy:**

1. **Đẩy code lên GitHub** (giống Render)

2. **Deploy trên Railway:**
   - Truy cập: https://railway.app
   - Login với GitHub
   - New Project → Deploy from GitHub
   - Chọn repo
   - Settings:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python bot.py`
     - NODE_ENV: `production`
   - Deploy!

---

### 3. ⭐ **Replit** (Cực kỳ dễ cho beginners)

**Ưu điểm:**
- ✅ Hoàn toàn miễn phí
- ✅ Chỉnh sửa code trực tiếp trong browser
- ✅ Không cần setup phức tạp
- ⚠️ Sleep khi không active (có thể setup uptime)

**Cách deploy:**

1. Truy cập: https://replit.com
2. Sign up
3. Create Repl → Python
4. Upload code vào
5. Install packages: `pip install python-telegram-bot`
6. Click "Run"
7. Optionally: Setup uptime để tránh sleep

---

### 4. 🌟 **PythonAnywhere** (Free tier tốt)

**Ưu điểm:**
- ✅ Free tier ổn định
- ✅ Console sẵn để debug
- ✅ Scheduled tasks (free)

**Cách deploy:**

1. Truy cập: https://www.pythonanywhere.com
2. Sign up
3. Upload code qua Files
4. Mở Console → Install packages
5. Tạo scheduled task để chạy bot

---

### 5. 🎯 **fly.io** (Modern, nhanh)

**Ưu điểm:**
- ✅ $5 credit miễn phí/tháng
- ✅ Không sleep
- ✅ Rất nhanh
- ✅ Global edge deployment

**Cách deploy:**

```bash
# Cài fly CLI
# Windows PowerShell:
iwr https://fly.io/install.ps1 -useb | iex

# Login
fly auth login

# Trong thư mục bot
fly launch

# Follow instructions
```

---

### 6. ☁️ **Oracle Cloud (Forever Free)**

**Ưu điểm:**
- ✅ Forever free tier
- ✅ 2 VPS miễn phí
- ✅ Vĩnh viễn, không hết hạn
- ⚠️ Cần setup SSH, cài Python

**Cách deploy:**

1. Đăng ký: https://www.oracle.com/cloud/
2. Create instance (Always Free)
3. SSH vào server
4. Cài đặt:
```bash
sudo apt update
sudo apt install python3-pip
pip3 install python-telegram-bot
git clone your-repo
cd telegram_learning_bot
python3 bot.py &
```

---

## 🎯 KHUYẾN NGHỊ CHO BẠN

**Dễ nhất:** **Render.com** hoặc **Replit**
- Chỉ cần vài click
- Không cần biết nhiều về server

**Tốt nhất:** **Railway.app** hoặc **fly.io**
- Không sleep
- Performance tốt
- $5 credit mỗi tháng

**Lâu dài:** **Oracle Cloud**
- Forever free
- Full control

---

## 📝 LƯU Ý KHI DEPLOY

### 1. Thêm file `.gitignore`
```
__pycache__/
*.pyc
.env
*.log
venv/
```

### 2. Thêm file `runtime.txt` (cho Render)
```
python-3.11.0
```

### 3. Thêm file `Procfile` (cho Render)
```
worker: python bot.py
```

### 4. Environment Variables
- Không hardcode API key trong code
- Dùng biến môi trường
- Render/Railway có dashboard để set

### 5. Tránh bot bị sleep

**Option 1: Uptime Robot (Free)**
- Truy cập: https://uptimerobot.com
- Tạo monitor ping bot mỗi 5 phút

**Option 2: GitHub Actions**
Tạo file `.github/workflows/ping.yml`:
```yaml
name: Ping Bot
on:
  schedule:
    - cron: '*/5 * * * *'
  workflow_dispatch:
jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping
        run: curl https://your-bot-url.com
```

---

## 🚀 QUICK START (Render - Recommended)

### Bước 1: Push code lên GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/repo.git
git push -u origin main
```

### Bước 2: Tạo files cần thiết

**Procfile:**
```
worker: python bot.py
```

**runtime.txt:**
```
python-3.11.0
```

**requirements.txt:**
```
python-telegram-bot==20.7
python-dotenv==1.0.0
```

### Bước 3: Deploy trên Render
1. https://render.com → Sign up với GitHub
2. New → Web Service
3. Connect GitHub repo
4. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `python bot.py`
   - Plan: Free
5. Deploy!

---

## 🔍 TEST SAU KHI DEPLOY

1. Mở Telegram
2. Tìm bot của bạn
3. Gửi `/start`
4. Bot sẽ phản hồi!

---

## ❓ TROUBLESHOOTING

### Bot không phản hồi
- Kiểm tra logs trên dashboard
- Kiểm tra API key đúng chưa
- Kiểm tra bot đang chạy

### Deploy failed
- Kiểm tra `requirements.txt`
- Kiểm tra Python version
- Xem logs chi tiết

### Bot bị sleep
- Setup Uptime Robot
- Hoặc chuyển sang Railway/fly.io

---

💡 **Tip:** Bắt đầu với **Render.com** hoặc **Replit** - Dễ nhất!

