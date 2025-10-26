# 📱 HƯỚNG DẪN SỬ DỤNG BOT TRÊN TELEGRAM

## 🤖 BƯỚC 1: TÌM BOT TRÊN TELEGRAM

### Nếu bạn đã tạo bot qua @BotFather:

1. **Mở Telegram**
2. **Tìm tên bot** của bạn hoặc dùng username
3. **Gửi lệnh** `/start`

### Nếu chưa có bot:

1. Mở Telegram → Tìm **@BotFather**
2. Gửi lệnh: `/newbot`
3. Đặt tên: `Learning Assistant Bot` (hiển thị cho users)
4. Đặt username: `your_learning_bot` (phải kết thúc bằng `bot`)
5. **Sao chép API key** được BotFather cung cấp
6. Thay vào file `config.py` trong project

---

## 🎮 BƯỚC 2: CÁC LỆNH VÀ TÍNH NĂNG

### Lệnh chính:
```
/start  - Bắt đầu bot
/help   - Xem hướng dẫn
/topics - Xem chủ đề học tập
```

---

## 📚 MENU CHÍNH

Sau khi gửi `/start`, bạn sẽ thấy 6 nút:

### 1. 📚 **Học Lý Thuyết**
- Nhấn vào → Chọn chủ đề:
  - C# & .NET
  - JavaScript
  - TypeScript
  - ReactJS
- Bot sẽ gửi nội dung lý thuyết chi tiết về chủ đề

**Ví dụ:**
```
👤 User: [Nhấn "📚 Học Lý Thuyết"]
Bot: 📚 Chọn chủ đề bạn muốn học...

👤 User: [Chọn "JavaScript"]
Bot: 📚 JavaScript - Lý Thuyết
[Gửi nội dung chi tiết về JS]
```

---

### 2. 💻 **Thực Hành & LeetCode**
- Luyện tập với bài tập LeetCode
- Bài tập theo chủ đề: Arrays, DP, Binary Search, etc.

**Các tùy chọn:**
- Arrays & Strings
- Dynamic Programming
- Binary Search
- Trees & Graphs
- Practice C#
- Practice JavaScript

**Ví dụ:**
```
👤 User: [Nhấn "💻 Thực Hành & LeetCode"]
Bot: 💻 Menu thực hành
    [Danh sách chủ đề]

👤 User: [Chọn "Arrays & Strings"]
Bot: 💻 Bài Tập: Two Sum
     [Gửi bài tập LeetCode + gợi ý]
```

---

### 3. ❓ **Hỏi AI**
- Đặt câu hỏi bất kỳ về lập trình
- Bot sẽ trả lời thông minh

**Ví dụ:**
```
👤 User: [Nhấn "❓ Hỏi AI"]
Bot: ❓ Đặt câu hỏi của bạn...

👤 User: "Giải thích async/await trong JavaScript"
Bot: [Trả lời chi tiết về async/await]

👤 User: "What is React hooks?"
Bot: [Trả lời về React hooks]

👤 User: "Làm thế nào để tối ưu query LINQ?"
Bot: [Trả lời về LINQ optimization]
```

---

### 4. 📊 **Kiểm Tra Kiến Thức**
- Làm quiz tương tác
- Đánh giá trình độ

**Các loại quiz:**
- Quiz C#
- Quiz JavaScript
- Quiz TypeScript
- Quiz React

**Ví dụ:**
```
👤 User: [Nhấn "📊 Kiểm Tra Kiến Thức"]
Bot: 📊 Chọn loại quiz...
    [Quiz C#, Quiz JavaScript, etc.]

👤 User: [Chọn "Quiz C#"]
Bot: 📊 Quiz C#
    Câu hỏi: C# là ngôn ngữ gì?
    [A) Compiled, B) Interpreted, C) Both, D) None]

👤 User: [Chọn đáp án]
Bot: ✅ Chính xác! [hoặc] ❌ Sai rồi
     [Giải thích đáp án]
```

---

### 5. ℹ️ **Giới Thiệu**
- Thông tin về bot
- Tính năng chính
- Công nghệ hỗ trợ

### 6. 🔗 **Tài Liệu Tham Khảo**
- Links tài liệu hữu ích
- Official docs
- Learning resources

---

## 🎯 VÍ DỤ SỬ DỤNG ĐẦY ĐỦ

### Scenario 1: Học JavaScript từ đầu

```
👤 User: /start
Bot: 👋 Xin chào! [Menu chính]

👤 User: [Nhấn "📚 Học Lý Thuyết"]
Bot: 📚 Chọn chủ đề...

👤 User: [Chọn "JavaScript"]
Bot: 📚 JavaScript - Lý Thuyết
     [Gửi nội dung chi tiết về JS]
     
👤 User: [Nhấn "🔙 Về Menu Chính"]
Bot: [Về menu chính]
     
👤 User: [Nhấn "📊 Kiểm Tra Kiến Thức"]
Bot: 📊 Chọn loại quiz...

👤 User: [Chọn "Quiz JavaScript"]
Bot: [Câu hỏi quiz về JS]

👤 User: [Trả lời]
Bot: [Kết quả + giải thích]
```

---

### Scenario 2: Luyện LeetCode

```
👤 User: /start
Bot: [Menu chính]

👤 User: [Nhấn "💻 Thực Hành & LeetCode"]
Bot: 💻 Menu thực hành
     [Các chủ đề]

👤 User: [Chọn "Dynamic Programming"]
Bot: 💻 Bài Tập: Coin Change
     - Độ khó: Medium
     - Mô tả: Tìm số tiền xu nhỏ nhất...
     - Ví dụ: ...
     - Gợi ý: DP với dp[i] = ...

👤 User: [Nhấn "🔁 Bài Tập Khác"]
Bot: [Bài tập khác]
```

---

### Scenario 3: Hỏi AI về C#

```
👤 User: /start
Bot: [Menu chính]

👤 User: [Nhấn "❓ Hỏi AI"]
Bot: ❓ Đặt câu hỏi...

👤 User: "Giải thích async/await trong C#"
Bot: 🔹 Async/Await trong C#:
     [Trả lời chi tiết với code example]

👤 User: "Sự khác biệt giữa Task và async Task"
Bot: [Giải thích về Task vs async Task]
```

---

## 💡 TIPS SỬ DỤNG HIỆU QUẢ

### 1. Kết hợp các tính năng
- Học lý thuyết → Làm quiz
- Hỏi AI → Thực hành code

### 2. Sử dụng Quiz
- Đánh giá kiến thức
- Ôn lại những gì đã học

### 3. LeetCode Practice
- Bắt đầu từ dễ
- Practice đều đặn
- Xem gợi ý khi stuck

### 4. Hỏi AI
- Đặt câu hỏi cụ thể
- Hỏi về syntax, concepts
- Hỏi best practices

---

## 🐛 TROUBLESHOOTING

### Bot không phản hồi?
1. Kiểm tra bot đang chạy (terminal/logs)
2. Kiểm tra internet connection
3. Thử gửi lại `/start`
4. Kiểm tra API key trong `config.py`

### Menu không hiển thị?
- Dùng `/start` để reset menu
- Bot cần hỗ trợ ReplyKeyboard

### Không thấy nội dung?
- Kiểm tra bot đã được deploy chưa
- Xem logs để debug

---

## 📞 KIỂM TRA BOT ĐANG HOẠT ĐỘNG

### Test local:
```powershell
cd telegram_learning_bot
python bot.py

# Terminal sẽ hiện:
# 🚀 Starting Learning Assistant Bot...
# ✅ Bot is running!
```

### Kiểm tra trên Telegram:
1. Mở Telegram
2. Tìm bot của bạn
3. Gửi `/start`
4. Bot phải phản hồi ngay lập tức

---

## 🎓 VÍ DỤ THỰC TẾ

### Học TypeScript:

```
Step 1:
👤 /start
Bot: Menu chính

Step 2:
👤 [📚 Học Lý Thuyết] → [TypeScript]
Bot: Gửi nội dung TypeScript

Step 3:  
👤 [📊 Kiểm Tra Kiến Thức] → [Quiz TypeScript]
Bot: Câu hỏi quiz

Step 4:
👤 Trả lời
Bot: Kết quả + Giải thích

Step 5:
👤 [❓ Hỏi AI] → "What are generics in TypeScript?"
Bot: Giải thích chi tiết
```

---

## 🚀 QUICK COMMANDS

```
/start     - Bắt đầu bot
/help      - Hướng dẫn
/topics    - Xem chủ đề

📚         - Học lý thuyết
💻         - Thực hành
❓         - Hỏi AI
📊         - Quiz
ℹ️         - Giới thiệu
🔗         - Tài liệu
```

---

🎉 **Chúc bạn học tập vui vẻ với bot!**

