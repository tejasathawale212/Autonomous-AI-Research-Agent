import requests
from bs4 import BeautifulSoup


def extract_webpage(url: str) -> str:
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(["script", "style", "nav", "footer"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text[:12000]