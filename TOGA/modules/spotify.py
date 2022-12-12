from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import typing
from TOGA.helpers.spthelper import SpotifyClient, get_spotify_data
import TOGA.helpers.strings as st


def authorize(update, user_id):
    msg = update.effective_message
    user = update.effective_user
    spotify = SpotifyClient()
    if spotify.is_oauth_ready:
        url = spotify.auth_uri(state=user_id)
        msg.reply_text(
            st.SPT_LOGIN.format(user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Authorize", url=url)]]
            ),
        )

    else:
        msg.reply_text("Something went wrong! Please report")

@typing
def now_playing(update, context):
    user = update.effective_user
    chat = update.effective_chat
    msg = update.effective_message

    spt = get_spotify_data(user.id)
    if not spt:
        if chat.type == "private":
            return authorize(update, user.id)
        return msg.reply_text(st.SPT_LOGIN_PM)

    text = ""
    music = spt.current_music
    if music:
        text = f"<b>{user.first_name} is currently listening to</b>"
    else:
        music = spt.last_music
        text = f"<b>{user.first_name} was listening to</b>"

    text += f"\n<a href='{music.url}'>{music.name}</a> by <b>{music.artist}</b>"
    msg.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Open in spotify", url=music.url)]]
        ),
    )


dp.add_handler(CommandHandler("nowplaying", now_playing))
