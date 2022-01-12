#Aryana yt downloader test with force sub


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
