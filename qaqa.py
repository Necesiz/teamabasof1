import os
import logging
from pytube import YouTube
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram bot tokenini buraya girin
TOKEN = '6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM'

# Botunuz için günlük kaydı etkinleştirme
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start komutunu işleyen fonksiyon
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! YouTube veya YouTube Shorts linkini gönderin.")

# Mesajları işleyen fonksiyon
def handle_message(update, context):
    chat_id = update.effective_chat.id
    message_text = update.message.text

    # Gelen mesajı YouTube veya YouTube Shorts linki olarak kontrol edin
    if 'youtube.com/watch' in message_text or 'youtu.be' in message_text or 'youtube.com/shorts' in message_text:
        try:
            # YouTube videosunu indirme işlemini gerçekleştirin
            video = YouTube(message_text)
            stream = video.streams.get_highest_resolution()
            file_path = stream.download()

            # İndirilen videoyu gönderin
            context.bot.send_video(chat_id=chat_id, video=open(file_path, 'rb'))

            # İndirilen videoyu silin
            os.remove(file_path)
        except Exception as e:
            context.bot.send_message(chat_id=chat_id, text="Video indirme hatası: {}".format(str(e)))
    else:
        context.bot.send_message(chat_id=chat_id, text="Geçersiz YouTube veya YouTube Shorts linki.")

# Telegram botunu başlatma işlemi
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
