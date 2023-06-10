import telebot
from pytube import YouTube

TOKEN = '6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = "Merhaba! YouTube videolarını veya shorts'ları indirmek için bana bir YouTube linki gönderin."
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        video_url = message.text
        video = YouTube(video_url)
        video_title = video.title

        # İndirme işlemi
        stream = video.streams.get_highest_resolution()
        stream.download(filename='video')

        # İndirilen videoyu gönderme
        with open('video.mp4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        # İndirme tamamlandı mesajı
        download_complete_message = f"{video_title} başarıyla indirildi."
        bot.reply_to(message, download_complete_message)
    except Exception as e:
        error_message = f"Bir hata oluştu: {str(e)}"
        bot.reply_to(message, error_message)

bot.polling()
