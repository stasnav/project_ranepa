import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json


BASE_URL = "https://pedsovet.org/"


def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/127.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text


def parse_cards(html: str):
    soup = BeautifulSoup(html, "html.parser")

    cards = []

    for a in soup.select('a[href^="/article/"]'):
        title = a.get_text(strip=True)
        if not title:
            continue

        href = a.get("href")
        full_url = urljoin(BASE_URL, href)

        cards.append({
            "title": title,
            "url": full_url,
        })

    unique_cards = []
    seen = set()
    for card in cards:
        if card["url"] in seen:
            continue
        seen.add(card["url"])
        unique_cards.append(card)

    return unique_cards


def main():
    html = fetch_html(BASE_URL)

    cards = parse_cards(html)

    print(json.dumps(cards, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()