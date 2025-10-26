import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Bot API Key
API_KEY = os.getenv('TELEGRAM_BOT_API_KEY', "7827052914:AAECexwtFx8yM6xZZZr8BZWtkqVOTiy-bZ8")

# Google Gemini API (Optional - for AI features)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# OpenAI API Key (Optional - for AI features)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Các cấu hình khác
MAX_MESSAGE_LENGTH = 4096  # Telegram message limit

# Danh sách chủ đề hỗ trợ
SUPPORTED_TOPICS = {
    'cs': ['C#', '.NET', 'ASP.NET', 'Entity Framework', 'Linq', 'ASP.NET CORE'],
    'js': ['JavaScript', 'ES6', 'Node.js'],
    'ts': ['TypeScript'],
    'react': ['ReactJS', 'Hooks', 'Context API'],
    'leetcode': ['Arrays', 'Strings', 'Dynamic Programming']
}
