Python
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Pozdrav! Ja sam Sljapkobot! 🤖\n\n"
        "Pratim razvoj projekta za zlato i WTI naftu.\n"
        "Automatsko trgovanje je isključeno.\n\n"
        "Komande:\n"
        "/gold - Zlato\n"
        "/wti - Nafta\n"
        "/traders - Trejderi\n"
        "/status - Status bota"
    )


async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟡 ZLATO XAU/USD\nPraćenje izvora još nije povezano."
    )


async def wti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛢️ WTI NAFTA\nPraćenje izvora još nije povezano."
    )


async def traders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Lista provjerenih trejdera još se priprema."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sljapkobot program je pokrenut.\n"
        "Praćenje signala još nije aktivno.\n"
        "Automatsko trgovanje: ISKLJUČENO."
    )


def main():
    if not TOKEN:
        raise RuntimeError("Telegram token nije podešen.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gold", gold))
    app.add_handler(CommandHandler("wti", wti))
    app.add_handler(CommandHandler("traders", traders))
    app.add_handler(CommandHandler("status", status))

    app.run_polling()


if __name__ == "__main__":
    main()
