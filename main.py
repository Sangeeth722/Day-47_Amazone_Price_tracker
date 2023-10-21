import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv
load_dotenv("C:/Users/sangeeth/PycharmProjects/EnvironmentVariables/.env.txt")

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD =os.getenv("APP_PASSWORD")
URL = "https://www.amazon.in/Gear-Premium-Dri-Fit-Helmet-Skull/dp/B0757LNY3F/ref=sr_1_4?keywords=helmet+cap&s=automotive&sr=1-4"
headers = {
    "User-Agent": "en-US",
    "Accept-Language": "537.36 (KHTML, like Gecko) Chrome",
}
def send_main(message):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="sangeeths431@gmail.com",msg=f"Subject : Amzone Price Alert \n\n {message}")

response = requests.get(URL,headers=headers)
response_text = response.text

sp = BeautifulSoup(response_text,"lxml")
price = sp.find("span", class_="a-price-whole").get_text()
price_int = int(price)

if price_int >95:
    title = sp.find("title").get_text()
    message = f"{title} is now ${price_int}  {URL}".encode("utf-8")
    send_main(message=message)

