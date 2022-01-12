#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import Config
from pyrogram import filters
from pyrogram import Client
from urllib.parse import quote_plus, unquote
import math, os, time, datetime, aiohttp, asyncio, mimetypes, logging
from helpers.download_from_url import download_file, get_size
from helpers.file_handler import send_to_transfersh_async, progress
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from helpers.display_progress import progress_for_pyrogram, humanbytes
from helpers.tools import execute
from helpers.ffprobe import stream_creator
from helpers.url_uploader import leecher2
from helpers.media_info import cinfo2
from helpers.link_info import linfo2

logger = logging.getLogger(__name__)

HELP_TXT = """
سلام 
این بات برای دانلود فیلم از یوتیوب میباشد 

/upload : برای دانلود روی لینک مورد نظر ریپلای کنید
    

@Client.on_message(filters.command(["start"]))
async def start(client , m):
    """Send a message when the command /start is issued."""
    await m.reply_text(text=f"سلام\nبرای دیافت کمک از /help استفاده کنید \n  برای دیگر بات ها میتونید به چنل من مراجعه کنید @The_Aryana_PY")

    
@Client.on_message(filters.command(["help"]))
async def help(client , m):
    """Send a message when the command /help is issued."""
    await m.reply_text(text=f"{HELP_TXT}")   


@Client.on_message(filters.private & filters.command(["upload"]))
async def leecher1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await leecher2(client , u)
    elif not Config.AUTH_USERS:
        await leecher2(client , u)
    else:
        await u.reply_text(text=f"شما اجازه استفاده از بات را ندارید:)", quote=True, disable_web_page_preview=True)
        return
