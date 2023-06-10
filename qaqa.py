import telebot

# Telegram Bot Tokenini buraya ekleyin
TOKEN = '6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM'

# Telebot nesnesini oluşturun
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.chat.type == 'supergroup' and message.new_chat_members)
def on_chat_join_request(message):
    for user in message.new_chat_members:
        # Kullanıcının grup isteğini kabul etmek için bir işlem yapabilirsiniz
        # Örneğin, kullanıcıya hoş geldin mesajı gönderebiliriz
        bot.send_message(user.id, 'Gruba hoş geldiniz!')

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def on_private_message(message):
    # Kullanıcının özel mesajına istediğiniz mesajı gönderebilirsiniz
    bot.send_message(message.chat.id, 'Özel mesajınıza gönderilen bir mesaj!')

# Botu çalıştırın
bot.polling()
