from config import UPDATES_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def join_updates_channel(bot: Client, msg: Message):
    if not UPDATES_CHANNEL:
        return
    try:
        try:
            await bot.get_chat_member(UPDATES_CHANNEL, msg.from_user.id)
        except UserNotParticipant:
            if UPDATES_CHANNEL.isalpha():
                link = "https://t.me/" + UPDATES_CHANNEL
            else:
                chat_info = await bot.get_chat(UPDATES_CHANNEL)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/183c91fb709d5af2600c3.jpg", caption=f'''
<b>» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ]({link}) ʏᴇᴛ, 
ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !</b>''',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⚡ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ⚡", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the UPDATES_CHANNEL chat : {UPDATES_CHANNEL} !")
