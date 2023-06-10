import telebot

TOKEN = "6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM"  # Telegram Bot Tokenınızı buraya ekleyin

bot = telebot.TeleBot(TOKEN)
blocklist = []  # Blocklist için boş bir liste oluşturuyoruz

@bot.message_handler(func=lambda message: True)
def check_message(message):
    user_id = message.from_user.id
    text = message.text.lower()

    if text in blocklist:
        if user_id not in blocklist[user_id]:
            blocklist[user_id] = 1
            bot.send_message(user_id, "Blocklistteki bir sözü 3 defa kullandığınız için uyarıldınız.")
        else:
            blocklist[user_id] += 1
            if blocklist[user_id] >= 3:
                bot.send_message(user_id, "Blocklistteki bir sözü 3 defa kullandığınız için banlandınız.")
                bot.kick_chat_member(message.chat.id, user_id)
    else:
        # Buraya blocklistede olmayan bir sözün işlenmesiyle ilgili kodlarınızı ekleyebilirsiniz.
        pass

@bot.message_handler(commands=['add_to_blocklist'])
def add_to_blocklist(message):
    words = message.text.split()[1:]
    blocklist.extend(words)
    bot.reply_to(message, "Blockliste sözler eklendi.")

@bot.message_handler(commands=['remove_from_blocklist'])
def remove_from_blocklist(message):
    words = message.text.split()[1:]
    for word in words:
        if word in blocklist:
            blocklist.remove(word)
    bot.reply_to(message, "Blocklistten sözler kaldırıldı.")

bot.polling()
