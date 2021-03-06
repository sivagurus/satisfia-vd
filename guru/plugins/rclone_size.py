#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52

import subprocess
import os
import asyncio

from guru import (
    EDIT_SLEEP_TIME_OUT,
    DESTINATION_FOLDER,
    RCLONE_CONFIG
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def check_size_g(client, message):
    #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    try:
        del_it = await message.reply_text("🔊 Checking size...wait!!!")
        if not os.path.exists('rclone.conf'):
            #subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
            with open('rclone.conf', 'a', newline="\n", encoding = 'utf-8') as fole:
                fole.write("[DRIVE]\n")
                fole.write(f"{RCLONE_CONFIG}")
        destination = f'{DESTINATION_FOLDER}'
        cmd = ['rclone', 'size', '--config=./rclone.conf', 'DRIVE:'f'{destination}']
        gau_tam = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        gau, tam = await gau_tam.communicate()
        print(gau)
        print(tam)
        print(tam.decode("utf-8"))
        gautam = gau.decode("utf-8")
        print(gautam)
        await asyncio.sleep(5)
        await message.reply_text(f"🔊CloudInfo:\n\n{gautam}")
        await del_it.delete()
    except Exception as g_e:
        LOGGER.info(g_e)

#gautamajay52

async def g_clearme(client, message):
    try:
        inline_keyboard = []
        ikeyboard = []
        ikeyboard.append(InlineKeyboardButton("Yes 🚫", callback_data=("fuckingdo").encode("UTF-8")))
        ikeyboard.append(InlineKeyboardButton("No 🤗", callback_data=("fuckoff").encode("UTF-8")))
        inline_keyboard.append(ikeyboard)
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await message.reply_text("Are you sure? 🚫 This will delete all your downloads locally 🚫", reply_markup=reply_markup, quote=True)
    except Exception as g_e:
        LOGGER.info(g_e)
