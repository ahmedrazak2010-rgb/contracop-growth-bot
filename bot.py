import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Presale", callback_data="presale")],
        [InlineKeyboardButton("🔗 Refer & Earn", callback_data="refer")],
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")],
        [InlineKeyboardButton("📊 My Stats", callback_data="stats")],
        [InlineKeyboardButton("🛡️ ContraCop", callback_data="about")],
        [InlineKeyboardButton("📄 Whitepaper", callback_data="whitepaper")],
        [InlineKeyboardButton("💬 Community", callback_data="community")],
        [InlineKeyboardButton("🆘 Support", callback_data="support")]
    ]

    await update.message.reply_text(
        "🛡️ *Welcome to ContraCop AI!*\n\n"
        "Your Web3 security, intelligence and growth hub.\n\n"
        "Choose an option below:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "presale": "💰 *ContraCop Presale*\n\nPresale information will be available here.",
        "refer": "🔗 *Refer & Earn*\n\nYour referral system will appear here.",
        "leaderboard": "🏆 *Leaderboard*\n\nTop contributors will appear here.",
        "stats": "📊 *My Stats*\n\nYour verified activity will appear here.",
        "about": "🛡️ *About ContraCop*\n\nAI-powered Web3 security and intelligence.",
        "whitepaper": "📄 *Whitepaper*\n\nWhitepaper link will be added here.",
        "community": "💬 *Community*\n\nCommunity link will be added here.",
        "support": "🆘 *Support*\n\nContact the ContraCop team for assistance."
    }

    await query.edit_message_text(
        messages.get(query.data, "Welcome to ContraCop!"),
        parse_mode="Markdown"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("ContraCop bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
