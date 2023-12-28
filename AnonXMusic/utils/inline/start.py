from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/Asupanhot_viral"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
