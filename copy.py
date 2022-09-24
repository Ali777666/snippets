# Telegram file copying using pyrogram
# pip3 install pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio


FROM = 1216387869
TO = 1204094907
PYRO_SESSION = "AgAGJ0nyQi6em7CasUo4bRxaAO52h4Ay85oZh-oN6580TsFIJYZHrlfRcVoLT4pUWu2-5AXfxgdw7xyLzrqHAqhHwZ2IK8kjraBgjvPlZVGVTDEaDuIa3xJfFdC3-F8DiQd3XuCz5EWE5AbXvNIcKKhKDd29a_a37RxOV6H3txAtL8zeuwB143SXF8r9Iv2w8TZIm_mvmE4ci2zyH9NEhKxwWPzA2xRGHsTUSfoY1qRobW4jmWxdFHWHrPbq2ocMO1UKXrMCF8ghOnx8JfLMMtOtxW43s9Pd-wREM8r0Najfhh2nRooQ8S_g6KakFFBaWj8oelcPjdOffzkrGJQz35HJJvPjngA"
API_ID = 11411895
API_HASH = "62b630c71e03401e3553ab5c59a41901"

user = Client(
    PYRO_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)

@user.on_message(filters.command('copy') & filters.me)
async def copy_files(c, m):
    async for msg in c.iter_history(FROM):
        try:
            if msg.document:  # specify the message type (document|video|photo|...)
                await msg.copy(TO)
        except FloodWait as t:
            await asyncio.sleep(t.x)
  
user.run()
