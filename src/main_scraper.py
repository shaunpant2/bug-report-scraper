import requests
import time
import pandas as pd
from config import LIMIT, FIELDS

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

retry = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry, pool_connections=1, pool_maxsize=1)
session.mount("https://", adapter)
session.mount("http://", adapter)

session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

def scraper_dataset(name, url):
    print(f"Scraping {name}...")

    all_bugs = []
    offset = 0

    while True:
        params = {
            "chfieldfrom": "1998-01-01",
            "chfieldto": "2011-12-31",
            "limit": LIMIT,
            "offset": offset,
            "include_fields": ",".join(FIELDS)
        }

        try:
            response = session.get(
                url,
                params=params,
                timeout=30,
                headers={"Connection": "close"}
            )
            if response.status_code != 200:
                print("Status code 200!")
                time.sleep(60)
                continue
            data = response.json()
        except requests.exceptions.RequestException:
            print(f"Server returned {response.status_code}")
            time.sleep(30)
            continue

        bugs = data.get("bugs",[])

        if not bugs:
            break

        all_bugs.extend(bugs)

        offset +=LIMIT
        time.sleep(5)

    df = pd.DataFrame(all_bugs)
    df.to_csv(f"data/{name}_bugs_before_2012.csv", index=False)