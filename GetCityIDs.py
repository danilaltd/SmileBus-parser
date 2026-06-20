import requests
from bs4 import BeautifulSoup
import json 

CITY_DEPARTURE = 2 # search in https://smilebus.by/api/v2/route/cities-departure

def read_file_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            return str(soup)
  
    except Exception as e:
        pass

def analyze_string(input_string):
    try:
        cities = json.loads(input_string)
        stops = cities['data']
        for stop in stops:
            print(stop["id_city"], stop["city_name"])

    except Exception as e:
        pass


str2 = read_file_content(f"https://smilebus.by/api/v2/route/cities-arrival?city_from_id={CITY_DEPARTURE}").encode('utf-8').decode('unicode_escape')
analyze_string(str2)