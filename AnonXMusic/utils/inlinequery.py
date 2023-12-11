from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"𝘿𝙖𝙝 𝙜𝙬 𝙟𝙚𝙙𝙖 𝙮𝙖 𝙢𝙚𝙠 𝙨𝙩𝙧𝙚𝙖𝙢 𝙣𝙮𝙖.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"𝘿𝙖𝙝 𝙜𝙬 𝙍𝙚𝙨𝙪𝙢𝙚 𝙮𝙖 𝙢𝙚𝙠 𝙨𝙩𝙧𝙚𝙖𝙢 𝙣𝙮𝙖.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"𝘿𝙖𝙝 𝙜𝙬 𝙨𝙠𝙞𝙥 𝙮𝙖 𝙢𝙚𝙠 𝙨𝙩𝙧𝙚𝙖𝙢 𝙣𝙮𝙖.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="𝘿𝙖𝙝 𝙜𝙬 𝙚𝙣𝙙 𝙮𝙖 𝙢𝙚𝙠 𝙨𝙩𝙧𝙚𝙖𝙢 𝙣𝙮𝙖.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/c535cd1372d231dcbcbf8.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
