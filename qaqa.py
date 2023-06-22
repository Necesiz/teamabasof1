import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Pyrogram istemciyi oluşturma
api_id = 21369475
api_hash = 'f85b4b4fa485f981df381692768be912'
bot_token = '6029692550:AAHMrKAcxP1uAODvm0WFb1e2tsqYSs-YX0g'

app = Client('shazam_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
import shazamio

# Telegram API anahtarlarınızı buraya girin


# Botunuzun çalışması için komutlar
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Merhaba! Şarkıyı tanımak için lütfen ses kaydedin.")

@app.on_message(filters.voice)
def recognize_song(client, message):
    # Ses kaydını alın
    voice_message = message.voice
    file_id = voice_message.file_id

    # Ses dosyasını indirin
    file_path = client.download_media(file_id)

    # ShazamIO kütüphanesini kullanarak şarkıyı tanıyın
    recognizer = shazamio.Shazam(file_path)
    song = recognizer.recognize_song()

    # Tanınan şarkıyı yanıt olarak gönderin
    if song:
        artist = song["track"]["subtitle"]
        title = song["track"]["title"]
        reply_text = f"Bu şarkı {artist} tarafından {title} adlı şarkıdır."
    else:
        reply_text = "Şarkı tanınamadı."

    # Yanıtı gönderin
    try:
        message.reply_text(reply_text)
    except MessageNotModified:
        pass

# Botunuzu çalıştırın
app.run()
