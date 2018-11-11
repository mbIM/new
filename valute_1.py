import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

valute_from = "EUR"
valute_to = "USD"
amount = 800


def course(valute_from, valute_to, amount):
    def getCourse(id):
        return xml.find("valute", {'id': id}).value.text

    print(getCourse("R01239"), "рублей на 1 евро")
    print(getCourse("R01235"), "рублей на 1 доллар")

    def getNominal(id):
        return xml.find("valute", {'id': id}).nominal.text

    print(getNominal("R01239"), "- номинал")

    eur = 75.8076
    usd = 66.8497
    nominal = 1

    diffence = eur / usd
    result = amount * diffence / nominal

    print ("800 евро =", (result), "долларов")


print(course(valute_from, valute_to, amount))