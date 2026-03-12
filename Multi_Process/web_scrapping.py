import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

url=['https://en.wikipedia.org/wiki/Young_Head_coinage',
'https://en.wikipedia.org/wiki/Five_pounds_(gold_coin)',
'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=28',
'https://chatgpt.com/c/69b25763-ea94-8322-aab0-66341ecfb9c1',
'https://en.wikipedia.org/wiki/World_War_II']



def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"Fetched {len(soup.text)} characters from {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
with ThreadPoolExecutor(max_workers=len(url)) as executor:
    executor.map(fetch_content, url)
print("All content fetched successfully")   