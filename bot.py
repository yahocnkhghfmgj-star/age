import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تكوين البوت
TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يعمل على Render بنجاح!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 البوت نشط وجاهز للعمل")

def main():
    """الدالة الرئيسية"""
    app = Application.builder().token(TOKEN).build()
    
    # إضافة handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    
    print("🤖 البوت يعمل على Render...")
    app.run_polling()

if __name__ == '__main__':
    main()