from bs4 import BeautifulSoup
import requests
import re
import pyttsx3
url = "https://globalnews.ca/toronto/weather/CAXX0504"
get = requests.get(url).text
soup = BeautifulSoup(get, "html.parser")
find = soup.find_all("div",attrs={"class":"weather-column weather-new-temp"})
engine = pyttsx3.init()
newVoiceRate = 147
engine.setProperty('rate', newVoiceRate)
for finds in find:
    print(finds.text)
    engine.say(f"The weather is {finds.text}")
    engine.runAndWait()


