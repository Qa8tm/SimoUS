import os
import aiohttp
import requests
import random
import re
import time
import sys
import asyncio
import math
import heroku3
import urllib3
import speedtest
import base64
import psutil
import platform
import json
from subprocess import PIPE
from subprocess import run as runapp
from asyncio.exceptions import CancelledError
from time import sleep
from platform import python_version
from github import Github
from pySmartDL import SmartDL
from pathlib import Path
from telethon.errors import QueryIdInvalidError
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from ..core import check_owner, pool
from datetime import datetime
from telethon import version
from telethon import Button, events ,types 
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from urlextract import URLExtract
from validators.url import url
from userbot import StartTime, iqthon, catversion
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP
from SQL.extras import *
ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"
UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"
ORDERS = gvarstatus("OR_ORDERS") or "(اوامري|أوامري|م)"
IQTHONPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/f16221fabee921fe219ff.mp4"
LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [    "ALIVE_PIC",    "ALIVE_EMOJI",    "ALIVE_TELETHONIQ",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP",]
DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}
IQPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/f16221fabee921fe219ff.mp4"
def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"
@iqthon.on(admin_cmd(pattern=f"{ALIVE}(?: |$)(.*)"))     
async def iq(iqthonevent):
    reply_to_id = await reply_id(iqthonevent)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    iqevent = await edit_or_reply(iqthonevent, "**☭︙ جاري فحص السورس **")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "☭︙"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "𝗐𝖾𝗅𝖼𝗈𝗆𝖾  𓃠"
    IQTHON_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/cb0e2b7df8a639302ec89.jpg"
    tg_bot = Config.TG_BOT_USERNAME
    me = await iqthonevent.client.get_me()
    my_last = me.last_name
    my_mention = f"[{me.last_name}](tg://user?id={me.id})"
    TM = time.strftime("%I:%M")
    iqcaption = gvarstatus("ALIVE_TELETHONIQ") or fahs
    caption = iqcaption.format(        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        my_mention=my_mention,
        TM=TM,
        tg_bot=tg_bot,    )
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        PIC = random.choice(CAT)
        try:
            await iqthonevent.client.send_file(iqthonevent.chat_id, PIC, caption=caption, reply_to=reply_to_id)
            await iqevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(iqevent)
    else:
        await edit_or_reply(iqevent,caption)
fahs = """.𓄌 : المستخدم  {my_mention}  𓇡.
.𓄌 : الوقت  {TM}  𓇡.
.𓄌 : مده التشغيل  {uptime}  𓇡.
.𓄌 : بوتك  {tg_bot}  𓇡.
.𓄌 : البنك  {ping}  𓇡.
.𓄌 : الاصدار 1  𓇡.
.𓄌 : قناة اسلورس  : @ADWSL  𓇡."""
@iqthon.on(admin_cmd(pattern="رابط التنصيب(?: |$)(.*)"))    
async def source(e):
    await edit_or_reply(e, "https://github.com/P9P9/SimoAS",)
@iqthon.on(admin_cmd(pattern="حساب كيثاب( -l(\d+))? ([\s\S]*)"))    
async def _(event):
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, "`" + username + " not found`")
            catevent = await edit_or_reply(event, "**☭︙  جـاري إحضـار معلومـات حساب كيثاب ↯**")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**☭︙  معلومـات الكيثاب لـ :** `{username}`\
                \n**☭︙  الإسـم 👤:** [{name}]({html_url})\
                \n**☭︙  النـوع 🔧:** `{type}`\
                \n**☭︙  الشرڪـة 🏢:** `{company}`\
                \n**☭︙  المدونـة 🔭:**  {blog}\
                \n**☭︙  الموقـع 📍:**  `{location}`\
                \n**☭︙  النبـذة 📝:**  `{bio}`\
                \n**☭︙  عـدد المتابعيـن ❤️:**  `{followers}`\
                \n**☭︙  الذيـن يتابعهـم 👁:**  `{following}`\
                \n**☭︙   عدد ريبو العام 📊:**  `{public_repos}`\
                \n**☭︙  الجمهـور 📄:**  `{public_gists}`\
                \n**☭︙  تم إنشـاء الملـف الشخصـي ✓** 🔗: `{created_at}`\
                \n**☭︙  تم تحديـث الملـف الشخصـي ✓** ✏️: `{updated_at}`".format(
                username=username, **result            )
            if repos:
                REPLY += "\n**☭︙  بعـض الريبوات 🔍 :** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(event.chat_id, ppath, caption=REPLY, reply_to=reply_to)
            os.remove(ppath)
            await catevent.delete()
@iqthon.on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**☭︙  تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
@iqthon.on(admin_cmd(pattern="المده(?: |$)(.*)"))    
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " ٍَ 🖤"
    IQTHON_ALIVE_TEXT = "❬ سورس سيمو - Source Simo ، 🕸  ❭ :"
    IQTHON_IMG = gvarstatus("ALIVE_PIC")
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption += f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**"
        try:
            await event.client.send_file(event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id)
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(event, f"**مدة التشغيل")
    else:
        await edit_or_reply(event, f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**")
@iqthon.on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    
async def _(event):
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (f"☭︙  وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب سورس سيمو @ADWSL :**\n\n{o}")
    await edit_or_reply(event, OUTPUT)

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await iqthon.get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"userbot/plugins/{plugin_name}"):
                return
            downloaded_file_name = await iqthon.download_media(                await iqthon.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "userbot/plugins/",            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await iqthon.send_message(                    BOTLOG_CHATID,                    f"**☭︙   تحـميل المـلف 🗂️  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )

    iqthon.loop.create_task(install())
@iqthon.on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def _(event):
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "**☭︙   تم تحديث سورس سيمو ↻**")
    sandy = await edit_or_reply(event , "☭︙  جـاري تـحديـث سيمو  🔄\n🔹 - قـد يستغـرق الأمـر 5 - 10 دقائـق انتـظـر\nلاتقـم بتحـديث أكثـر من 3 مـرات باليـوم" ,)
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS1.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS1.error(e)
    try:
        delgvar("ipaddress")
        await iqthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS1.error(e)
@iqthon.on(admin_cmd(pattern="مساعده(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"""• اذا كنت تحتاج للمساعدة الرجاء الذهاب الى 

المطور  : @O_8_F
قناة السورس  : @ADWSL
""")
@iqthon.on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "☭︙  بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            "**☭︙   تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **☭︙  عـدد الثوانـي ⏱**",        )
    event = await edit_or_reply(event, f"`☭︙   حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")
    sleep(counter)
    await event.edit("** ☭︙  حسنـاً، أنـا نشـط الآن ᯤ **")
@iqthon.on(admin_cmd(pattern="تاريخ التنصيب$"))
async def psu(event):
    uname = platform.uname()
    softw = "**تاريخ تنصيب **\n ** بوت سورس سيمو لديك :**"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"` {bt.year}/{bt.month}/{bt.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    help_string = f"{str(softw)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(event, f"**☭︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"**☭︙  📑 يرجى متابع قناه السورس تجدها هنا : @ADWSL")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(event, f"**☭︙ قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")
            if not vinfo:
                return await edit_delete(event, f"**☭︙ يـجب وضع القـيمـة الصحـيحه**")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**☭︙ يـجـب وضـع رابـط صحـيح **")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID,f"**☭︙ اضف فـار\n☭︙ {vname} الفارالذي تم تعديله :")
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(event, f"**☭︙  📑 القيـمة لـ {vname} \n☭︙   تـم تغييـرها لـ :-** `{vinfo}`", time=20)
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(event, f"**☭︙  📑 قيـمة الـ {vname}** \n☭︙   هية  `{var_data}`", time=20)
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"**☭︙ حـذف فـار **\n**☭︙ {vname}** تـم حـذف هـذا الفـار **")
            await edit_delete(event,f"**☭︙  📑 قيـمة الـ {vname}** \n**☭︙   تم حذفها ووضع القيمه الاصلية لها**",time=20)
    else:
        await edit_delete(event, f"**☭︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)

@iqthon.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑺𝑰𝑴𝑶- 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                    f"\n **⌔** `{variable} = {heroku_var[variable]}` .\n"                )
            return await ics.edit(                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑺𝑰𝑴𝑶- 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                f"\n **⌔ خطا :**\n-> {variable} غيـر موجود. "            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(                        var.chat_id,                        "configs.json",                        reply_to=var.id,                        caption="`Output too large, sending it as a file`",                    )
                else:
                    await ics.edit(                        "`[HEROKU]` ConfigVars:\n\n"                       "================================"                        f"\n```{result}```\n"                        "================================"                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**⌔ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**⌔ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        else:
            await ics.edit("**⌔ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "⌔ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("⌔ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"⌔ `{variable}`**  غير موجود**")

        await ics.edit(f"**⌔** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        del heroku_var[variable]
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑   اوامر السورس   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑴ ⦙ `.السورس` **✐  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
    ⑶ ⦙ `.حساب كيثاب + اسم الحساب` 
    **✐  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸ ⦙ `.المده` **✐  : يضهر لك مدة تشغيل بوت الوالي لديك ❝** 
    ⑼ ⦙  `.تحديث` **✐ :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع سورس سيمو  ❝
    **⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`**✐ : يقوم بأطفاء سورس سيمو بعدد الثواني الي ضفتها  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑾ ⦙  `.الاوامر` **✐ :   لأضهار جميع اوامر السورس اونلاين❝
    **⑿ ⦙  `.اوامري` **✐ :   لأضهار جميع اوامر السورس كتابه بدون اونلاين❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⒀ ⦙  `.استخدامي` **✐ :   يضهر لك كمية استخدامك لالوالي❝
    **⒁ ⦙  `.تاريخ التنصيب` **✐ :   يضهر لك تاريخ تنصيبك❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰"""    
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order13")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الوقتي   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙ `.اسم وقتي`**✐ : يضع الوقت المزخرف في اسمك تلقائيا ❝
    ** ⑵ ⦙  `.نبذه وقتيه`**✐ : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا ❝**
    ⑶⦙ `.صوره وقتيه`**✐ : يضع لك الوقت لمزخرف في صورتك تغير تلقائي ❝
    **⑷⦙ `.ايقاف + الامر الوقتي`**✐ : الامر الوقتي يعني (اسم وقتي)&(صوره وقتيه) كمثال -  .ايقاف اسم وقتي  ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order14")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑     1 الاوامر المتحركه للتسلية   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    `.غبي`
    `.تفجير`
    `.قتل`
    `.طوبه`
    `.مربعات
    `.حلويات`
    `.نار`
    `.هلكوبتر`
    `.اشكال مربع`
    `.دائره`
    `.قلب `
    `.مزاج`
    `.قرد`
    `.ايد`
    `.العد التنازلي`
    `.الوان قلوب`
    `.عين`
    `.ثعبان`
    `.رجل`
    `.رموز شيطانيه`
    `.قطار`
    `.موسيقى`
    `.رسم`
    `.فراشه`
    `.مكعبات`
    `.مطر`
    `.تحركات`
    `.ايموجيات`
    `.طائره`
    `.شرطي`
    `.النضام الشمسي`
    `.افكر`
    `.اضحك
    `.ضايج`
    `.ساعه متحركه`
    `.بوسه`
    `.قلوب`
    `.رياضه`
    `.الارض`
    `.قمر`
    `.اقمار`
    `.قمور`
    `.زرفه`
    `.بيبي`
    `.تفاعلات`
    `.اخذ قلبي`
    `.اشوفج السطح`
    `.احبك`
    `.اركض`
    `.روميو`
    `.البنك`
    `.تهكير + الرد على شخص`
    `.طياره`\n`.مصاصه`
    `.مصه`\n`.جكه`
    `.اركضلي`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **"""
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordvars")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  اوامـر الـفـارات  ⦒ :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴ ⦙ `.اضف فار + اسم افار + القيمه`
    **✐ :  يضيف اليك الفار الخاص بسورس ❝**
    ⑵ ⦙ `.حذف فار + اسم الفار`
    **✐ :  يحذف الفار الذي اضفته ❝**
    ⑶  ⦙ `.جلب فار + اسم الفار`
    **✐ :  يرسل اليك معلومات الفار وقيمه الفار ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **☣️  ⦑  1  الــفــارات  ⦒  :
    **⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :
    **`.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`
    **⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : 
    **`.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`
    **⑶  ⦙ لأضـافة فار الايمـوجي  : 
    **`.اضف فار ALIVE_EMOJI + الايموجي`
     **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : 
    ** `.اضف فار ALIVE_TEXT + النص`
    **⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**
     `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`
     **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : 
    ** `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`
     **✐ : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :
    **`.تليجراف ميديا + الرد على صورة او فيديو`
     ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **⑺ ⦙  لتغير كليشة الفحص كاملة :
    **`.اضف فار ALIVE_TELETHONIQ + كليشه مع المتغيرات`
    **✐ : متغيرات كليشه الفحص  :
    **1 -  :  `{uptime}` :  مده التشغيل بوتك
    2 -  :  `{my_mention}`  : رابط حسابك 
    3 -  :  `{TM}`  : الوقت 
    4 -  :  `{ping} ` : البنك 
    5 -  : ` {telever} ` : نسخه الوالي 
    6 -  :  `{tg_bot}` :  معرف بوتك 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑻ ⦙ `.اضف فار AUTO_PIC + رابط صورة تليجراف`
    **✐ :  يضيف اليك الفار للصوره الوقتيه ❝
    **⑼ ⦙ `.اضف فار MAX_FLOOD_IN_PMS + العدد`
    **✐ :  يضيف اليك الفار تغير عدد تحذيرات رساله حمايه الخاص ❝
    **⑽ ⦙ `.اضف فار DEFAULT_BIO + الجمله`
    **✐ :  يضيف اليك الفار تغير جمله النبذه الوقتية  ❝
    **""" 
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الحساب 1   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.معرفه + الرد ع الشخص` **✐ : سيجلب لك معرف الشخص ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` **✐ : يجلب لك اسماء الشخص القديمه ❝** 
    ⑶  ⦙ `.انشاء بريد` **✐ : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.ايدي + الرد ع الشخص`**✐ : سيعطيك معلومات الشخص ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ `. الايدي الرد ع الشخص` **✐ : سوف يعطيك ايدي المجموعه او ايدي حسابك ❝
    ** ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑹ ⦙ `.معلومات تخزين المجموعه` **✐ : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑺ ⦙ `.تخزين الخاص تشغيل`**✐ : يجلب لك جميع الرسائل التي تأتي اليك في الخاص ❝
    **⑻ ⦙ . تخزين الخاص ايقاف ✐ : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص ❝
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑼ ⦙ .تخزين الكروبات تشغيل✐ : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات ❝
    ⑽ ⦙ .تخزين الكروبات ايقاف✐ : يوقف لك جميع ارسال الرسائل التي يتم رد عليها ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰"""
    buttons = [[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb2")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الحساب 2   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
     ⑴  ⦙  `.صورته + الرد ع الشخص`**✐ : يجلب صوره الشخص الذي تم رد عليه ❝
    **⑵  ⦙ `.رابطه + الرد ع الشخص`**✐ :  يجلب لك رابط الشخص الذي تم رد عليه  ❝
    **⑶  ⦙ `.اسمه + الرد ع الشخص`**✐ : يجلب لك اسم الشخص الذي تم رد عليه ❝**
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑼ ⦙ `.بنك`**✐ : يقيس سرعه استجابه لدى تنصيبك ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑽ ⦙ `.سرعه الانترنيت`**✐ : يجلب لك سرعه الانترنيت لديك 
    ❝**⑾ ⦙ `.الوقت`**✐ : يضهر لك الوقت والتاريخ واليوم ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑿ ⦙  `.وقتي`**✐ : يضهر لك الوقت والتاريخ بشكل جديد ❝
    **"""
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb3")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  اوامر الحساب  3     ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙ `.حالتي `**✐  :  لفحص الحظر**
    ⑵  ⦙ `.طقس + اسم المدينه `**✐ : يعطي لك طقس المدينه 
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙  `.ازاله التوجيه + الرد على رساله`**✐ : يرسل اليك الرساله التي تم رد عليها بدون توجيه **
    ⑹  ⦙ `.كشف + الرد على شخص`**✐ : رد على شخص يفحص حضر مستخدم**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺ ⦙ `.وضع بايو + الرد على البايو`**✐ : يضع الكلمه التي تم رد عليها في البايو الخاص بك
    **⑻  ⦙ `.وضع اسم + الرد على الاسم`**✐ :  يضع الاسم الذي تم رد عليه في اسمك
    **⑼  ⦙ `.وضع صوره + الرد على صوره`**✐ :  يضع الصوره التي تم رد عليها في حسابك
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑽ ⦙ `.معرفاتي`** ✐ : يجلب جميع المعرفات المحجوزه  في حسابك 
    **⑾ ⦙  `.تحويل ملكية + معرف الشخص`**✐ : يحول ملكيه القناه او المجموعه الى معرف
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑿ ⦙  `.انتحال + الرد على الشخص`**✐ :  ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك 
    **⒀ ⦙ `.الغاء الانتحال + الرد على الشخص`**✐ : يقوم بالغاء الانتحال ويرجع معلومات  المذكوره بالسورس  
    ⒁  ⦙ `.ازعاج + الرد على شخص`**✐ :  يقوم بتكرار الرسائل للشخص المحدد من دون توقف 
    **⒂ ⦙ `.الغاء الازعاج` :  يوقف جميع الازعاجات في المجموعه 
     ⒃  ⦙ `.المزعجهم`**✐ : يضهر اليك جميع الاشخاص الي تزعجهم
    **"""
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb4")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  اوامر الحساب  4     ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙  `.الحماية تشغيل`**✐ : يقوم بتشغيل الحمايه ❝
    **⑵  ⦙ `.الحماية ايقاف`**✐ :  يقوم بتعطيل الحمايه❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑶  ⦙ `.قبول`**✐ : يقوم بقبول الشخص للأرسال اليك بدون حظره ❝
    **⑷  ⦙  `.رفض`**✐ :  الغاء قبول الشخص من الارسال وتحذيره ايضا❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑸  ⦙ `.مرفوض`**✐ :  حظر الشخص من دون تحذير حظر مباشر م الخاص ❝
    **⑹  ⦙  `.المقبولين`**✐ :  عرض قائمة المقبولين في الحماية ❝
    **⑺ ⦙   `.جلب الوقتيه + الرد على الصورة`**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑻  ⦙  `.تاك بالكلام + الكلمه + معرف الشخص`**✐:  يسوي تاك للشخص بالرابط جربه وتعرف ❝
    **⑼  ⦙ `.نسخ + الرد على رساله`**✐:  يرسل الرساله التي رديت عليها ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑽ ⦙  `.احسب + المعادله`**✐:  يجمع او يطرح او يقسم او يجذر المعادله الأتية ❝
    **"""
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1hs")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الحساب   ⦒  :**"""
    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="usage(?: |$)(.*)"))    
async def dyno_usage(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",)
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")
    user_id = Heroku.account().id
    headers = {"User-Agent": useragent, "Authorization": f"Bearer {Config.HEROKU_API_KEY}", "Accept": "application/vnd.heroku+json; version=3.account-quotas"}
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(f"**Dyno Usage**:\n\n -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n  •  `{AppHours}`**h**  `{AppMinutes}`**m** **|**  [`{AppPercentage}`**%**] \n\n  -> `Dyno hours quota remaining this month`:\n •  `{hours}`**h**  `{minutes}`**m|**  [`{percentage}`**%**]")
@iqthon.on(admin_cmd(pattern="(herokulogs|logs)(?: |$)(.*)"))    
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply( " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")
    data = app.get_log()
    await edit_or_reply(dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **")
def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )
    return indentitems(items, indent, level=0)
@iqthon.on(admin_cmd(pattern="استخدامي$"))
async def psu(event):
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu = "**حجم استخدامك لالوالي :**\n"
    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"
    svmem = psutil.virtual_memory()
    help_string = f"{str(cpuu)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    catevent = await edit_or_reply(event, "**☭︙   جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")
    start = time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await catevent.edit(                """**☭︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**☭︙   التنزيل 📶 :** `{} (or) {} ميغا بايت`
**☭︙   الرفع 📶 :** `{} (or) {} ميغا بايت`
**☭︙   البنك :** {}` بالثانية`
**☭︙   مزود خدمة الإنترنت 📢 :** `{}`
**☭︙   تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )
        else:
            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )
            await event.delete()
    except Exception as exc:
        await catevent.edit(            
"""**☭︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**☭︙   التنزيل 📶:** `{} (or) {} ميغا بايت`
**☭︙   الرفع 📶:** `{} (or) {} ميغا بايت`
**☭︙   البنك :** {}` بالثانية`
**☭︙  مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("تنصيب") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.url("1- قناة السورس", "https://t.me/ADWSL"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://replit.com/@telethon-Arab/generatestringsession#start.sh"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://dashboard.heroku.com/new?template=https://github.com/P9P9/SimoAS"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/O_8_F"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help1, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=help1,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=help1,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="تنصيب"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "تنصيب")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الالعاب 1   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **⑴  ⦙  نسب وهميه :
    **`.نسبه الحب + الرد ع الشخص`
    `. نسبه الانحراف + الرد ع الشخص `
    `.نسبه الكراهيه + الرد ع الشخص`
    `.نسبه المثليه +الرد ع الشخص`
    `. نسبه النجاح + الرد ع الشخص`
    `.نسبه الانوثه + الرد ع الشخص `
    `.نسبه الغباء + الرد ع الشخص`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    **⑵  ⦙  رفع وهمي :
    **`.رفع زباله + الرد ع الشخص `
    `.رفع منشئ + الرد ع الشخص `
    `.رفع مدير + الرد ع الشخص`
    `.رفع مطور + الرد ع الشخص` 
    `.رفع مثلي + الرد ع الشخص` 
    `.رفع كواد + الرد ع الشخص` 
    `.رفع مرتبط + الرد ع الشخص`
    `.رفع مطي + الرد ع الشخص`
    `.رفع كحبه + الرد ع الشخص` 
    `.رفع زوجتي + الرد ع الشخص`
    `.رفع صاك + الرد ع الشخص` 
    `.رفع صاكه + الرد ع الشخص`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑶  ⦙ `.كت`**✐ : لعبه اسأله كت تويت عشوائيه ❝
    **⑷  ⦙ `.اكس او` **✐ :  لعبه اكس او دز الامر و اللعب ويا صديقك ❝
    **⑸  ⦙  `.همسه + الكلام + معرف الشخص` **✐ : يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  ❝
    **"""
    buttons = [[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play2")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الالعاب 2   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    **⑻ ⦙ `.رسم شعار + الاسم` **✐ : يرسم شعار للأسم  ❝
    **⑼ ⦙ `.نص ثري دي + الكلمه`**✐ : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  ❝
    **⑽ ⦙ `.كلام متحرك + الكلام`**✐ : يقوم بكتابه الكلام حرف حرف  ❝
    **⑾  ⦙  `.ملصق متحرك + الكلام`**✐ : يقوم بكتابه الكلام بملصق متحرك  ❝
    **⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`**✐ :  قم بتجربه الامر لتعرفه +18  ❝
    **⒀ ⦙ `.رسم قلوب + الاسم`**✐ : يكتب الاسم ع شكل قلوب  ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰n"""
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play3")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  اوامر الالعاب 3  ⦒  :
    **⑴  ⦙  `.كتابه وهمي + عدد الثواني`
    ⑵  ⦙  `.فيديو وهمي + عدد الثواني`
    ⑶  ⦙  `.صوره وهمي + عدد الثواني`
    ⑷  ⦙  `.جهه اتصال وهمي + عدد الثواني`
    ⑸  ⦙  `.موقع وهمي + عدد الثواني`
    ⑹  ⦙  `.لعب وهمي + عدد الثواني`
    """
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1pl")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑   اوامر الالعاب   ⦒  :**"""
    buttons = [[Button.inline("اوامر الالعاب  1", data="play1"),],[Button.inline("اوامر الالعاب 2", data="play2"),],[Button.inline("اوامر الالعاب 3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  1 اوامر تحويل الصيغ  ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`**✐ : يحول صوت mp3 الى بصمه ❝
    **⑵  ⦙  `.تحويل صوت + الرد ع الصوت` **✐ :  يحول البصمه الى صوت   mp3
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` **✐ :  يحول الصوره الى ملصق ❝
    **⑷  ⦙ `. تحويل صوره + الرد ع الملصق` **✐ :  يحول الملصق الى صوره ❝
    ⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` **✐ :  يقوم بتحويل الفيديو الى متحركه ❝
    ⑺ ⦙ `.ملصقي + الرد ع الرساله` **✐ : يحول رساله الى ملصق ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره` **✐ :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف   ❝
    **⑼ ⦙  `.تحويل رساله + الرد ع الملف`**✐ :  يقوم بجلب جميع الكتابه الذي داخل الملف  ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`**✐ : يحول الفيديو الى فيديو دائري مرئي ❝
    **⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق`**✐ :  يحول الملصق الى ملصق دائري** 
    """
    buttons = [[Button.inline("اوامر تحويل الصيغ  2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag2")))
@check_owner
async def inlineiqthon(iqthon):
    text = """**🚹  ⦑  2 اوامر تحويل الصيغ   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
     ⑿ ⦙  `.ترجمه en + الرد ع الرساله` **✐ :  يقوم بترجمه الرساله الى اللغه الانكليزيه
    **⒀ ⦙ `.ترجمه ar + الرد ع الشخص`**✐ :  يقوم بترجمه الرساله الى اللغه العربيه ❝
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰"""
    buttons = [[Button.inline("اوامر تحويل الصيغ  1", data="shag1"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordsag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الصيغ   ⦒  :**"
    buttons = [[Button.inline("اوامر الصيغ  1", data="shag1"),],[Button.inline("اوامر الصيغ 2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern=f"{ORDERS}(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
 ✐  ⦗ اوامـر سـورس سيمو ⦘
                                             
 『`.م1`』: اوامر الحساب و الفارات  
 『`.م2`』: اوامر الكروب والتكرار   
 『`.م3`』: اوامر الالعاب و التسليه    
 『`.م4`』: اوامر البصمات و الزخرفه                           
 『`.م5`』: اوامر الاعلانات و الوقتي                           
 『`.م6`』: اوامر السورس و الملصقات 
 『`.م7`』: اوامر التنزيلات و الوسائط 
 『`.م8`』: اوامر الصيغ و الترجمه 
 ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰                                    
 """)
@iqthon.on(admin_cmd(pattern="م1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر الحساب1`)
    (`اوامر الحساب2`)
    (`اوامر الحساب3`)
    (`اوامر الفارات`)
    """)
@iqthon.on(admin_cmd(pattern="م2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر الكروب1`)
    (`اوامر الكروب2`)
    (`اوامر الكروب3`)
    (`اوامر التكرار`)
    """)
@iqthon.on(admin_cmd(pattern="م3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر الالعاب1`)
    (`اوامر الالعاب2`)
    (`اوامر الالعاب3`)
    (`اوامر التسليه1`)
    (`اوامر التسليه2`)
    """)
@iqthon.on(admin_cmd(pattern="م4(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر البصمات1`)
    (`اوامر البصمات2`)
    (`اوامر البصمات3`)
    (`اوامر الزخرفه`)
    """)
@iqthon.on(admin_cmd(pattern="م5(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر الاعلانات`)
    (`اوامر الوقتي`)
    """)
@iqthon.on(admin_cmd(pattern="م6(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر السورس`)
    (`اوامر الملصقات`)
    """)
@iqthon.on(admin_cmd(pattern="م7(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر التنزيلات`)
    (`اوامر الوسائط`)
    """)
@iqthon.on(admin_cmd(pattern="م8(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    (`اوامر الصيغ`)
    (`اوامر الترجمه`)
    """)
@iqthon.on(admin_cmd(pattern="اوامر الالعاب1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """**🚹  ⦑   اوامر الالعاب 1   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    **`.نسبه الحب + الرد ع الشخص`
    `. نسبه الانحراف + الرد ع الشخص `
    `.نسبه الكراهيه + الرد ع الشخص`
    `.نسبه المثليه +الرد ع الشخص`
    `. نسبه النجاح + الرد ع الشخص`
    `.نسبه الانوثه + الرد ع الشخص `
    `.نسبه الغباء + الرد ع الشخص`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    **⑵  ⦙  رفع وهمي :
    **`.رفع زباله + الرد ع الشخص `
    `.رفع منشئ + الرد ع الشخص `
    `.رفع مدير + الرد ع الشخص`
    `.رفع مطور + الرد ع الشخص` 
    `.رفع مثلي + الرد ع الشخص`
    `.رفع كواد + الرد ع الشخص` 
    `.رفع مرتبط + الرد ع الشخص`
    `.رفع مطي + الرد ع الشخص`
    `.رفع كحبه + الرد ع الشخص` 
    `.رفع زوجتي + الرد ع الشخص`
    `.رفع صاك + الرد ع الشخص` 
    `.رفع صاكه + الرد ع الشخص`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑶  ⦙ `.كت`**✐ : لعبه اسأله كت تويت عشوائيه ❝**
    ⑷  ⦙ `.اكس او` **✐ :  لعبه اكس او دز الامر و اللعب ويا صديقك ❝
    **⑸  ⦙  `.همسه + الكلام + معرف الشخص`**✐ : يرسل همسه سريه  
    ❝**""")
@iqthon.on(admin_cmd(pattern="اوامر الالعاب2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر الالعاب 2   ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    **⑻ ⦙ `.رسم شعار + الاسم` 
    **✐ : يرسم شعار للأسم  ❝**
    ⑼ ⦙ `.نص ثري دي + الكلمه`
    **✐ : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  ❝**
    ⑽ ⦙ `.كلام متحرك + الكلام`
    **✐ : يقوم بكتابه الكلام حرف حرف  ❝**
    ⑾  ⦙  `.ملصق متحرك + الكلام`
    **✐ : يقوم بكتابه الكلام بملصق متحرك  ❝**
    ⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`
    **✐ :  قم بتجربه الامر لتعرفه +18  ❝**
    ⒀ ⦙ `.رسم قلوب + الاسم`
    **✐ : يكتب الاسم ع شكل قلوب  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰   
    ⑴  ⦙  `.كتابه وهمي + عدد الثواني`
    ⑵  ⦙  `.فيديو وهمي + عدد الثواني`
    ⑶  ⦙  `.صوره وهمي + عدد الثواني`
    ⑷  ⦙  `.جهه اتصال وهمي + عدد الثواني`
    ⑸  ⦙  `.موقع وهمي + عدد الثواني`
    ⑹  ⦙  `.لعب وهمي + عدد الثواني`""")

@iqthon.on(admin_cmd(pattern="اوامر الصيغ(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر تحويل الصيغ  ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`
    **✐ : يحول صوت mp3 الى بصمه ❝**
    ⑵  ⦙  `.تحويل صوت + الرد ع الصوت` 
    **✐ :  يحول البصمه الى صوت   mp3**
    ⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` 
    **✐ :  يحول الصوره الى ملصق ❝**
    ⑷  ⦙ `. تحويل صوره + الرد ع الملصق` 
    **✐ :  يحول الملصق الى صوره ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` 
    **✐ :  يقوم بتحويل الفيديو الى متحركه ❝**
    ⑺ ⦙ `.ملصقي + الرد ع الرساله` 
    **✐ : يحول رساله الى ملصق ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره`
    **✐ :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف للأستخدام  ❝**
    ⑼ ⦙  `.تحويل رساله + الرد ع الملف` 
    **✐ :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`
    **✐ : يحول الفيديو الى فيديو دائري مرئي ❝**
    ⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق` 
    **✐ :  يحول الملصق الى ملصق دائري** 
    """)
@iqthon.on(admin_cmd(pattern="اوامر الزخرفه(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   لأوامر الزخرفة    ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.غمق + الرد على رساله` **✐ :  يحول خط الرسالة غامقه  ❝** 
    ⑵  ⦙ `.ينسخ + الرد على رساله` **✐ :  يحول خط الرساله الى كلام ينسخ  ❝** 
    ⑶  ⦙ `.خط سفلي + الرد على رساله` **✐ :   يضيف الى خط رساله خط سفلي ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.كتابه + الكلام بالانكلش` **✐ : يكتب الكلام على ورقه بخط اليد 100% ❝** 
    ⑸  ⦙ `.زخرفه_انكليزي + الاسم` **✐ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول ❝**
    ⑹ ⦙ `.زخرفه_عربي + الاسم` **✐ : يزخرف الاسم العربي لعده زخرفات ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑺ ⦙  `.بايوهات1`**✐ :  يعطيك بايو انستا متعدده 1 ❝**
    ⑻ ⦙ .بايوهات2**✐ :  يعطيك بايو انستا متعدده 2 ❝**
    ⑼ ⦙  .رموز1**✐ :  يعطيك رموز للزخرفه 1 ❝**
    10 ⦙ .رموز2**✐ :  يعطيك رموز للزخرفه2 ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
""")
@iqthon.on(admin_cmd(pattern="اوامر التكرار(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑    اوامر التكرار   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.تكرار + الكلمة + العدد` 
    **✐ :  يرسل الكلمة يكررها على عدد المرات  ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑵  ⦙ `.تكرار حزمه الملصقات + الرد على ملصق` 
    **✐ :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   ❝** 
    ⑶  ⦙ `.تكرار_احرف  + الكلمة` 
    **✐ :   يكرر الك احرف الكلمة حتى لو جملة ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.تكرار_كلمه  + الجملة` 
    **✐ : يكرر الك كلام الجملة ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ `.مؤقت  + عدد الثواني + عدد مرات + الجملة` 
    **✐ : يرسل اليك الجملة كل وقت معين ❝**
    """)
@iqthon.on(admin_cmd(pattern="اوامر الترجمه(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    **🚹  ⦑    اوامر الترجمه   ⦒  :
    `.ترجمه en + الرد ع الرساله` **✐ :  يقوم بترجمه الرساله الى اللغه الانكليزيه**
    `.ترجمه ar + الرد ع الشخص` **✐ :  يقوم بترجمه الرساله الى اللغه العربيه ❝**
    **""")
@iqthon.on(admin_cmd(pattern="اوامر الالعاب3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر الالعاب 3    ⦒  :
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.شوت + الكلمة` **✐ :  امر تسليه جربه وتعرف  ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑵  ⦙ `.كتابه + الكلام بالانكلش` **✐ :   يكتب الكلام على ورقه بخط اليد 100%   ❝** 
    ⑶  ⦙ ** اضـافه العـاب اخـرى فقط قم بنسخ الأمر وارسالـة    :- **
    1. - `.لعبه تيك توك اربعه` 
    2. - `.لعبه تيك توك اثنان 3` 
    3. - `.لعبه ربط أربعة` 
    4. - `.لعبه قرعة` 
    5. - `.لعبه حجر-ورقة-مقص` 
    6. - `.لعبه روليت` 
    7. - `.لعبه داما` 
    8. - `.لعبه داما تجمع`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰    
    ⑴  ⦙ `.هديه + الكلام` **✐ :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  ❝** 
    ⑵  ⦙ `.ضفدع + الكلمه` **✐ :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   ❝** 
    ⑶  ⦙ `.لافته + الكلمه` **✐ :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف   ❝** 
    ⑷  ⦙ `.تكرار_كلمه  + الجملة` **✐ : يكرر الك كلام الجملة ❝** 
    ⑸  ⦙ `.صفق + الرد على الكلام` **✐ : جربه وتعرف مضحك ❝**
    ⑹ ⦙ `.حضر وهمي + الرد على شخص` **✐ : حظر وهمي جربه وتعرف ❝**
    ⑺ ⦙ `.خط ملصق + الكلمه`**✐ : يدعم انكليزي فقط + يحول الكتابه لملصق ❝**
    8 ⦙ `.شعر`**✐ : يرسل الك شعر ميمز او مضحك ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ """)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordahln1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑  اوامر الاعلانات   ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.مؤقته + الوقت بالثواني + رساله`**✐ :  يرسل الرساله لمده معينه وتحذف**
    ⑵  ⦙ `.للكروبات + الرد على الرساله`**✐ :  يرسل الرسالها الى جميع المجموعات**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑶  ⦙ `.مؤقت + عدد ثواني + عدد الرسائل + كليشة` **✐ :  يقوم بارسال رساله وقتيه محدده لكل وقت معين وعدد مرات معين**
    ⑷  ⦙ `.اضافه + رابط الكروب`✐ :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    يجب ان تتاكد انو مامحضور حسابك ارسل  ⬅️ ( `.حالتي` ) 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    """
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الاعلانات(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الاعلانات(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.on(admin_cmd(pattern="اوامر التنزيلات(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر التنزيلات    ⦒  :
    **⑴  ⦙ `.بحث صوت + اسم الاغنيه`**✐ : سيحمل لك الاغنية صوت رابط او اسم ❝**
    ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` **✐ : سيحمل لك الاغنية  فيديو رابط او اسم ❝**
    ⑶  ⦙ `.معلومات الاغنيه` **✐ : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.كوكل بحث + موضوع البحث`**✐ : يجلب لك معلومات الموضوع من كوكل ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`**✐ : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو ❝**
    ⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`**✐ : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`**✐ : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني ❝**
    ⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`**✐ : يحمل فيديو تيك توك بدون العلامه المائيه** ❝
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """)
@iqthon.on(admin_cmd(pattern="اوامر الوسائط(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""**
    🚹  ⦑   اوامر الوسائط    ⦒  :
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙ `.سمول + الرد على ملصق او صوره او فيديو` **✐  : يقوم بتصغير الوسائط **
    ⑵ ⦙ `.عكس الالوان + الرد على ملصق او صوره او فيديو`**✐  : يعكس الالوان الموجودة في الوسائط**
    ⑶ ⦙ `.فلتر احمر + الرد على ملصق او صوره او فيديو`**✐  : يقوم باضافه فلتر احمر الى وسائط**
    ⑷ ⦙ `.فلتر رصاصي + الرد على ملصق او صوره او فيديو`**✐  :  يقوم باضافه فلتر رصاصي الى وسائط**
    ⑸ ⦙ `.يمين الصوره + الرد على ملصق او صوره او فيديو )`**✐  : يقوم بتحويل وجهه الوسائط الى اليمين**
    ⑹ ⦙ `.قلب الصوره + الرد على ملصق او صوره او فيديو`**✐  : يقلب الوسائط من فوق لتحت**
    ⑺ ⦙ `.زوم + الرد على ملصق او صوره او فيديو`**✐  :  يقوم بتقريب على الوسائط**
    ⑻ ⦙ `.اطار + الرد على ملصق او صوره او فيديو`**✐  : يضيف اطار الى الوسائط**
    ⑼ ⦙ `.لوقو + الاسم`**✐  : يقوم بصنع logo خاص بك**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **""")
@iqthon.on(admin_cmd(pattern="اوامر الكروب1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑  اوامر الكروب 1     ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙ `.كتم + الرد ع الشخص`**✐ : يكتم الشخص من الخاص او الكروبات (صلاحيه) ❝**
    ⑵  ⦙ `. الغاء كتم + الرد ع الشخص`**✐ :  يجلب لك جميع معرفات المشرفين في الكروب  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑶  ⦙ `.البوتات`**✐ : يجلب لك جميع معرفات البوتات في الكروب ❝**
    ⑷  ⦙ `.الأعضاء`**✐ : اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  ❝** 
    ⑸  ⦙ `.معلومات`**✐ : سيرسل لك جميع معلومات الكروب بالتفصيل ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑹ ⦙ `.مسح المحظورين`**✐ : يمسح جميع المحظورين في الكروب ❝**
    ⑺ ⦙ `.المحذوفين`**✐ : يجلب لك جميع الحسابات المحذوفه ❝**
    ⑻ ⦙ `.المحذوفين تنظيف`**✐ : يمسح جميع الحسابات المحذوفه في الكروب ❝**
    ⑼ ⦙ `.احصائيات الاعضاء`**✐ : يجيب احصائيات الاعضاء في الكروب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑽ ⦙ `.انتحال + الرد ع الشخص`**✐ : يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف ❝**
    ⑾ ⦙ `.الغاء الانتحال + الرد ع الشخص`**✐ : يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙ `.حظر عام + الرد على شخص` 
    **✐ : يحضر الشخص من جميع الكروبات الي عندك  ❝** 
    ⑵  ⦙ `.الغاء حظر عام + الرد على شخص` 
    **✐ :  يلغي حضر العام للشخص  ❝** 
    ⑶  ⦙ `.المحظورين عام` 
    **✐ :   يضهر الك جميع الاشخاص الي حاضرهم عام ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.تقيد + الرد على شخص` 
    **✐ : يقيد الشخص من المجموعة ❝** 
    ⑸  ⦙ `.اكتم + الوقت بثواني + المدة` 
    **✐ : كتم وقتي للشخص  : ❝**
    ⑹ ⦙ `.احظر + الوقت بثواني + المدة` **✐ :حظر وقتي للشخص  :  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """)
@iqthon.on(admin_cmd(pattern="اوامر الكروب2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر الكروب 2   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙  `.ترحيب + الرساله` **✐ : يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  ❝**
    ⑵  ⦙   `.مسح الترحيبات` **✐ :  ييقوم بمسح الترحيب من الكروب ❝**
    ⑶   `.ترحيباتي` **✐ :  يضهر لك جميع الترحيبات التي وضعتها في الكروب ❝**
    ⑷  ⦙ `.رساله الترحيب السابقه تشغيل`  **✐ :  عندما يحدث تكرار سيحذف رساله الترحيب ❝**
    ⑸  ⦙  `.رساله الترحيب السابقه ايقاف`**✐ :  عندما يحدث تكرار لا يحذف رساله الترحيب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑹ ⦙  `.اضف رد + الكلمه` **✐ :  مثلاً تدز رساله هلو تسوي عليها رد بهلوات ❝**
    ⑺ ⦙ `.مسح رد + الكلمه` **✐ :  سيحذف الكلمه الي انت ضفتها ❝**
    ⑻ ⦙  `.جميع الردود` **✐ :  يجلب لك جميع الردود الذي قمت بأضافتها  ❝**
    ⑼ ⦙  `.مسح جميع الردود` **✐ :  يمسح جميع الردود الي انت ضفتها ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑽ ⦙  `.صنع مجموعه + اسم المجموعه`**✐ : يقوم بعمل مجموعه خارقه ❝**
    ⑾ ⦙  `.صنع قناه +  اسم القناة`**✐ : يقوم بعمل قناه خاصه  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑿ ⦙ `.عدد رسائلي`**✐ : سيظهر لك عدد رسائلك في الكروب ❝**
      ⦙ `.جلب الاحداث`**✐ :  يرسل اليك اخر 20 رساله محذوفه في المجموعة من الاحداث**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙ `.تحذير التكرار + عدد رسائل`**✐ :  اي شخص بلكروب يكرر رسائل مالته بلعدد المحدد يقيدة مهما كان رتبته**
    ⑵  ⦙ ` .تحذير تكرار 99999 `✐ :  هذا الامر ستعمله من تريد تلغي التحذير لان مستحيل احد يكرر هل عدد ف اعتبار ينل(غي التحذير**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑶  ⦙ ` .حظر + الرد على شخص`✐ : حظر الشخص من المجموعه او الكروب**
    ⑷  ⦙ ` .الغاء الحظر + الرد على شخص`✐ :  يلغي حظر الشخص من المجموعه او الكروب**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺  ⦙ ` .تنزيل مشرف + الرد على شخص`
    ✐ :  يقوم بازاله الشخص من الاشراف **
    ⑻  ⦙ ` .تثبيت + الرد على رساله`
    ✐ : شرح : تثبيت الرساله التي رديت عليها**⒀  ⦙ `.الأعضاء`
    **✐ :  اضهار قائمة الاعضاء للمجموعة اذا هواي يرسلك ملف كامل لمعلوماتهم**
    """)
@iqthon.on(admin_cmd(pattern="اوامر الكروب3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑  اوامر الكروب 3     ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.تنظيف الوسائط` ✐: ينضف جميع ميديا من صور وفديوهات و متحركات** او ( `.تنظيف الوسائط + العدد`) ** 
    ⑵  ⦙ `.حذف الرسائل`**✐ :  يحذف جميع الرسائل بلكروب ** ` او  `.حذف الرسائل + العدد 
    ⑶  ⦙ `.مسح + الرد على رسالة`**✐ :  يحذف الرساله الي راد عليها فقط **
    ⑷  ⦙ `.غادر + بلكروب دزها`**✐ :  يغادر من المجموعه او من القناة**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ ` .تفليش`**✐ :  يطرد جميع الي بلكروب الامر صار احسن ومتطور واسرع** 
    ⑹  ⦙ `.اضافه + رابط الكروب `**✐ :  يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك ( يجب ان تتاكد انو مامحضور حسابك ارسل ⬅️( .فحص الحظر ) علمود تتاكد حسابك محظور او لا) 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺  ⦙ `.جلب الوقتيه + الرد على الصورة`**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑻  ⦙ `.تاك بالكلام + الكلمه + معرف الشخص`**✐ :  يسوي تاك للشخص بالرابط جربه وتعرف**
    ⑼  ⦙ `.نسخ + الرد على رساله`**✐ :  يرسل الرساله التي رديت عليها **
    ⑽  ⦙ `.ابلاغ الادمنيه`**✐ :  يسوي تاك لجميع الادمنيه ارسله هذا الامر بلمجموعه في حاله اكو تفليش او مشكلة**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑾  ⦙ `.المشرفين` **✐ : يجيب الك جميع المشرفين في المجموعه او القناه**
    ⑿  ⦙ `.البوتات` **✐ :  يجيب الك جميع بوتات في المجموعه او قناه**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙  `.تفعيل حمايه المجموعه`**✐ : يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل❝** 
    ⑵  ⦙ `تعطيل حمايه المجموعه`**✐ :  يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده❝**
    ⑶  ⦙ `.صلاحيات المجموعه`**✐ : يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه❝**
    ⑷  ⦙  `.رفع مشرف + الرد على شخص`**✐ : يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ `.منع + كلمة`**✐ : منع كلمه من الارسال في الكروب**❝
    ⑹ ⦙ `.الغاء منع + كلمه`**✐ : يقوم بالغاء منع الكلمه ❝** 
    ⑺ ⦙ `.قائمه المنع`**✐ : يقوم بجلب جميع الكلمات الممنوعه في الكروب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑻ ⦙ ` .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️`
    ( 10 - 50 - 100 - 200  )**✐ : يجلب لك الاعضاء بالروابط بالعدد المحدد ❝** 
    ⑼ ⦙ `.معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️`
    ( 10 - 50 - 100 - 200  )**✐ :جلب لك معرفات الاعضاء بالعدد المحدد ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordSONG")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑   اوامر التنزيلات والبحث الاغاني    ⦒  :
    **⑴  ⦙ `.بحث صوت + اسم الاغنيه`**✐ : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**
    ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` *✐ : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**
    ⑶  ⦙ `.معلومات الاغنيه` **✐ : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.كوكل بحث + موضوع البحث`**✐ : يجلب لك معلومات الموضوع من كوكل ❝**
    ⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`**✐ : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو ❝**
    ⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`**✐ : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`**✐ : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني ❝**
    ⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`**✐ : يحمل فيديو تيك توك بدون العلامه المائيه** ❝

    """
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="اوامر الحساب1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر الحساب 1   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.معرفه + الرد ع الشخص` **✐ : سيجلب لك معرف الشخص ❝** 
    ⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` **✐ : يجلب لك اسماء الشخص القديمه ❝** 
    ⑶  ⦙ `.انشاء بريد` **✐ : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑷  ⦙ `.ايدي + الرد ع الشخص` **✐ : سيعطيك معلومات الشخص ❝** 
    ⑸  ⦙ `. الايدي الرد ع الشخص` **✐ : سوف يعطيك ايدي المجموعه او ايدي حسابك ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑹ ⦙ `.معلومات تخزين المجموعه` **✐ : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين ❝**
    ⑺ ⦙ `.تخزين الخاص تشغيل`**✐ : يجلب لك جميع الرسائل التي تأتي اليك في الخاص ❝**
    ⑻ ⦙ . تخزين الخاص ايقاف ✐ : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص ❝
    ⑼ ⦙ .تخزين الكروبات تشغيل✐ : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات ❝
    ⑽ ⦙ .تخزين الكروبات ايقاف✐ : يوقف لك جميع ارسال الرسائل التي يتم رد عليها ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.كول + الكلمة` **✐ : لازم ضيف بوتك يحجي بدالك البوت ❝** 
    ⑵  ⦙ `.وضع النائم + السبب` **✐ : اي شخص يسويلك تاك او يراسلك او يرد عليك يرد عليه بوتك  ❝** 
    ⑶  ⦙ ` .الصور + الرد على الشخص`  **✐ : يجلب لك جميع صور الشخص و يمكن وضع رقم صوره بجانب الامر ❝** 
    ⑷  ⦙ ` .زاجل + معرف الشخص + الرساله` **✐ : يرسل الرساله الى الشخص المحدد بالمعرف ❝** 
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸ ⦙`.فيديو`**✐  : يرسل اليك فيديوهات عشوائية**
    ⑹ ⦙ `.فيديو2`**✐  :  يرسل اليك فيديوهات عشوائية اخرى**
    ⑺ ⦙ `.فايروس`**✐  :  يرسل فايروس الى المجموعه او الدردشه ويقوم بتعليقها**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """)
@iqthon.on(admin_cmd(pattern="اوامر الحساب2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    **🚹  ⦑   اوامر الحساب 2   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙  `.صورته + الرد ع الشخص`**✐ : يجلب صوره الشخص الذي تم رد عليه ❝**
    ⑵  ⦙ `.رابطه + الرد ع الشخص`**✐ :  يجلب لك رابط الشخص الذي تم رد عليه  ❝**
    ⑶  ⦙ `.اسمه + الرد ع الشخص`**✐ : يجلب لك اسم الشخص الذي تم رد عليه ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑷  ⦙  `.نسخ + الرد ع الرساله`**✐ : يرسل الرساله التي تم رد عليها ❝**
    ⑼ ⦙ `.بنك`**✐ : يقيس سرعه استجابه لدى تنصيبك ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑽ ⦙ `.سرعه الانترنيت`**✐ : يجلب لك سرعه الانترنيت لديك ❝**
    ⑾ ⦙ `.الوقت`**✐ : يضهر لك الوقت والتاريخ واليوم ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑿ ⦙  `.وقتي`   **✐ : يضهر لك الوقت والتاريخ بشكل جديد ❝**
    ** ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙  `.الحماية تشغيل`**✐ : يقوم بتشغيل رساله الحمايه في الخاص  ❝**
    ⑵  ⦙ `.الحماية ايقاف`**✐ :  يقوم بتعطيل رساله الحماية الخاص وعد تحذير اي شخص❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑶  ⦙ `.قبول`**✐ : يقوم بقبول الشخص للأرسال اليك بدون حظره ❝**
    ⑷  ⦙  `.رفض`**✐ :  الغاء قبول الشخص من الارسال وتحذيره ايضا❝**
    ⑸  ⦙ `.مرفوض`**✐ :  حظر الشخص من دون تحذير حظر مباشر م الخاص ❝**
    ⑹  ⦙  `.المقبولين`**✐ :  عرض قائمة المقبولين في الحماية ❝**
    ⑺ ⦙   `.جلب الوقتيه + الرد على الصورة`**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑻  ⦙  `.تاك بالكلام + الكلمه + معرف الشخص`**✐:  يسوي تاك للشخص بالرابط جربه وتعرف ❝**
    ⑼  ⦙ `.نسخ + الرد على رساله **✐:  يرسل الرساله التي رديت عليها ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑽ ⦙  `.احسب + المعادله`**✐:  يجمع او يطرح او يقسم او يجذر المعادله الأتية ❝**
    """)
@iqthon.on(admin_cmd(pattern="اوامر الحساب3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑  اوامر الحساب  3     ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙ `.حالتي `**✐  :  لفحص الحظر**
    ⑵  ⦙ `.طقس + اسم المدينه `**✐ : يعطي لك طقس المدينه ** 
    ⑶  ⦙  `.طقوس + اسم المدينه `**✐ : يعطي لك طقس المدينه ل 3 ايام قادمه **
    ⑷  ⦙  `.مدينه الطقس + اسم المدينه `**✐ : لتحديد طقس المدينه تلقائي عند ارسال الأمر **
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙  `.ازاله التوجيه + الرد على رساله`**✐ : يرسل اليك الرساله التي تم رد عليها بدون توجيه**
    ⑹  ⦙ `.كشف + الرد على شخص`**✐ : رد على شخص يفحص حضر مستخدم**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺ ⦙ `.وضع بايو + الرد على البايو`**✐ : يضع الكلمه التي تم رد عليها في البايو الخاص بك**
    ⑻  ⦙ `.وضع اسم + الرد على الاسم`**✐ :  يضع الاسم الذي تم رد عليه في اسمك**
    ⑼  ⦙ `.وضع صوره + الرد على صوره`**✐ :  يضع الصوره التي تم رد عليها في حسابك**
    ⑽ ⦙ `.معرفاتي`** ✐ : يجلب جميع المعرفات المحجوزه  في حسابك **
    ⑾ ⦙  `.تحويل ملكية + معرف الشخص`**✐ : يحول ملكيه القناه او المجموعه الى معرف**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑿ ⦙  `.انتحال + الرد على الشخص`**✐ :  ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك ( المعرف الخاص بك لايتغير ) **
    ⒀ ⦙ `.الغاء الانتحال + الرد على الشخص`**✐ : يقوم بالغاء الانتحال ويرجع معلومات  المذكوره بالسورس **
    ⒁  ⦙ `.ازعاج + الرد على شخص`**✐ :  يقوم بتكرار الرسائل للشخص المحدد من دون توقف اي شي يتكلمه حسابك همين يدزه**
    ⒂ ⦙ `.الغاء الازعاج` شرح :  يوقف جميع الازعاجات في المجموعه 
    ⒃  ⦙ `.المزعجهم`**✐ : يضهر اليك جميع الاشخاص الي بل مجموعه مفعل عليهم ازعاج وتكرر رسايلهم**
    """)
@iqthon.on(admin_cmd(pattern="اوامر السورس(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑    اوامر السورس  ⦒  :
    **⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ 
    ⑴ ⦙ `.السورس` **✐  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝**
    ⑶ ⦙ `.حساب كيثاب + اسم الحساب` **✐  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝** 
    ⑸ ⦙ `.المده` **✐  : يضهر لك مدة تشغيل بوت سورس سيمو لديك ❝** 
    ⑹ ⦙ `.فارات تنصيبي` **✐  : يجلب لك جميع الفارات التي لديك وجميع معلومات تنصيبك في هيروكو ❝** 
    ⑼ ⦙  `.تحديث` **✐ :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع سورس سيمو  ❝**
    ⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`**✐ : يقوم بأطفاء سورس سيمو بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل سورس  سيمو ❝**
    ⑾ ⦙  `.الاوامر` **✐ :   لأضهار جميع اوامر السورس اونلاين❝**
    ⑿ ⦙  `.اوامري` **✐ :   لأضهار جميع اوامر السورس كتابه بدون اونلاين❝**
    ⒀ ⦙  `.استخدامي` **✐ :   يضهر لك كمية استخدامك لسورس سيمو❝**
    ⒁ ⦙  `.تاريخ التنصيب` **✐ :   يضهر لك تاريخ تنصيبك❝**
    """   ) 
@iqthon.on(admin_cmd(pattern="اوامر الملصقات(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    **🚹  ⦑    اوامر الملصقات  ⦒  :
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴ ⦙ `.جلب الملصقات + الرد على الملصق`**✐  : يجلب اليك ملصقات الحزمه**
    ⑵ ⦙  `.انشاء حزمه ملصقات + الرد على الملصق`**✐  : يضع الملصق بحزمه بشكل مقصوص**
    ⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )**✐  : يجلب لك جميع معلومات الملصق**
    ⑷ ⦙ `.ملصق + اسم الحزمه او الملصق`**✐  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك**
    """)
@iqthon.on(admin_cmd(pattern="اوامر الاعلانات(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑   اوامر الاعلانات   ⦒  :
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙ `.مؤقته + الوقت بالثواني + رساله`**✐ :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده**
    ⑵  ⦙ `.للكروبات + الرد على الرساله`**✐ :  يرسل الرسالها الى جميع المجموعات**
    ⑶  ⦙ `.مؤقت + عدد ثواني + عدد الرسائل + كليشة` **✐ :  يقوم بارسال رساله وقتيه محدده لكل وقت معين وعدد مرات معين**
    ⑷  ⦙ `.اضافه + رابط الكروب`✐ :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
    يجب ان تتاكد انو مامحضور حسابك ارسل  ⬅️ ( `.حالتي` )
    """)
@iqthon.on(admin_cmd(pattern="اوامر الوقتي(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,""" 
    🚹  ⦑   اوامر الوقتي   ⦒  :
    ⑴ ⦙ `.اسم وقتي`**✐ : يضع الوقت المزخرف في اسمك تلقائيا ❝**
    ⑵ ⦙  `.نبذه وقتيه`**✐ : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا ❝**
    ⑶⦙ `.صوره وقتيه`**✐ : يضع لك الوقت لمزخرف في صورتك تغير تلقائي ❝**
    ⑷⦙ `.ايقاف + الامر الوقتي`**✐ :  ...الامر الوقتي يعني حط بداله الامر الي ستعملته (اسم وقتي)&(بايو وقتي) ❝**""")
@iqthon.on(admin_cmd(pattern="اوامر التسليه1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑    1الاوامر المتحركه للتسلية   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    `.غبي`                                                       
    `.تفجير`
    `.طوبه`
    `.مربعات`
    `.حلويات`
    `.نار`
    `.هلكوبتر`
    `.اشكال مربع`
    `.دائره`
    `.قلب `
    `.مزاج`
    `.قرد`
    `.ايد`
    `.العد التنازلي`
    `.الوان قلوب`
    `.عين`
    `.ثعبان`
    `.رجل`
    `.رموز شيطانيه`
    `.قطار`
    `.موسيقى`
    `.رسم`
    `.فراشه`
    `.مكعبات`
    `.مطر`
    `.تحركات`
    `.ايموجيات`
    `.طائره`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰**""")
@iqthon.on(admin_cmd(pattern="اوامر التسليه2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,"""
    **🚹  ⦑    2الاوامر المتحركه للتسلية   ⦒  :
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    `.شرطي`
    `.النضام الشمسي`
    `.افكر`
    `.اضحك`
    `.ضايج`
    `.ساعه متحركه`
    `.بوسه`
    `.قلوب`
    `.رياضه`
    `.الارض`
    `.قمر`
    `.اقمار`
    `.قمور`
    `.زرفه`
    `.بيبي`
    `.تفاعلات`
    `.اخذ قلبي`
    `.اشوفج السطح`
    `.احبك`
    `.اركض`
    `.روميو`
    `.البنك`
    `.تهكير + الرد على شخص`
    `.طياره`
    `.مصاصه`
    `.مصه`
    `.جكه`
    `.اركضلي`
    `.حمامه`
    `.فواكه`
    `.الحياة`
    `.هلو`
    `.مربعاتي`
    `.اسعاف`
    `.سمايلي`
    """)
@iqthon.on(admin_cmd(pattern="اوامر الفارات(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
    **🚹  ⦑  اوامـر الـفـارات  ⦒ :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴ ⦙ `.اضف فار + اسم افار + القيمه`
    **✐ :  يضيف اليك الفار الخاص بسورس ❝**
    ⑵ ⦙ `.حذف فار + اسم الفار`
    **✐ :  يحذف الفار الذي اضفته ❝**
    ⑶  ⦙ `.جلب فار + اسم الفار`
    **✐ :  يرسل اليك معلومات الفار وقيمه الفار ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :**
    `.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`
    **⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : **
    `.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`
    **⑶  ⦙ لأضـافة فار الايمـوجي  : **
    `.اضف فار ALIVE_EMOJI + الايموجي`
    **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : **
    `.اضف فار ALIVE_TEXT + النص`
    **⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**
    `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`
    **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : **
    `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`
    **✐ : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :**
    `.تليجراف ميديا + الرد على صورة او فيديو`
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    **⑺ ⦙  لتغير كليشة الفحص كاملة :**`.اضف فار ALIVE_TELETHONIQ + كليشه مع المتغيرات`
    **✐ : متغيرات كليشه الفحص  :**
    1 -  :  `{uptime}` :  مده التشغيل بوتك 
    2 -  :  `{my_mention}`  : رابط حسابك  
    3 -  :  `{TM}`  : الوقت 
    4 -  :  `{ping} ` : البنك 
    5 -  : ` {telever} ` : نسخه سورس سيمو 
    6 -  :  `{tg_bot}` :  معرف بوتك
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑻ ⦙ `.اضف فار AUTO_PIC + رابط صورة تليجراف`**✐ :  يضيف اليك الفار للصوره الوقتيه ❝**
    ⑼ ⦙ `.اضف فار MAX_FLOOD_IN_PMS + العدد**✐ :  يضيف اليك الفار تغير عدد تحذيرات رساله حمايه الخاص ❝**
    ⑽ ⦙ `.اضف فار DEFAULT_BIO + الجمله`**✐ :  يضيف اليك الفار تغير جمله النبذه الوقتية  ❝**""") 
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"orders")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **☭︙ قـائمـه الاوامـر :
    **
    **☭︙ قنـاه السـورس :** @ADWSL
    **☭︙ المطور 2: @K_8_U**
    **☭︙ المطور : @O_8_F
    """
    buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1G")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب   ⦒  :**"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G1")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑  اوامر الكروب 1     ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.كتم + الرد ع الشخص`**✐ : يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل ❝** 
    ⑵  ⦙ `. الغاء كتم + الرد ع الشخص`**✐ :  يجلب لك جميع معرفات المشرفين في الكروب  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑶  ⦙ `.البوتات`**✐ : يجلب لك جميع معرفات البوتات في الكروب ❝**
    ⑷  ⦙ `.الأعضاء`**✐ : اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  ❝** 
    ⑸  ⦙ `.معلومات`**✐ : سيرسل لك جميع معلومات الكروب بالتفصيل ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑹ ⦙ `.مسح المحظورين`**✐ : يمسح جميع المحظورين في الكروب ❝** 
    ⑺ ⦙ `.المحذوفين`**✐ : يجلب لك جميع الحسابات المحذوفه ❝**
    ⑻ ⦙ `.المحذوفين تنظيف`**✐ : يمسح جميع الحسابات المحذوفه في الكروب ❝** 
    ⑼ ⦙ `.احصائيات الاعضاء`**✐ : يمسح جميع المحظورين في الكروب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑽ ⦙ `.انتحال + الرد ع الشخص`**✐ : يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف ❝**
    ⑾ ⦙ `.الغاء الانتحال + الرد ع الشخص`**✐ : يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ """
    buttons = [[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="تحميل الملف(?: |$)(.*)"))    
async def install(event):
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(await event.get_reply_message(), "userbot/plugins/")
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_delete(event, f"**☭︙   تم تثبيـت الملـف بنجـاح ✓** `{os.path.basename(downloaded_file_name)}`", 10)
            else:
                os.remove(downloaded_file_name)
                await edit_delete(event, "**☭︙  حـدث خطـأ، هـذا الملف مثبـت بالفعـل !**", 10)
        except Exception as e:
            await edit_delete(event, f"**☭︙  خطـأ ⚠️:**\n`{str(e)}`", 10)
            os.remove(downloaded_file_name)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G2")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑   اوامر الكروب 2   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑴  ⦙  `.ترحيب + الرساله` **✐ : يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  ❝**
    ⑵  ⦙   `.مسح الترحيبات` **✐ :  ييقوم بمسح الترحيب من الكروب ❝**
    ⑶  `.ترحيباتي` **✐ :  يضهر لك جميع الترحيبات التي وضعتها في الكروب ❝**
    ⑷  ⦙ `.رساله الترحيب السابقه تشغيل`  **✐ :  عندما يحدث تكرار سيحذف رساله الترحيب ❝**
    ⑸  ⦙  `.رساله الترحيب السابقه ايقاف`**✐ :  عندما يحدث تكرار لا يحذف رساله الترحيب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑹ ⦙  `.اضف رد + الكلمه` **✐ :  مثلاً تدز رساله هلو تسوي عليها رد بهلوات ❝**
    ⑺ ⦙ `.مسح رد + الكلمه` **✐ :  سيحذف الكلمه الي انت ضفتها ❝**
    ⑻ ⦙  `.جميع الردود` **✐ :  يجلب لك جميع الردود الذي قمت بأضافتها  ❝**
    ⑼ ⦙  `.مسح جميع الردود` **✐ :  يمسح جميع الردود الي انت ضفتها ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑽ ⦙  `.صنع مجموعه + اسم المجموعه`**✐ : يقوم بعمل مجموعه خارقه ❝**
    ⑾ ⦙  `.صنع قناه +  اسم القناة`**✐ : يقوم بعمل قناه خاصه  ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑿ ⦙ `.عدد رسائلي`**✐ : سيظهر لك عدد رسائلك في الكروب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ """
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G3")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑   اوامر الكروب 3   ⦒  :
    **⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰  
    ⑴  ⦙  `.تفعيل حمايه المجموعه`**✐ : يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل❝**
    ⑵  ⦙ `تعطيل حمايه المجموعه`**✐ :  يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده❝**
    ⑶  ⦙ `.صلاحيات المجموعه`**✐ : يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑷  ⦙  `.رفع مشرف + الرد على شخص`**✐ : يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ `.منع + كلمة`**✐ : منع كلمه من الارسال في الكروب**❝
    ⑹ ⦙ `.الغاء منع + كلمه`**✐ : يقوم بالغاء منع الكلمه ❝** 
    ⑺ ⦙ `.قائمه المنع`**✐ : يقوم بجلب جميع الكلمات الممنوعه في الكروب ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑻ ⦙ ` .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️`
    ( 10 - 50 - 100 - 200  )**✐ : يجلب لك الاعضاء بالروابط بالعدد المحدد ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑼ ⦙ `.معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️`
    ( 10 - 50 - 100 - 200  )**✐ :جلب لك معرفات الاعضاء بالعدد المحدد ❝**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    """
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="مسح الملف(?: |$)(.*)"))    
async def unload(event):
    shortname = event.pattern_match.group(1)
    path = Path(f"userbot/plugins/{shortname}.py")
    if not os.path.exists(path):
        return await edit_delete(event, f"**☭︙   ملـف مـع مسـار ⚠️ {path} لإلغـاء التثبيـت ⊠**")
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"**☭︙   {shortname} تم إلغـاء التثبيـت بنجـاح ✓**")
    except Exception as e:
        await edit_or_reply(event, f"**☭︙  تمـت الإزالـة بنجـاح ✓ : {shortname}\n{str(e)}**")
@iqthon.on(admin_cmd(pattern="هاش ([\s\S]*)"))    
async def gethash(hash_q):
    hashtxt_ = "".join(hash_q.text.split(maxsplit=1)[1:])
    with open("hashdis.txt", "w+") as hashtxt:
        hashtxt.write(hashtxt_)
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = f"**Text : **\
            \n`{hashtxt_}`\
            \n**MD5 : **`\
            \n`{md5}`\
            \n**SHA1 : **`\
            \n`{sha1}`\
            \n**SHA256 : **`\
            \n`{sha256}`\
            \n**SHA512 : **`\
            \n`{sha512[:-1]}`\
         "
    await edit_or_reply(hash_q, ans)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G4")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑  اوامر الكروب 4     ⦒  :**
        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑴  ⦙ `.تنظيف الوسائط` ✐: ينضف جميع ميديا من صور وفديوهات و متحركات** او ( `.تنظيف الوسائط + العدد`) ** 
    ⑵  ⦙ `.حذف الرسائل`**✐ :  يحذف جميع الرسائل بلكروب ** ` او  `.حذف الرسائل + العدد 
    ⑶  ⦙ `.مسح + الرد على رسالة`**✐ :  يحذف الرساله الي راد عليها فقط **
    ⑷  ⦙ `.غادر + بلكروب دزها`**✐ :  يغادر من المجموعه او من القناة**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑸  ⦙ ` .تفليش`**✐ :  يطرد جميع الي بلكروب الامر صار احسن ومتطور واسرع**
    ⑹  ⦙ `.اضافه + رابط الكروب `**✐ :  يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك ( يجب ان تتاكد انو مامحضور حسابك ارسل ⬅️( .فحص الحظر ) علمود تتاكد حسابك محظور او لا) 
    ⑺  ⦙ `.جلب الوقتيه + الرد على الصورة`**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰
    ⑻  ⦙ `.تاك بالكلام + الكلمه + معرف الشخص`**✐ :  يسوي تاك للشخص بالرابط جربه وتعرف**
    ⑼  ⦙ `.نسخ + الرد على رساله`**✐ :  يرسل الرساله التي رديت عليها **
    ⑽  ⦙ `.ابلاغ الادمنيه`**✐ :  يسوي تاك لجميع الادمنيه ارسله هذا الامر بلمجموعه في حاله اكو تفليش او مشكلة**
    ⑾  ⦙ `.المشرفين` **✐ : يجيب الك جميع المشرفين في المجموعه او القناه**
    ⑿  ⦙ `.البوتات` **✐ :  يجيب الك جميع بوتات في المجموعه او قناه
   **"""
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G5")))
@check_owner
async def inlineiqthon(iqthon):
    text = """
    **🚹  ⦑  اوامر الكروب 5     ⦒  :**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑴  ⦙ `.تحذير التكرار + عدد رسائل`**✐ :  اي شخص بلكروب يكرر رسائل مالته بلعدد المحدد يقيدة مهما كان رتبته**
    ⑵  ⦙ ` .تحذير تكرار 99999 `✐ :  هذا الامر ستعمله من تريد تلغي التحذير لان مستحيل احد يكرر هل عدد ف اعتبار ينل(غي التحذير**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑶  ⦙ ` .حظر + الرد على شخص`✐ : حظر الشخص من المجموعه او الكروب**
    ⑷  ⦙ ` .الغاء الحظر + الرد على شخص`✐ :  يلغي حظر الشخص من المجموعه او الكروب**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⑺  ⦙ ` .تنزيل مشرف + الرد على شخص`✐ :  يقوم بازاله الشخص من الاشراف **
    ⑻  ⦙ ` .تثبيت + الرد على رساله`✐ : شرح : تثبيت الرساله التي رديت عليها**
    ⒀⦙ `.الأعضاء`**✐ :  اضهار قائمة الاعضاء للمجموعة اذا هواي يرسلك ملف كامل لمعلوماتهم**
    ⒁  ⦙ `.تفليش `**✐ :  يقوم بأزاله جميع اعضاء المجموعه او القناة الى 0**
    ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰ 
    ⒂  ⦙ `.مسح المحظورين**✐ :  يمسح جميع المحظورين في المجموعه او القناه **
    ⒃  ⦙ `.المحذوفين`**✐:  يجلب لك جميع الحسابات المحذوفه في المجموعه او القناه**
    ⒄  ⦙ `.المحذوفين تنظيف`**✐ :  مسح جميع الحسابات المحذوفه في المجموعه او القناة**
    ⒅  ⦙ `.احصائيات الاعضاء`**✐ :  يرسل اليك جميع معلومات اعضاء المجموعه منها عدد الحسابات المحذوفه او الحسابات النشطه او الحسابات اخر ضهور وجميعهم**
    ⒆  ⦙ `.عدد رسائلي`**✐ : يقوم بحساب عدد رسائلك في المجموعه او القناة**
    ⒇  ⦙ `.جلب الاحداث`**✐ :  يرسل اليك اخر 20 رساله محذوفه في المجموعة من الاحداث**
    """
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="هاش(ين|دي) ([\s\S]*)"))    
async def endecrypt(event):
    string = "".join(event.text.split(maxsplit=2)[2:])
    catevent = event
    if event.pattern_match.group(1) == "ين":
        if string:
            result = base64.b64encode(bytes(string, "utf-8")).decode("utf-8")
            result = f"**Shhh! It's Encoded : **\n`{result}`"
        else:
            reply = await event.get_reply_message()
            if not reply:
                return await edit_delete(event, "`What should i encode`")
            mediatype = media_type(reply)
            if mediatype is None:
                result = base64.b64encode(bytes(reply.text, "utf-8")).decode("utf-8")
                result = f"**Shhh! It's Encoded : **\n`{result}`"
            else:
                catevent = await edit_or_reply(event, "`Encoding ...`")
                c_time = time.time()
                downloaded_file_name = await event.client.download_media(                    reply,                    Config.TMP_DOWNLOAD_DIRECTORY,                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(                        progress(d, t, catevent, c_time, "trying to download")                    ),                )
                catevent = await edit_or_reply(event, "`Encoding ...`")
                with open(downloaded_file_name, "rb") as image_file:
                    result = base64.b64encode(image_file.read()).decode("utf-8")
                os.remove(downloaded_file_name)
        await edit_or_reply(            catevent, result, file_name="encodedfile.txt", caption="It's Encoded"        )
    else:
        try:
            lething = str(                base64.b64decode(                    bytes(event.pattern_match.group(2), "utf-8"), validate=True                )            )[2:]
            await edit_or_reply(event, "**Decoded text :**\n`" + lething[:-1] + "`")
        except Exception as e:
            await edit_delete(event, f"**Error:**\n__{str(e)}__")
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الكروب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الكروب", data="ord1G"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الكروب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الكروب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("(الاوامر|الأوامر)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]
            result = builder.article(title="iqthon",text=help2,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="(الاوامر|الأوامر)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "(الاوامر|الأوامر)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الحساب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الحساب", data="ord1hs"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الحساب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الحساب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الالعاب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الالعاب", data="ord1pl"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الالعاب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الالعاب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الصيغ(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الصيغ", data="ordsag1"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@iqthon.on(admin_cmd(pattern="اوامر البصمات1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 1   ⦒  :**\n\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص1`)   ⦙   ابو  عباس  لو  تاكل  خره\n(`.ص2`)   ⦙   استمر  نحن  معك\n(`.ص3`)   ⦙   افحط  بوجه\n(`.ص4`)   ⦙   اكعد  لا  اسطرك  سطره  العباس\n(`.ص5`)   ⦙   اللهم  لا  شماته\n(`.ص6`)   ⦙   امرع  دينه\n(`.ص7`)   ⦙   امشي  بربوك\n(`.ص8`)   ⦙   انت  اسكت  انت  اسكت\n(`.ص9`)   ⦙   انت  سايق  زربه\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص10`)   ⦙   اوني  تشان\n(`.ص11`)   ⦙   برافو  عليك  استادي \n(`.ص12`)   ⦙   بلوك  محترم\n(`.ص13`)   ⦙   بووم  في  منتصف  الجبهة \n(`.ص14`)   ⦙   بيتش \n(`.ص15`)   ⦙   تخوني  ؟\n(`.ص16`)   ⦙   تره  متكدرلي\n(`.ص17`)   ⦙   تعبان  اوي\n(`.ص18`)   ⦙   تكذب\n(`.ص19`)   ⦙   حسبي  الله\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص20`)   ⦙   حشاش \n(`.ص21`)   ⦙   حقير  \n(`.ص22`)   ⦙   خاص  \n(`.ص23`)   ⦙   خاله  ما  تنامون  \n(`.ص24`)   ⦙   خرب  شرفي  اذا  ابقى  بالعراق \n(`.ص25`)   ⦙   دكات  الوكت  الاغبر  \n(`.ص26`)   ⦙   ررردح  \n(`.ص27`)   ⦙   سلامن  عليكم  \n(`.ص28`)   ⦙   بوم منتصف جبهه   \n(`.ص29`)   ⦙   شكد  شفت  ناس  مدودة\n                                                       ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰")
@iqthon.on(admin_cmd(pattern="اوامرالبصمات2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 2   ⦒  :**\n\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص30`)   ⦙  شلون  ، \n(`.ص31`)   ⦙  صح  لنوم  \n(`.ص32`)   ⦙  صمت  \n(`.ص33`)   ⦙  ضحكة  مصطفى  الحجي  \n(`.ص34`)   ⦙  طماطه  \n(`.ص35`)   ⦙  طيح  الله  حضك  \n(`.ص36`)   ⦙  فاك  يوو  \n(`.ص37`)   ⦙  اني فرحان وعمامي فرحانين\n(`.ص38`)   ⦙  لا  تضل  تضرط  \n(`.ص39`)   ⦙  لا  تقتل  المتعه  يا  مسلم  \n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص40`)   ⦙  لا  مستحيل  \n(`.ص41`)   ⦙  لا  والله  شو  عصبي  \n(`.ص42`)   ⦙  لش  \n(`.ص43`)   ⦙  لك  اني  شعليه  \n(`.ص44`)   ⦙  ما  اشرب  \n(`.ص45`)   ⦙  مع  الاسف  \n(`.ص46`)   ⦙  مقتدى  \n(`.ص47`)   ⦙  من  رخصتكم  \n(`.ص48`)   ⦙  منو  انت  \n(`.ص49`)   ⦙  منورني  \n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص50`)  ⦙  نتلاكه  بالدور  الثاني \n(`.ص51`)  ⦙  نستودعكم  الله  \n(`.ص52`)  ⦙  ها  شنهي  \n(`.ص53`)  ⦙  ههاي  الافكار  حطها ب\n(`.ص54`)  ⦙  ليش شنو سببها ليش\n(`.ص55`)  ⦙  يموتون  جهالي\n(`.ص56`)  ⦙  اريد انام\n(`.ص57`)  ⦙  افتحك فتح\n(`.ص58`)  ⦙  اكل خره لدوخني\n(`.ص59`)  ⦙  السيد شنهو السيد\n                                                       ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص60`)  ⦙  زيج2\n(`.ص61`)  ⦙  زيج لهارون\n(`.ص62`)  ⦙  زيج الناصرية\n(`.ص63`)  ⦙  راقبو اطفالكم\n(`.ص64`)  ⦙  راح اموتن\n(`.ص65`)  ⦙  ذس اس مضرطة\n(`.ص66`)  ⦙  دروح سرسح منا\n(`.ص67`)  ⦙  خويه ما دكوم بيه\n(`.ص68`)  ⦙  خلصت تمسلت ديلة كافي انجب\n(`.ص69`)  ⦙  بعدك تخاف\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰")
@iqthon.on(admin_cmd(pattern="اوامر البصمات3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 3   ⦒  :**\n\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص70`)  ⦙  بسبوس\n(`.ص71`)  ⦙  اني بتيتة كحبة\n(`.ص72`)  ⦙  انعل ابوكم لابو اليلعب وياكم طوبة\n(`.ص73`)  ⦙  انت شدخلك\n(`.ص74`)  ⦙  انا ماشي بطلع\n(`.ص75`)  ⦙  امداك وامده الخلفتك\n(`.ص76`)  ⦙  امبيههههه\n(`.ص77`)  ⦙  هدي بيبي\n(`.ص78`)  ⦙  هاه صدك تحجي\n(`.ص79`)  ⦙  مو كتلك رجعني\n                                                       ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص80`)  ⦙  مامرجية منك هاية\n(`.ص81`)  ⦙  ليش هيجي\n(`.ص82`)  ⦙  كـــافـي\n(`.ص83`)  ⦙  كس اخت السيد\n(`.ص84`)  ⦙  شنو كواد ولك اني هنا\n(`.ص85`)  ⦙  شجلبت\n(`.ص86`)  ⦙  شبيك وجه الدبس\n(`.ص87`)  ⦙  سييييي\n(`.ص88`)  ⦙  زيجج1\n(`.ص89`)  ⦙  يموتون جهالي\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n(`.ص90`)  ⦙  ياخي اسكت اسكت\n(`.ص91`)  ⦙  وينهم\n(`.ص92`)  ⦙  هيلو سامر وحود\n(`.ص93`)  ⦙  هو\n(`.ص94`)  ⦙  ههاي الافكار حطها\n                                                        ⊱━━━━━━━━⊰✾⊱━━━━━━━━⊰\n")
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الصيغ(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الصيغ(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.on(admin_cmd(pattern="فتح همسه(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**عزيزي كل عقلك ؟  **\n**وين اكو شي اسمه فتح همسة عرض العالم ماتخاف علية ادبسزز ولي يلة 🙂💔**")
