from pyrogram import Client, filters
import requests

api_id = 21369475
api_hash = 'f85b4b4fa485f981df381692768be912'
bot_token = '6127439543:AAEfCkQds7VMMiXOvrPJV0-9vAlJPgLYBGI'

app = Client('my_userbot', api_id, api_hash, bot_token=bot_token)

# "/start" komutuna cevap verme
@app.on_message(filters.command("start"))
def start(client, message):
    client.send_message(message.chat.id, "Bot aktif!")

# Mesaj filtresi ekleme
@app.on_message(filters.text & ~filters.command("start"))
def add_filter(client, message):
    # Mesajdaki komutu filtre adı olarak kullan
    filter_name = message.text.lower()
    # Filtreyi ekleyin
    app.set_filter(filter_name, message.reply_to_message)
    client.send_message(message.chat.id, f"Yeni filtre eklenmiş: {filter_name}")

# Mevcut filtreleri görüntüleme
@app.on_message(filters.command("filters"))
def show_filters(client, message):
    filters_list = app.list_filters()
    if filters_list:
        filters_text = "\n".join(filters_list)
        client.send_message(message.chat.id, f"Mevcut filtreler:\n{filters_text}")
    else:
        client.send_message(message.chat.id, "Hiçbir filtre bulunamadı.")

# Filtreleri silme
@app.on_message(filters.command("remove_filter"))
def remove_filter(client, message):
    filter_name = message.text.split(maxsplit=1)[1].lower()
    removed = app.remove_filter(filter_name)
    if removed:
        client.send_message(message.chat.id, f"Filtre silindi: {filter_name}")
    else:
        client.send_message(message.chat.id, f"Filtre bulunamadı: {filter_name}")

app.run()
