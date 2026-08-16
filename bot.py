from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from deep_translator import GoogleTranslator
import os
import pdfplumber
from docx import Document

# ضع هنا التوكن الجديد الذي حصلت عليه من BotFather
TOKEN 8617398935:AAGoDVPdrtdqnZBnn914Ah4zQdbr52ev2hA

# رسالة الترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في بوت ترجمة الملفات.\n\n"
        "أرسل ملف PDF أو Word أو TXT وسأترجمه إلى العربية."
    )

# ترجمة النص
def translate_text(text):
    return GoogleTranslator(
        source="auto",
        target="ar"
    ).translate(text)

# قراءة PDF
def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

# قراءة Word
def read_docx(path):
    doc = Document(path)
    text = ""
    for p in doc.paragraphs:
        text += p.text + "\n"
    return text
