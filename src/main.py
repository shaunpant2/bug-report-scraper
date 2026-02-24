from config import URLS
from main_scraper import scraper_dataset

def main():
    for name, url in URLS.items():
        scraper_dataset(name,url)


if __name__ == "__main__":
    main()