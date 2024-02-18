from pyrogram.types import InlineKeyboardButton
from Uputt import CMD_HELP
class Data:

    text_help_menu = (
        "**Menu Inline Tikus-Userbot**\n**Prefixes:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Menu", callback_data="reopen")]]
