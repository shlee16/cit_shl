# https://www.dataquest.io/blog/web-scraping-tutorial-python/

from bs4 import BeautifulSoup
import requests

# page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# page = requests.get("https://www.w3schools.com/python/ref_random_randint.asp")
page = requests.get("https://www.naver.com/")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# print(forecast_items)
