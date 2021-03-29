import requests
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    else:
        return None


def get_data(player):
    player = str(player)
    URL = "https://apex.tracker.gg/apex/profile/origin/" + player + "/legends"
    dom = get_web_page(URL)
    soup = BeautifulSoup(dom, "html.parser")
    pict_url = soup.find("div", "legend__portrait").img["src"]
    title = soup.find("div", "legend__name").text
    names = soup.find_all("span", class_="name")  # 8910
    values = soup.find_all("span", class_="value")
    data = {
        "pict_url": pict_url,
        "title": title,
        "name1": names[8].text,
        "name2": names[9].text,
        "name3": names[10].text,
        "value1": values[0].text,
        "value2": values[1].text,
        "value3": values[2].text,
    }
    return data


def get_overview(player):
    player = str(player)
    URL = "https://apex.tracker.gg/apex/profile/origin/" + player + "/overview"
    dom = get_web_page(URL)
    soup = BeautifulSoup(dom, "html.parser")
    url = soup.find("div", "highlighted-stat").img["src"]
    suptext = soup.find("div", "highlight-suptext").text.strip()
    text = soup.find("div", "highlight-text").text.strip()
    data = {
        "url": url,
        "suptext": suptext,
        "text": text
    }
    return data

