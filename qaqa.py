import os
import youtube_dl
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# indirilecek video için fonksiyonlar
def download_video(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
        ydl.download([url])
        return video_title + '.mp3'

# Telegram botu için fonksiyonlar
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba, ben müzik botu. İstediğin şarkının YouTube linkini gönder!")
    
def handle_message(update, context):
    message_text = update.message.text
    chat_id = update.message.chat_id
    if "https://www.youtube.com/" in message_text:
        mp3_file = download_video(message_text)
        context.bot.send_audio(chat_id=chat_id, audio=open(mp3_file, 'rb'), title=mp3_file)
        os.remove(mp3_file)
    else:
        context.bot.send_message(chat_id=chat_id, text="Lütfen sadece YouTube linki gönderin!")

def main():
    updater = Updater(token="6290317562:AAHQq06eN1EHUYqVbUWR0k1eSHSCY4AZo-8", use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    updater.start_polling()

if name == 'main':
    main()