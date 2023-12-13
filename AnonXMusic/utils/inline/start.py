from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=Berlinsupportmanage),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=6851974966),
            InlineKeyboardButton(text=_["S_B_2"], url=Berlinsupportmanage),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=Asupan_bokepviral),
            InlineKeyboardButton(text=_["S_B_7"], url=xnxx.com),
        ],
    ]
    return buttons
