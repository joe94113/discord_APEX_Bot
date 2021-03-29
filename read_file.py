import json


def read_setting():
    with open("setting.json", "r", encoding="utf8") as f:
        data = json.load(f)
        return data


def read_url():
    with open("url.json", "r", encoding="utf8") as f:
        urls = json.load(f)
        return urls