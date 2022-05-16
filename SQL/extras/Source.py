import re
import time
from datetime import datetime
from userbot import StartTime, iqthon
from userbot.Config import Config
from userbot.plugins import mention
help1 = ("**☭⦙ كيفيه التنصيب :**")
help2 = ("**☭⦙ قـائمـه الاوامـر :**\n**☭⦙ قنـاه السـورس :** @ADWSL** ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"""
**.𓄌 : version 1  𓇡.
**.𓄌 : me  {mention}  𓇡. 
**.𓄌 : time  {TM}  𓇡.**
**.𓄌 : My Bot {TG_BOT} 𓇡.**
**.𓄌 : Source : @ADWSL  𓇡.**"""
