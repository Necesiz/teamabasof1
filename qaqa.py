import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Pyrogram istemciyi oluşturma
api_id = 21369475
api_hash = 'f85b4b4fa485f981df381692768be912'
bot_token = '6029692550:AAHMrKAcxP1uAODvm0WFb1e2tsqYSs-YX0g'

app = Client('shazam_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# "/start" komutuna yanıt veren bir işlev
@app.on_message(filters.command('start'))
def start_command(client: Client, message: Message):
    client.send_message(message.chat.id, 'Merhaba! Şarkı adını öğrenmek için bana bir ses kaydedin.')

# Ses kaydedildiğinde çalışacak işlev
@app.on_message(filters.voice)
def recognize_song(client: Client, message: Message):
    # Ses dosyasını indirme
    file = client.download_media(message.voice)

    # Shazam API'sini kullanarak şarkıyı tanıma
    song_title = recognize_song_with_shazam(file)

    # Tanınan şarkıyı gönderme
    client.send_message(message.chat.id, f"Bu şarkı: {song_title}")

    # İndirilen ses dosyasını silme
    os.remove(file)

# Shazam API'sini kullanarak şarkıyı tanıma işlevi
def recognize_song_with_shazam(file_path):
    # Burada Shazam API'siyle ilgili işlemleri gerçekleştirin
    # Ses dosyasını Shazam API'sine gönderip şarkıyı tanıyın
    # Tanınan şarkının adını döndürün
    return "Tanınan Şarkı"

# Pyrogram istemcisini başlatma
app.run()
