## ©copyright infringement on Team Shadow Projects
## support: https://t.me/tgshadow_fighters
## network: https://t.me/teamshadowprojects


import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ChatJoinRequest
import random
from pyrogram.errors import UserNotParticipant
from modules.database.dbchat import add_served_chat, is_served_chat
from modules.__main__ import bot
from modules import __version__
from pytgcalls import (__version__ as pytover)
from sys import version_info

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):  
    await message.reply_photo(
        photo=random.choice(START_IMG_URL),
        caption=f"""**👋🏻 ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ 
ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..
 
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) **
""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("sʜᴀᴅᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/tgshadow_fighters"), 
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/teamshadowprojects"), 
            ],[
            InlineKeyboardButton("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", callback_data="info"), 
            ],[
            InlineKeyboardButton("✚ ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
    
    
@Client.on_message(commandpro(["/alive",]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    await message.reply_photo(
        photo=random.choice(START_IMG_URL),
        caption=f"""ʜᴇʟʟᴏ.. {message.from_user.mention()} ɪᴀᴍ ᴀʟɪᴠᴇ ɴᴏᴡ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="info")
                ]
            ]
        ),
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/02daf1a0d434a29f9d54c.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command("ghelp") & filters.group & ~filters.edited)
async def gelp(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/02daf1a0d434a29f9d54c.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=random.choice(START_IMG_URL), 
        caption="😊 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ʙᴏᴛ sᴛᴀᴛᴜs:\n"
                f"• **ᴜᴘᴛɪᴍᴇ:** **{uptime}**\n"
                f"• **ᴜsᴇʀ:** **{message.from_user.mention()}**\n"
                f"• **sᴛᴀʀᴛ ᴛɪᴍᴇ:** **{START_TIME_ISO}**\n"
                f"• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** **@{GROUP_SUPPORT}**"
              ) 


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("💝 `ᴘᴏɴɢ!!`\n" f"💖 `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command("id") & ~filters.edited) 
async def id(c: Client, message: Message):
    text = """
**ᴛʜɪs ɪs ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ** : `{}`"""
    await message.reply_text(
        text=text.format(
            message.chat.id
        ), 
    ) 


@Client.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ {query.message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ.. 
ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) !**
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("sʜᴀᴅᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/tgshadow_fighters"), 
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/teamshadowprojects"), 
            ],[
            InlineKeyboardButton("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", callback_data="info"), 
            ],[
            InlineKeyboardButton("✚ ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
     

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("command list") 
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ ʜᴇʟʟᴏ ɴᴀᴍsᴛʜᴇ ᴀɴɴᴀ ᴛʜɪs ɪs ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ɢᴜɪᴅᴇ ᴡʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ɴᴇᴅᴅ sᴇʟᴇᴄᴛ ʜᴇʀᴇ.. 
➠ ᴛʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴘʀᴏᴊᴇᴄᴛs](https://t.me/tgshadow_fighters) 
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴜsᴇʀs ᴄᴏᴍᴍᴀɴᴅs•", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("sᴋɪᴘ", callback_data="skip_list"), 
            InlineKeyboardButton("ᴘᴀᴜsᴇ", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("ʀᴇsᴜᴍᴇ", callback_data="resume_list"), 
            InlineKeyboardButton("sᴛᴏᴘ", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="play_list"), 
            InlineKeyboardButton("ᴋɴᴏᴡ ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ", callback_data="id"), 
            ],[
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="source"), 
            ],[
            InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
async def general_list(_, query: CallbackQuery):
    await query.answer("general commands")
    await query.edit_message_text(
        f"""🥳 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
𝟷️⃣ /ᴘʟᴀʏ - ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ   

𝟸️⃣ /sᴏɴɢ - ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ʏᴛ

𝟹️⃣ /ᴀʟɪᴠᴇ - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴꜰᴏ

𝟺️⃣ /ᴘᴀᴜsᴇ - ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 

𝟻️⃣ /ʀᴇsᴜᴍᴇ - ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 

𝟼️⃣ /sᴋɪᴘ - ꜱᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ ꜱᴛʀᴇᴀᴍ 

𝟽️⃣ /sᴛᴏᴘ - ꜱᴛᴏᴘ ᴛʜᴇ ꜱᴛʀᴇᴀᴍɪɴɢ

𝟾️⃣ /ʀᴇʟᴏᴀᴅ - ᴄʟᴇᴀʀ ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ

ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
async def skip_list(_, query: CallbackQuery):
    await query.answer("skiped current song")
    await query.edit_message_text(
        f"""🚩 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/skip ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ sᴋɪᴘ ᴛᴏ ɴᴇxᴛ sᴏɴɢ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**
➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/teamshadowprojects)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(_, query: CallbackQuery):
    await query.answer("pause current playing song")
    await query.edit_message_text(
        f"""💘 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/pause ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ɪɴ ɢʀᴏᴜᴘ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**
➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(_, query: CallbackQuery):
    await query.answer("resume current playing song")
    await query.edit_message_text(
        f"""❤ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/resume ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**
➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/Team_shadowmusic_bot)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(_, query: CallbackQuery):
    await query.answer("stopping current playing song")
    await query.edit_message_text(
        f"""💓 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/end ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴇɴᴅ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**
➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(_, query: CallbackQuery):
    await query.answer("playing song in vc")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/play ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴘʟᴀʏ ᴀ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**
➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("id"))
async def id(_, query: CallbackQuery):
    await query.answer("chat id")
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠ **/id ᴛʏᴘᴇ ɪᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀʀᴇ ᴘᴇʀsᴏɴᴀʟ !**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("source"))
async def source(_, query: CallbackQuery):
    await query.answer("team shadow source code")
    await query.edit_message_text(
        f"""❣️ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠  **sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴄᴏᴍᴘʟᴇᴛᴇ ᴄʟᴏsᴇᴅ sᴏᴜʀᴄᴇ ʀᴇᴘᴏʀᴛɪɴɢ ᴀɴʏ ʙᴜɢs ᴏʀ ʀᴇᴘᴏʀᴛs ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)!**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
💘 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ɪs ᴀ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ɪɴ sᴏ ᴍᴀɴʏ sᴇʀᴠᴇʀ's, ɪᴛ's ᴏɴʟɪɴᴇ sɪɴᴄᴇ 𝟷sᴛ ᴊᴜɴᴇ 𝟸𝟶𝟸𝟸 ᴀɴᴅ ɪᴛ's ᴄᴏɴsᴛᴀɴᴛʟʏ ᴜᴘᴅᴀᴛᴇᴅ \n
💝 ᴛʜɪs ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) \n 
❣️ © ᴏɴ ʙᴇʜᴀʟғ ᴏғ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="home_start")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = me_user.username
    bot_id = me_bot.id
    for member in m.new_chat_members:
        if chat_id in await blacklisted_chats():
            await m.reply(
                "❗️ ᴛʜɪs ᴄʜᴀᴛ ʜᴀs ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ʙʏ sᴜᴅᴏ ᴜsᴇʀ ᴀɴᴅ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ."
            )
            return await bot.leave_chat(chat_id)
        if member.id == bot_id:
            return await m.reply(
                "❤️ ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ᴛʜᴇ **ɢʀᴏᴜᴘ** !\n\n"
                "ᴀᴘᴘᴏɪɴᴛ ᴍᴇ ᴀs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ɪɴ ᴛʜᴇ **ɢʀᴏᴜᴘ**, ᴏᴛʜᴇʀᴡɪsᴇ ɪ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴡᴏʀᴋ ᴘʀᴏᴘᴇʀʟʏ, ᴀɴᴅ ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴄʜᴀᴛ.\n\n"
                "ᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʜᴇɴ ᴛʏᴘᴇ /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴘʀᴏᴊᴇᴄᴛs", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="set_close")
                        ]
                    ]
                )
            )


chat_watcher_group = 10
