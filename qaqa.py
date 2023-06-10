import telebot

# Telegram botunuzun token'ını buraya girin
TOKEN = '6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM'

# Blocklist
blocklist = []

# Telegram botunuzu oluşturun
bot = telebot.TeleBot(TOKEN)

# Kullanıcıları ve mesajları saklamak için bir sözlük oluşturun
user_warnings = {}

# Kullanıcıları ve engellemeleri saklamak için bir sözlük oluşturun
user_bans = {}

# Botunuzun başlangıç komutu
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Blocklist botuna hoş geldiniz!")

# Blocklist'e sözcük ekleme komutu
@bot.message_handler(commands=['add'])
def add_to_blocklist(message):
    words = message.text.split()[1:]
    blocklist.extend(words)
    bot.reply_to(message, "Blocklist'e sözcükler eklendi.")

# Blocklist'ten sözcük silme komutu
@bot.message_handler(commands=['remove'])
def remove_from_blocklist(message):
    words = message.text.split()[1:]
    for word in words:
        if word in blocklist:
            blocklist.remove(word)
    bot.reply_to(message, "Blocklist'ten sözcükler silindi.")

# Mesaj kontrolü
@bot.message_handler(func=lambda message: True)
def check_message(message):
    user_id = message.from_user.id
    user_warnings.setdefault(user_id, 0)
    user_bans.setdefault(user_id, 0)
    for word in blocklist:
        if word in message.text.lower():
            user_warnings[user_id] += 1
            bot.reply_to(message, "Blocklistteki bir kelime kullandığınız için uyarıldınız. "
                                  "Toplam uyarı sayınız: {}".format(user_warnings[user_id]))
            if user_warnings[user_id] >= 3:
                bot.reply_to(message, "3. kez uyarıldığınız için engellendiniz.")
                bot.kick_chat_member(message.chat.id, user_id)
                user_bans[user_id] += 1
                user_warnings[user_id] = 0
            break

# Botu çalıştırın
bot.polling()
