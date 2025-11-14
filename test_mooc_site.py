import requests
from bs4 import BeautifulSoup

BASE_URL = "https://mooc.enu.kz"


def test_home_page_status():
    resp = requests.get(BASE_URL, timeout=15)
    assert resp.status_code == 200


def test_home_page_title_text():
    resp = requests.get(BASE_URL, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    assert "Eurasian" in text or "Course" in text or "Курс" in text


def test_login_page_status():
    resp = requests.get(BASE_URL + "/login/index.php", timeout=15)
    assert resp.status_code == 200
