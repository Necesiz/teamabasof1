from pyrogram import Client, filters
import requests

api_id = 21369475
api_hash = 'f85b4b4fa485f981df381692768be912'
bot_token = '6127439543:AAEfCkQds7VMMiXOvrPJV0-9vAlJPgLYBGI'

app = Client('my_userbot', api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.private)
def find_ip(client, message):
    if message.text.startswith('/ip'):
        target_user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
        ip_info = requests.get('https://ipinfo.io/json').json()
        ip_address = ip_info['ip']
        response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
        ip_data = f"IP Address: {response['query']}\nCity: {response['city']}\nRegion: {response['regionName']}\nCountry: {response['country']}\nISP: {response['isp']}"
        client.send_message(target_user.id, ip_data)

app.run()
