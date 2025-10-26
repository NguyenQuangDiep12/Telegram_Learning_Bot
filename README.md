# 🤖 Telegram Learning Assistant Bot

Chatbot thông minh hỗ trợ học tập và kiểm tra kiến thức về C#, .NET, JavaScript, TypeScript, ReactJS, và LeetCode.

## ✨ Tính năng

- 📚 **Học Lý Thuyết:** Nội dung chi tiết về C#, .NET, JS, TS, React
- 💻 **Thực Hành & LeetCode:** Bài tập từ dễ đến khó, theo chủ đề
- ❓ **Hỏi AI:** Trợ lý AI trả lời câu hỏi lập trình
- 📊 **Kiểm Tra Kiến Thức:** Quiz tương tác đánh giá trình độ

## 🚀 Cài đặt

### Yêu cầu
- Python 3.8+
- Telegram Bot Token

### Bước 1: Clone repository
```bash
cd telegram_learning_bot
```

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình (Optional)
Nếu muốn sử dụng AI features (Gemini hoặc OpenAI):

**Option 1: Gemini (Free - Khuyến nghị)**
1. Lấy API key tại: https://ai.google.dev/
2. Tạo file `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key
```

**Option 2: OpenAI**
1. Lấy API key tại: https://platform.openai.com/
2. Thêm vào `.env`:
```env
OPENAI_API_KEY=your_openai_api_key
```

> **Lưu ý:** Bot vẫn hoạt động tốt nếu không có AI API key, chỉ dùng rule-based responses.

## 🎯 Sử dụng

### Chạy bot
```bash
python bot.py
```

Bot sẽ khởi động và sẵn sàng nhận tin nhắn!

### Lệnh Telegram
- `/start` - Bắt đầu bot
- `/help` - Xem hướng dẫn
- `/topics` - Xem các chủ đề học tập

### Menu chính
1. **📚 Học Lý Thuyết** - Chọn chủ đề để học
2. **💻 Thực Hành & LeetCode** - Luyện tập với bài tập
3. **❓ Hỏi AI** - Đặt câu hỏi cho AI
4. **📊 Kiểm Tra Kiến Thức** - Làm quiz đánh giá
5. **ℹ️ Giới Thiệu** - Thông tin về bot
6. **🔗 Tài Liệu Tham Khảo** - Danh sách tài liệu

## 📁 Cấu trúc Project

```
telegram_learning_bot/
├── bot.py                    # File chính
├── config.py                 # Cấu hình
├── requirements.txt          # Dependencies
├── handlers/
│   ├── __init__.py
│   ├── learning_handler.py   # Xử lý học tập và quiz
│   ├── practice_handler.py   # Xử lý thực hành
│   └── ai_handler.py         # Xử lý AI assistant
└── README.md
```

## 🛠️ Tùy chỉnh

### Thêm nội dung học tập
Sửa file `handlers/learning_handler.py`:
```python
LEARNING_CONTENT = {
    'Chủ đề mới': """
    Nội dung của bạn...
    """
}
```

### Thêm câu hỏi Quiz
Trong `handlers/learning_handler.py`:
```python
QUIZ_QUESTIONS = {
    'Chủ đề': [
        {
            'question': 'Câu hỏi?',
            'options': ['A', 'B', 'C'],
            'correct': 0,
            'explanation': 'Giải thích'
        }
    ]
}
```

### Thêm bài tập LeetCode
Sửa file `handlers/practice_handler.py`:
```python
LEETCODE_PROBLEMS = {
    'chủ đề': [
        {
            'title': 'Tên bài',
            'difficulty': 'Easy',
            'description': 'Mô tả',
            'example': 'Input/Output',
            'hint': 'Gợi ý'
        }
    ]
}
```

## 🤖 Kết nối với AI

Bot hỗ trợ 3 chế độ:
1. **Rule-based:** Mặc định, sử dụng pattern matching
2. **Gemini AI:** Free, chất lượng tốt (khuyến nghị)
3. **OpenAI GPT:** Chất lượng cao nhất (có phí)

Để bật AI, thêm API key vào `.env` file.

## 📝 Example Usage

```
User: /start
Bot: 👋 Xin chào! Tôi là Learning Assistant Bot...

User: [Nhấn "📚 Học Lý Thuyết"]
Bot: Chọn chủ đề...

User: [Chọn "JavaScript"]
Bot: 📚 JavaScript - Lý Thuyết [Nội dung chi tiết]

User: [Nhấn "💻 Thực Hành & LeetCode"]
Bot: Menu thực hành...

User: "Arrays & Strings"
Bot: [Bài tập LeetCode được gửi]
```

## 🐛 Troubleshooting

**Bot không phản hồi:**
- Kiểm tra API key trong `config.py`
- Kiểm tra internet connection
- Xem logs trong console

**AI không hoạt động:**
- Kiểm tra API key trong `.env`
- Hoặc bot sẽ dùng rule-based responses

## 📚 Tài liệu tham khảo

- [python-telegram-bot docs](https://docs.python-telegram-bot.org/)
- [C# Documentation](https://docs.microsoft.com/dotnet/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [React Documentation](https://react.dev/)
- [LeetCode](https://leetcode.com/)

## 📄 License

MIT License - Sử dụng tự do cho mục đích học tập và thương mại.

## 🎉 Contributors

Được tạo với ❤️ cho cộng đồng học lập trình!

---

💡 **Tip:** Hãy star repo này nếu bạn thấy hữu ích!
