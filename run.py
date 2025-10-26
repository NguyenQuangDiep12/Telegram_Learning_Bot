#!/usr/bin/env python3
"""
Script khởi chạy bot dễ dàng
"""

import sys
import os

# Kiểm tra dependencies
try:
    import telegram
    print("✅ python-telegram-bot installed")
except ImportError:
    print("❌ python-telegram-bot not found")
    print("📦 Installing requirements...")
    os.system("pip install -r requirements.txt")
    print("✅ Installation complete!")

# Khởi chạy bot
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🤖 Starting Learning Assistant Bot...")
    print("="*50 + "\n")
    
    try:
        import bot
        bot.main()
    except KeyboardInterrupt:
        print("\n\n✅ Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
