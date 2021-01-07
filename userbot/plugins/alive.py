from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mama-userbotb  User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/b85514e03cbfdf471a0c4.mp4"
pm_caption = "__**🔥🔥Mama-userbot is alive!!🔥🔥**__\n\n"

pm_caption += f"✨TELETHON : `1.15.0` \n"

pm_caption += f"✨My Master      : __**{DEFAULTUSER}](tg://user?id={mama-userbot}**__\n"

pm_caption += f"✨Heroku Database: Everything working normally\n"

pm_caption += f"✨Sudo           : `{sudou}`\n"

pm_caption += f"✨CHANNEL   : [ᴊᴏɪɴ](https://t.me/mamauserbot)\n"

pm_caption += f"✨CREATOR    : [Nub Here](https://t.me/mama_bad_op)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/mama-userbot/mama-userbot) 🔹 [📜License📜](https://github.com/mama-userbot/mama-userbot/blob/master/LICENSE)"

pm_caption += f"✨Status     : Check Stats By Doing .stat."

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'hell', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
