import Utilities
import telebot

from config import CHAT_ID, DATES, ID_CITY_FROM, ID_CITY_TO, TOKEN

bot = telebot.TeleBot(TOKEN)

BaseUrl = f"https://smilebus.by/api/v2/route/schedule-detail?id_city_from={ID_CITY_FROM}&id_city_to={ID_CITY_TO}&date="

def send_notification(message):
	bot.send_message(CHAT_ID, message)


if __name__ == "__main__":
    send_notification("Started")
    Utilities.monitor_file_changes(DATES, BaseUrl)