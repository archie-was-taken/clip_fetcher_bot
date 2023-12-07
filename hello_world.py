# Standard library modules
import asyncio
import subprocess
import os
import time

# Third-party modules
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.constants import ParseMode

with open('api_key.txt') as api_key:
    api_key = api_key.read()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.message.from_user.first_name

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Hello, {first_name}! This bot can download videos from all'
        ' popular sites like YouTube, Instagram, Reddit, TikTok etc. To learn'
        ' how to use the bot, type /help.',
        reply_to_message_id=update.message.message_id
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('help.txt') as help_text:
        help_text = help_text.read()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=help_text,
        parse_mode=ParseMode.HTML,
        reply_to_message_id=update.message.message_id,
    )



async def url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = context.args[0]

    output = subprocess.getoutput(
        f'yt-dlp --no-warnings -f best/bestvideo+bestaudio --get-url {url}')
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Click <a href="{output}">here</a> to download the video.',
        parse_mode=ParseMode.HTML,
        reply_to_message_id=update.message.message_id,)

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    url = context.args[0]
    chat_id = update.effective_chat.id
    timestamp = int(time.time())
    file_path = f'test/video_{chat_id}_{timestamp}.mp4'

    subprocess.call(
        ['yt-dlp', '--format', 'bestvideo+bestaudio/best', 
        '--merge-output-format', 'mp4', '--concurrent-fragments', '4', 
        '--no-playlist', f'{url}', '-o',f'{file_path}']
        )
    
    temp_message = await context.bot.send_message(
        chat_id=chat_id,
        text='Downloading video and sending. Please wait.',
        reply_to_message_id=update.message.message_id)
    
    # subprocess.call(['ffmpeg', '-i', file_path, '-vf', 'scale=1:360', 
    #                compressed_file_path])
    
    with open(file_path, 'rb+') as video:
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=video,
            reply_to_message_id=update.message.message_id,
            write_timeout=300,
        )
    await context.bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=temp_message.message_id,
    )

    if os.path.isfile(file_path):
        os.remove(file_path)
    



if __name__ == '__main__':
    application = ApplicationBuilder().token(api_key).build()

    application.add_handler(
        CommandHandler('start', start)
    )
    application.add_handler(
        CommandHandler('url', url)
    )
    application.add_handler(
        CommandHandler('download', download)
    )
    application.add_handler(
        CommandHandler('dl', download)
    )
    application.add_handler(
        CommandHandler('help', help)
    )

    application.run_polling()

