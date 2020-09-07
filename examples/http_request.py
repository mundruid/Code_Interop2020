import requests
import json


def get_json(url):
    path = "/json"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    result = requests.get(url=f"{url}{path}", headers=headers)

    return result


if __name__ == "__main__":
    print(get_json("https://httpbin.org"))
