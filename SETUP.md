# 🚀 Hướng Dẫn Cài Đặt Bot

## Yêu cầu hệ thống
- Windows 10/11 hoặc macOS hoặc Linux
- Python 3.8 hoặc cao hơn
- Kết nối Internet
- Telegram Bot API Key
## Cài đặt nhanh (3 bước)

### Bước 1: Mở Terminal/CMD
```bash
# Windows
cd C:\Users\YourName
# hoặc bất kỳ thư mục nào bạn muốn
```

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Chạy bot
```bash
python bot.py
```

Hoặc sử dụng script tiện lợi:
```bash
python run.py
```

## ✅ Kiểm tra cài đặt

Bot sẽ in ra:
```
🚀 Starting Learning Assistant Bot...
✅ Bot is running! Press Ctrl+C to stop.
```

## 🎯 Sử dụng Bot trên Telegram

1. Mở Telegram
2. Tìm bot theo username (nếu bạn đã set) hoặc bằng BotFather
3. Gửi lệnh `/start` để bắt đầu
4. Sử dụng các nút menu để tương tác

## 🤖 Tích hợp AI (Tùy chọn)

### Option 1: Google Gemini (Free - Khuyến nghị)

1. Truy cập: https://ai.google.dev/
2. Đăng nhập với Google account
3. Tạo API key mới
4. Tạo file `.env` trong thư mục bot:
```env
GEMINI_API_KEY=your_key_here
```

### Option 2: OpenAI GPT

1. Truy cập: https://platform.openai.com/
2. Tạo account và nạp tiền
3. Tạo API key
4. Thêm vào file `.env`:
```env
OPENAI_API_KEY=your_key_here
```

> **Lưu ý:** Bot vẫn hoạt động tốt không cần AI key!

## 🔧 Troubleshooting

### Lỗi: "Module not found"
```bash
pip install --upgrade python-telegram-bot
```

### Lỗi: "API Key invalid"
- Kiểm tra lại API key trong `config.py`
- Đảm bảo key đúng định dạng

### Bot không phản hồi
- Kiểm tra internet connection
- Kiểm tra bot đang chạy không (terminal không có lỗi)
- Thử restart bot: `Ctrl+C` và chạy lại `python bot.py`

### Port bị chiếm
```bash
# Windows
netstat -ano | findstr :PORT
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:PORT | xargs kill
```

## 📊 Cấu trúc files

```
telegram_learning_bot/
├── bot.py              ← File chính, chạy bot
├── config.py           ← Cấu hình API key
├── run.py              ← Script chạy tiện lợi
├── requirements.txt    ← Dependencies
├── handlers/           ← Logic xử lý
│   ├── learning_handler.py
│   ├── practice_handler.py
│   └── ai_handler.py
├── .gitignore
├── .env.example        ← Template cho .env
├── README.md           ← Hướng dẫn chung
└── SETUP.md            ← File này
```

## 🎓 Mở rộng Bot

### Thêm chủ đề học tập
Sửa `handlers/learning_handler.py`:
```python
LEARNING_CONTENT['Chủ Đề Mới'] = """
Nội dung của bạn...
"""
```

### Thêm câu hỏi Quiz
Sửa `handlers/learning_handler.py`:
```python
QUIZ_QUESTIONS['Chủ Đề'] = [{
    'question': 'Câu hỏi?',
    'options': ['A', 'B', 'C'],
    'correct': 0,
    'explanation': 'Giải thích'
}]
```

### Thêm bài tập LeetCode
Sửa `handlers/practice_handler.py`:
```python
LEETCODE_PROBLEMS['chủ đề'].append({
    'title': 'Tên Bài',
    'difficulty': 'Easy',
    'description': 'Mô tả',
    'example': 'I/O',
    'hint': 'Gợi ý'
})
```

## 💡 Tips

1. **Logs:** Xem logs trong terminal để debug
2. **Restart:** Luôn restart bot sau khi sửa code
3. **Testing:** Test trên group private trước
4. **Backup:** Backup code định kỳ

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra logs trong terminal
2. Đọc README.md
3. Check troubleshooting ở trên

## 🎉 Hoàn thành!

Bot của bạn đã sẵn sàng sử dụng! 

**Thử ngay:**
- Mở Telegram
- Gửi `/start` cho bot
- Khám phá các tính năng!

---