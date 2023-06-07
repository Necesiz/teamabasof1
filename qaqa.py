import telebot
import youtube_dl
import os

BOT_TOKEN = '6290317562:AAHQq06eN1EHUYqVbUWR0k1eSHSCY4AZo-8'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba, ben müzik botuyum. Müzik aramak için /search komutunu kullanabilirsiniz.")

@bot.message_handler(commands=['search'])
def search_music(message):
    msg = bot.send_message(message.chat.id, "Lütfen bir müzik adı ya da sanatçı ismi giriniz.")
    bot.register_next_step_handler(msg, download_music)

def download_music(message):
    query = message.text
    ydl_opts = {'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio',
                     'preferredcodec': 'mp3',
                     'preferredquality': '320'}
                ]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{query}", download=False)['entries']
        if len(search_results) == 0:
            bot.send_message(message.chat.id, "Aradığınız müzik bulunamadı!")
            return
        music_id = search_results[0]['id']
        music_title = search_results[0]['title']
        ydl.download([f"https://www.youtube.com/watch?v={music_id}"])
        music_file = f"{music_title}.mp3"
        bot.send_audio(message.chat.id, audio=open(music_file, 'rb'), title=music_title)
        os.remove(music_file)

bot.polling()