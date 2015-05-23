from bs4 import BeautifulSoup
import requests

url = 'http://www.randomfunfacts.com'

def get_fun_facts():
    req = requests.get(url)
    soup = BeautifulSoup(req.text)
    fun = soup.find("i")
    for fact in fun:
        print fact

get_fun_facts()
