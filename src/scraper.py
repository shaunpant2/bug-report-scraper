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
            "creation_time_end" : END_DATE,
            "limit" : LIMIT,
            "offset" : offset,
            "include_fields" : FIELDS
        }

        response = requests.get(url, params=params)
        data = response.json()

        bugs = data.get("bugs",[])

        print(f"Downloaded {len(bugs)} bugs this page")

        if not bugs:
            break

        all_bugs.extend(bugs)

        if len(all_bugs) >= 10:
            all_bugs = all_bugs[:10]
            break

        offset = LIMIT + offset
        time.sleep(WAIT_TIME)

    df = pd.DataFrame(all_bugs)
    # df.to_csv(f"data/{name}_bugs_before_2012.csv", index=False)
    df.to_csv(f"data/{name}_10_bugs.csv", index=False)

    print(f"{name} finished. Saved {len(df)} bugs.")