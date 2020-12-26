#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

# the logging things
import logging
import os
import shutil
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

from pyrogram.types import CallbackQuery
from guru.helper_funcs.admin_check import AdminCheck
from guru.helper_funcs.youtube_dl_button import youtube_dl_call_back
from guru import (
    MAX_MESSAGE_LENGTH,
    AUTH_CHANNEL
)
async def button(bot, update: CallbackQuery):
    cb_data = update.data
    LOGGER.info(cb_data)
    try:
        g = await AdminCheck(bot, update.message.chat.id, update.from_user.id)
        LOGGER.info(g)
    except Exception as ee:
        LOGGER.info(ee)
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    LOGGER.info(update.from_user.id)
    LOGGER.info(update.message.reply_to_message.from_user.id)
    if cb_data == "fuckingdo":
        if update.from_user.id in AUTH_CHANNEL:
            g_d_list = ['app.json', 'venv', 'rclone.conf', '.gitignore', '_config.yml', 'COPYING', 'Dockerfile', 'DOWNLOADS', 'Procfile', '.heroku', '.profile.d', 'rclone.jpg', 'README.md', 'requirements.txt', 'runtime.txt', 'start.sh', 'guru', 'gautam', 'Torrentleech-Gdrive.txt', 'vendor']
            LOGGER.info(g_d_list)
            g_list = os.listdir()
            LOGGER.info(g_list)
            g_del_list = list(set(g_list)-set(g_d_list))
            LOGGER.info(g_del_list)
            if len(g_del_list) != 0:
                for f in g_del_list:
                    if os.path.isfile(f):
                        os.remove(f)
                    else:
                        shutil.rmtree(f)
                await update.message.edit_text(f"Deleted {len(g_del_list)} objects 😬")
            else:
                await update.message.edit_text("Nothing to clear 🙄")
        else:
            await update.message.edit_text("You are not allowed to do that 🤭")
    elif cb_data == "fuckoff":
        await update.message.edit_text("Okay! fine 🤬")
                
