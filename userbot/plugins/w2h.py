import time

from telethon import version
from userbot import ALIVE_NAME, StartTime, ultronversion
from ULTRONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "ULTRON User"
ULTRON_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Legend's Choice ULTRONBOT"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="ULTRON$"))
@bot.on(sudo_cmd(pattern="ULTRON$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if ULTRON_IMG:
        ULTRON_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        ULTRON_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        ULTRON_caption += f"     __**BOT STATUS**__\n\n"
        ULTRON_caption += f"**★ Telethon version :** `{version.__version__}`\n"
        ULTRON_caption += f"**★ ULTRONBOT :**`{ultronversion}`\n"
        ULTRON_caption += f"**★ Uptime :** `{uptime}\n`"
        ULTRON_caption += f"**★ Master:** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, ULTRON_IMG, caption=ULTRON_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"      __**BOT STATUS**__\n\n"
            f"**★ Telethon Version :** `{version.__version__}`\n"
            f"**★ ULTRONBOT:** `{ultronversion}`\n"
            f"**★ Uptime :** `{uptime}\n`"
            f"**★ Master:** {mention}\n",
        )
