import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

# Official ContraCop presale receiving address
PRESALE_ADDRESS = "A5yboTdtu9beoM297MxrN6KfWRPS6u76FKFpWxgMLXZE"

# Temporary referral storage
referrals = {}
referred_by = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    # Handle referral link
    if context.args:
        referrer_id = context.args[0].replace("ref_", "")

        if referrer_id.isdigit():
            referrer_id = int(referrer_id)

            if referrer_id != user_id and user_id not in referred_by:
                referred_by[user_id] = referrer_id
                referrals[referrer_id] = referrals.get(referrer_id, 0) + 1

    keyboard = [
        [InlineKeyboardButton("💰 Presale", callback_data="presale")],
        [InlineKeyboardButton("🔗 Refer & Earn", callback_data="refer")],
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")],
        [InlineKeyboardButton("📊 My Stats", callback_data="stats")],
        [InlineKeyboardButton("🧾 Verify Transaction", callback_data="verify")],
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

    user_id = query.from_user.id

    if query.data == "presale":
        message = (
            "💰 *ContraCop Presale*\n\n"
            "Official presale receiving address:\n\n"
            f"`{PRESALE_ADDRESS}`\n\n"
            "⚠️ Always verify the address before sending funds.\n\n"
            "After completing your purchase, use "
            "🧾 *Verify Transaction* to submit your transaction signature."
        )

        keyboard = [
            [InlineKeyboardButton("🧾 Verify Transaction", callback_data="verify")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "refer":
        link = f"https://t.me/ContraCopAI_bot?start=ref_{user_id}"
        count = referrals.get(user_id, 0)

        message = (
            "🔗 *Refer & Earn*\n\n"
            f"Your personal referral link:\n`{link}`\n\n"
            f"👥 Successful referrals: *{count}*\n\n"
            "Share your link with friends and community members!"
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "leaderboard":
        top = sorted(
            referrals.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        if not top:
            message = (
                "🏆 *Leaderboard*\n\n"
                "No referrals yet.\n"
                "Be the first to start building!"
            )
        else:
            message = "🏆 *Leaderboard*\n\n"

            for position, (user, count) in enumerate(top, 1):
                message += f"{position}. User `{user}` — {count} referrals\n"

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "stats":
        count = referrals.get(user_id, 0)

        message = (
            "📊 *My Stats*\n\n"
            f"👥 Referrals: *{count}*\n"
            "⭐ Points: Coming soon\n"
            "💰 Verified purchases: Coming soon"
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "verify":
        message = (
            "🧾 *Transaction Verification*\n\n"
            "After purchasing from the official presale, "
            "send your Solana transaction signature here.\n\n"
            "The automated blockchain verification system "
            "will be connected next."
        )

        keyboard = [
            [InlineKeyboardButton("💰 Presale", callback_data="presale")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "about":
        message = (
            "🛡️ *About ContraCop*\n\n"
            "ContraCop is an AI-powered Web3 security "
            "and intelligence platform."
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "whitepaper":
        message = (
            "📄 *Whitepaper*\n\n"
            "The official whitepaper link will be added here."
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "community":
        message = (
            "💬 *Community*\n\n"
            "The official community link will be added here."
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "support":
        message = (
            "🆘 *Support*\n\n"
            "Contact the ContraCop team for assistance."
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💰 Presale", callback_data="presale")],
            [InlineKeyboardButton("🔗 Refer & Earn", callback_data="refer")],
            [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")],
            [InlineKeyboardButton("📊 My Stats", callback_data="stats")],
            [InlineKeyboardButton("🧾 Verify Transaction", callback_data="verify")],
            [InlineKeyboardButton("🛡️ ContraCop", callback_data="about")],
            [InlineKeyboardButton("📄 Whitepaper", callback_data="whitepaper")],
            [InlineKeyboardButton("💬 Community", callback_data="community")],
            [InlineKeyboardButton("🆘 Support", callback_data="support")]
        ]

        message = (
            "🛡️ *ContraCop AI*\n\n"
            "Choose an option below:"
        )

    else:
        message = "Welcome to ContraCop AI!"
        keyboard = []

    await query.edit_message_text(
        message,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
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
