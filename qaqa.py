import telebot
from pytube import YouTube

# Telegram botunuzun API anahtarını buraya ekleyin
API_KEY = '6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if text.startswith('https://www.youtube.com/') or text.startswith('https://youtu.be/'):
        try:
            yt = YouTube(text)
            video = yt.streams.get_highest_resolution()
            video.download()
            bot.send_message(message.chat.id, 'Video indirildi.')
        except Exception as e:
            bot.send_message(message.chat.id, 'Video indirilirken bir hata oluştu.')
            print(str(e))

bot.polling()
