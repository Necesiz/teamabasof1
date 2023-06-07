python
import requests
import telegram
from telegram.ext import Updater, CommandHandler

# Telegram bot token
TOKEN = "6290317562:AAHQq06eN1EHUYqVbUWR0k1eSHSCY4AZo-8"

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Bana bir şehir adı söyleyin, size hava durumunu söyleyeyim.")

# Function to handle the weather command
def weather(update, context):
    # Get the city name from the user input
    city_name = " ".join(context.args)

    # Generate the URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=your_api_key&lang=tr&units=metric"

    # Request the weather information from the API
    response = requests.get(url)

    # Parse the JSON response
    weather_data = response.json()

    # Extract the weather information
    city = weather_data["name"]
    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]

    # Compose the response message
    message = f"Hava durumu: {city}\nDurum: {description}\nSıcaklık: {temp:.1f} °C\nHissedilen sıcaklık: {feels_like:.1f} °C\nNem: {humidity}%"

    # Send the response message to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Setup the Telegram bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the command handlers
start_handler = CommandHandler("start", start)
weather_handler = CommandHandler("weather", weather)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)

# Start the bot
updater.start_polling()