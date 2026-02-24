import requests
import time
import pandas as pd
from config import END_DATE, LIMIT, WAIT_TIME, FIELDS

def scraper_dataset(name, url):
    print(f"Scraping {name}...")

    all_bugs = []
    offset = 0


    while True:
        params = {
            "chfield": "[Bug creation]",
            "chfieldfrom": "1998-01-01",
            "chfieldto": "2011-12-31",
            "limit": LIMIT,
            "offset": offset,
            "include_fields": ",".join(FIELDS)
        }

        response = requests.get(url, params=params)
        print(response)
        data = response.json()
        print(data)
        bugs = data.get("bugs",[])

        if not bugs:
            break

        all_bugs.extend(bugs)

        if len(all_bugs) >= 1000:
            break

        offset +=LIMIT
        time.sleep(WAIT_TIME)

    df = pd.DataFrame(all_bugs)
    df.to_csv(f"data/{name}_bugs_before_2012.csv", index=False)