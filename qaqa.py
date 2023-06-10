import telebot

bot = telebot.TeleBot("6112298959:AAFsCNm4qJ-r9o6GHZswao7cq3wpL9a9ruM")  # Botunuzun tokenını buraya yerleştirin

blocklist = []  # Blocklist için boş bir liste

@bot.message_handler(func=lambda message: True)
def check_message(message):
    user_id = message.from_user.id
    text = message.text.lower()
    
    for word in blocklist:
        if word in text:
            if user_id not in blocklist:
                blocklist.append(user_id)
                bot.reply_to(message, "Blocklistteki bir kelimeyi kullandığınız için uyarıldınız.")
                break
            elif blocklist.count(user_id) < 3:
                blocklist.append(user_id)
                bot.reply_to(message, "Blocklistteki bir kelimeyi tekrar kullandığınız için uyarıldınız. Bu 3. uyarınız, bir sonraki uyarıda banlanacaksınız.")
                break
            else:
                bot.kick_chat_member(message.chat.id, user_id)
                bot.reply_to(message, "Blocklistteki bir kelimeyi 3 kez kullandığınız için banlandınız.")
                break

@bot.message_handler(commands=['add'])
def add_word_to_blocklist(message):
    word = message.text.split('/add ', 1)[1].lower()
    if word not in blocklist:
        blocklist.append(word)
        bot.reply_to(message, f"{word} blockliste eklendi.")
    else:
        bot.reply_to(message, f"{word} zaten blocklistte yer alıyor.")

@bot.message_handler(commands=['remove'])
def remove_word_from_blocklist(message):
    word = message.text.split('/remove ', 1)[1].lower()
    if word in blocklist:
        blocklist.remove(word)
        bot.reply_to(message, f"{word} blocklistten kaldırıldı.")
    else:
        bot.reply_to(message, f"{word} blocklistte bulunamadı.")

bot.polling()
