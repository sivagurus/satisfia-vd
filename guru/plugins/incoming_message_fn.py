#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | Akshay C

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os
import requests

from guru import (
    DOWNLOAD_LOCATION
)


import time
import asyncio
from guru.helper_funcs.extract_link_from_message import extract_link
from guru.helper_funcs.display_progress import progress_for_pyrogram
from guru.helper_funcs.youtube_dl_extractor import extract_youtube_dl_formats
from guru.helper_funcs.admin_check import AdminCheck
from guru.helper_funcs.ytplaylist import yt_playlist_downg
from guru.helper_funcs.download import download_tg
from guru.helper_funcs.upload_to_tg import upload_to_tg

async def incoming_youtube_dl_f(client, message):
    """ /ytdl command """
    g_id = message.from_user.id
    credit = await message.reply_text(f"💀 Downloading for you <a href='tg://user?id={g_id}'>🤕</a>", parse_mode="html")
    i_m_sefg = await message.reply_text("processing", quote=True)
    # LOGGER.info(message)
    # extract link from message
    dl_url, cf_name, yt_dl_user_name, yt_dl_pass_word = await extract_link(
        message.reply_to_message, "YTDL"
    )
    LOGGER.info(dl_url)
    #if len(message.command) > 1:
        #if message.command[1] == "gdrive":
            #with open('blame_my_knowledge.txt', 'w+') as gg:
                #gg.write("I am noob and don't know what to do that's why I have did this")
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        current_user_id = message.from_user.id
        # create an unique directory
        user_working_dir = os.path.join(DOWNLOAD_LOCATION, str(current_user_id))
        # create download directory, if not exist
        if not os.path.isdir(user_working_dir):
            os.makedirs(user_working_dir)
        # list the formats, and display in button markup formats
        thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
            dl_url,
            cf_name,
            yt_dl_user_name,
            yt_dl_pass_word,
            user_working_dir
        )
        print(thumb_image)
        req = requests.get(f"{thumb_image}")
        gau_tam = f"{current_user_id}.jpg"
        open(gau_tam, 'wb').write(req.content)
        if thumb_image is not None:
            await message.reply_photo(
                #text_message,
                photo=gau_tam,
                quote=True,
                caption=text_message,
                reply_markup=reply_markup
            )
            await i_m_sefg.delete()
        else:
            await i_m_sefg.edit_text(
                text=text_message,
                reply_markup=reply_markup
            )
    else:
        await i_m_sefg.edit_text(
            "**FCUK**! wat have you entered. \nPlease read /help \n"
            f"<b>API Error</b>: {cf_name}"
        )
#playlist
async def g_yt_playlist(client, message):
    """ /pytdl command """
    #i_m_sefg = await message.reply_text("Processing...you should wait🤗", quote=True)
    usr_id = message.from_user.id
    G_DRIVE = False
    if len(message.command) > 1:
        if message.command[1] == "gdrive":
            G_DRIVE = True
    if 'youtube.com/playlist' in message.reply_to_message.text:
        i_m_sefg = await message.reply_text("Downloading...you should wait🤗", quote=True)
        await yt_playlist_downg(message.reply_to_message, i_m_sefg, G_DRIVE)
    
    else:
        await message.reply_text("Reply to youtube playlist link only 🙄")
                
async def rename_tg_file(client, message):
    usr_id = message.from_user.id
    if len(message.command) > 1:
        new_name = '/app/' + message.command[1].strip()
        file = await download_tg(client, message)
        try:
            if file:
                os.rename(file, new_name)
        except Exception as g_g:
            await message.reply_text("g_g")
        response = {}
        final_response = await upload_to_tg(
            message,
            new_name,
            usr_id,
            response
        )
        LOGGER.info(final_response)
        try:
            message_to_send = ""
            for key_f_res_se in final_response:
                local_file_name = key_f_res_se
                message_id = final_response[key_f_res_se]
                channel_id = str(message.chat.id)[4:]
                private_link = f"https://t.me/c/{channel_id}/{message_id}"
                message_to_send += "👉 <a href='"
                message_to_send += private_link
                message_to_send += "'>"
                message_to_send += local_file_name
                message_to_send += "</a>"
                message_to_send += "\n"
            if message_to_send != "":
                mention_req_user = f"<a href='tg://user?id={usr_id}'>Your Requested Files</a>\n\n"
                message_to_send = mention_req_user + message_to_send
                message_to_send = message_to_send + "\n\n" + "#uploads"
            else:
                message_to_send = "<i>FAILED</i> to upload files. 😞😞"
            await message.reply_text(
                text=message_to_send,
                quote=True,
                disable_web_page_preview=True
            )
        except Exception as pe:
            LOGGER.info(pe)

    else:
        await message.reply_text("Provide new name of the file with extension 😐")