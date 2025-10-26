#!/usr/bin/env python3
"""
Telegram Learning Bot - Hệ thống chatbot học tập thông minh
Hỗ trợ học tập và kiểm tra kiến thức về C#, .NET, JS, TS, React, LeetCode
"""

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import API_KEY

# Import handlers
from handlers.learning_handler import handle_learning_topics, handle_quiz, get_quiz_content
from handlers.practice_handler import handle_practice_menu, handle_leetcode_request
from handlers.ai_handler import handle_ai_question

# Thiết lập logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Main menu keyboard
def get_main_menu():
    keyboard = [
        [KeyboardButton('📚 Học Lý Thuyết'), KeyboardButton('💻 Thực Hành & LeetCode')],
        [KeyboardButton('❓ Hỏi AI'), KeyboardButton('📊 Kiểm Tra Kiến Thức')],
        [KeyboardButton('ℹ️ Giới Thiệu'), KeyboardButton('🔗 Tài Liệu Tham Khảo')]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bắt đầu cuộc trò chuyện"""
    user = update.effective_user
    welcome_message = f"""
👋 Xin chào {user.first_name}!

🎓 Tôi là *Learning Assistant Bot* - Trợ lý học tập của bạn!

✨ *Tôi có thể giúp bạn:*
📚 Học lý thuyết về C#, .NET, JavaScript, TypeScript, ReactJS
💻 Luyện tập với LeetCode và các bài tập code
❓ Trả lời câu hỏi với AI thông minh
📊 Kiểm tra kiến thức với quiz tương tác

💡 *Bạn có thể:*
• Dùng các nút menu bên dưới
• Hoặc gõ câu hỏi tự do bất kỳ lúc nào!

Ví dụ: "Giải thích async/await trong JavaScript"

🤖 /help - Xem hướng dẫn chi tiết
"""
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=get_main_menu(),
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hiển thị hướng dẫn sử dụng"""
    help_text = """
📖 *HƯỚNG DẪN SỬ DỤNG*

🔹 *📚 Học Lý Thuyết:*
   Chọn chủ đề bạn muốn học:
   • C# & .NET
   • JavaScript
   • TypeScript
   • ReactJS
   • Tổng hợp các công nghệ

🔹 *💻 Thực Hành & LeetCode:*
   • Yêu cầu bài tập LeetCode
   • Nhận gợi ý bài tập từ dễ đến khó
   • Bài tập thực hành theo chủ đề

🔹 *❓ Hỏi AI:*
   Đặt câu hỏi bất kỳ về lập trình, bot sẽ trả lời thông minh!

🔹 *📊 Kiểm Tra Kiến Thức:*
   Làm quiz để đánh giá trình độ

*Lệnh khác:*
/start - Bắt đầu lại
/help - Xem hướng dẫn
/topics - Xem các chủ đề học tập
"""
    
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def topics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hiển thị các chủ đề có thể học"""
    topics_text = """
📚 *CÁC CHỦ ĐỀ ĐƯỢC HỖ TRỢ:*

✨ *C# & .NET:*
   • C# Syntax & Basics
   • OOP Concepts
   • LINQ & Collections
   • Entity Framework
   • ASP.NET Core
   • Design Patterns

✨ *JavaScript:*
   • ES6+ Features
   • Async/Await & Promises
   • DOM Manipulation
   • Closures & Scope
   • Modules & Import/Export

✨ *TypeScript:*
   • Type System
   • Interfaces & Types
   • Generics
   • Decorators
   • Advanced Types

✨ *ReactJS:*
   • Components & Props
   • Hooks (useState, useEffect, etc.)
   • Context API
   • State Management
   • Performance Optimization

✨ *LeetCode:*
   • Arrays & Strings
   • Two Pointers
   • Sliding Window
   • Binary Search
   • Trees & Graphs
   • Dynamic Programming

Nhấn *📚 Học Lý Thuyết* để bắt đầu!
"""
    
    await update.message.reply_text(topics_text, parse_mode='Markdown')


async def handle_menu_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý lựa chọn từ menu"""
    text = update.message.text
    
    if text == '📚 Học Lý Thuyết':
        topics_keyboard = [
            [KeyboardButton('C# & .NET'), KeyboardButton('JavaScript')],
            [KeyboardButton('TypeScript'), KeyboardButton('ReactJS')],
            [KeyboardButton('🔙 Về Menu Chính')]
        ]
        await update.message.reply_text(
            "📚 Chọn chủ đề bạn muốn học:",
            reply_markup=ReplyKeyboardMarkup(topics_keyboard, resize_keyboard=True)
        )
        context.user_data['awaiting_topic'] = True
    
    elif text == '💻 Thực Hành & LeetCode':
        await handle_practice_menu(update, context)
    
    elif text == '❓ Hỏi AI':
        await update.message.reply_text(
            "❓ Đặt câu hỏi của bạn (tiếng Việt hoặc tiếng Anh):\n\n"
            "💡 Bạn có thể hỏi bất kỳ lúc nào bằng cách gõ câu hỏi trực tiếp!\n\n"
            "Ví dụ:\n"
            "• 'Giải thích async/await trong JavaScript'\n"
            "• 'What is React hooks?'\n"
            "• 'Làm thế nào để tối ưu query LINQ?'\n\n"
            "🤖 Gõ câu hỏi của bạn ngay bây giờ..."
        )
        context.user_data['awaiting_ai_question'] = True
    
    elif text == '📊 Kiểm Tra Kiến Thức':
        quiz_keyboard = [
            [KeyboardButton('Quiz C#'), KeyboardButton('Quiz JavaScript')],
            [KeyboardButton('Quiz TypeScript'), KeyboardButton('Quiz React')],
            [KeyboardButton('🔙 Về Menu Chính')]
        ]
        await update.message.reply_text(
            "📊 Chọn loại quiz bạn muốn làm:",
            reply_markup=ReplyKeyboardMarkup(quiz_keyboard, resize_keyboard=True)
        )
        context.user_data['awaiting_quiz_type'] = True
    
    elif text == 'ℹ️ Giới Thiệu':
        intro_text = """
🤖 *Giới Thiệu Learning Assistant Bot*

📌 Bot được thiết kế để hỗ trợ bạn học lập trình hiệu quả

🌟 *Tính năng chính:*
   • Học lý thuyết có cấu trúc
   • Bài tập thực hành
   • LeetCode challenges
   • AI-powered assistance
   • Quiz đánh giá

🎯 *Công nghệ hỗ trợ:*
   C#, .NET, JavaScript, TypeScript, ReactJS

💡 *Tips:*
   Sử dụng tính năng 'Hỏi AI' để được tư vấn chi tiết!
"""
        await update.message.reply_text(intro_text, parse_mode='Markdown')
    
    elif text == '🔗 Tài Liệu Tham Khảo':
        resources_text = """
📚 *TÀI LIỆU THAM KHẢO*

🔹 *C# & .NET:*
   • docs.microsoft.com/dotnet
   • dotnet.microsoft.com/learn

🔹 *JavaScript:*
   • MDN Web Docs
   • javascript.info
   • Eloquent JavaScript

🔹 *TypeScript:*
   • typescriptlang.org/docs
   • TypeScript Handbook

🔹 *ReactJS:*
   • react.dev
   • react-tutorial-app

🔹 *LeetCode:*
   • leetcode.com
   • NeetCode.io

💡 Sử dụng bot để được giải thích chi tiết hơn!
"""
        await update.message.reply_text(resources_text, parse_mode='Markdown')
    
    elif text == '🔙 Về Menu Chính':
        await update.message.reply_text(
            "🏠 Về menu chính",
            reply_markup=get_main_menu()
        )
        context.user_data.clear()
    
    # Xử lý chọn chủ đề học tập
    elif text in ['C# & .NET', 'JavaScript', 'TypeScript', 'ReactJS']:
        await handle_learning_topics(update, context, text)
    
    # Xử lý quiz
    elif text.startswith('Quiz'):
        await handle_quiz(update, context, text)
    
    # Xử lý câu hỏi AI (nếu có flag, nhưng giờ không cần nữa vì tự động xử lý)
    elif context.user_data.get('awaiting_ai_question'):
        await handle_ai_question(update, context)
        # Giữ flag để user có thể hỏi tiếp (không clear)
    
    # Xử lý yêu cầu LeetCode hoặc bài tập
    elif context.user_data.get('awaiting_practice'):
        await handle_leetcode_request(update, context)
    
    # Xử lý câu trả lời quiz
    elif 'current_quiz' in context.user_data and text.startswith('📝'):
        quiz_data = context.user_data.get('current_quiz', {})
        user_answer = text.replace('📝', '').strip()
        correct_answer = quiz_data.get('correct', 0)
        
        # Lấy đáp án đúng
        options = quiz_data.get('options', [])
        if correct_answer < len(options):
            correct_text = options[correct_answer]
        else:
            correct_text = "Unknown"
        
        # Check answer
        user_index = -1
        for i, opt in enumerate(options):
            if user_answer in opt or opt in user_answer:
                user_index = i
                break
        
        if user_index == correct_answer:
            result_text = f"✅ *Chính xác!*\n\n"
        else:
            result_text = f"❌ *Sai rồi*\n\n"
            result_text += f"Đáp án đúng: {correct_text}\n\n"
        
        result_text += f"📌 *Giải thích:*\n{quiz_data.get('explanation', 'N/A')}"
        
        # Clear quiz data
        del context.user_data['current_quiz']
        
        # Keyboard về menu
        menu_keyboard = [
            [KeyboardButton('🔙 Về Menu Chính')]
        ]
        
        await update.message.reply_text(
            result_text,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
        )
    
    else:
        # Nếu không match với menu nào, coi như câu hỏi tự do từ user
        # Tự động xử lý bằng AI handler
        await handle_ai_question(update, context)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý lỗi"""
    logger.error(f"Exception while handling an update: {context.error}")
    if update and hasattr(update, 'message') and update.message:
        await update.message.reply_text("❌ Đã xảy ra lỗi. Vui lòng thử lại!")


def main():
    """Khởi động bot"""
    print("🚀 Starting Learning Assistant Bot...")
    
    # Tạo application
    application = Application.builder().token(API_KEY).build()
    
    # Thêm handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("topics", topics_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_selection))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Chạy bot
    print("✅ Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
