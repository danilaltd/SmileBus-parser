import os

TOKEN = os.getenv("TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")

ID_CITY_FROM = int(os.getenv("ID_CITY_FROM", "-1"))
ID_CITY_TO = int(os.getenv("ID_CITY_TO", "-1"))

raw_dates = os.getenv("DATES", "01.01.1970, 02.01.1970")
DATES = [date.strip() for date in raw_dates.split(",") if date.strip()]
