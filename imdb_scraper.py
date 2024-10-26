# imdb_scraper.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import re

def scrape_imdb(choice):
    
    options = Options()
    options.headless = True
    service = Service(GeckoDriverManager().install())  # Automatically manages GeckoDriver
    driver = webdriver.Firefox(service=service, options=options)

    # Set URL based on user choice
    if choice == "Box Office Top 10":
        url = "https://www.imdb.com/chart/boxoffice/"
    elif choice == "Popular Movies":
        url = "https://www.imdb.com/chart/moviemeter/"

    driver.get(url)

    # Wait for the body of the page to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract movie titles and ratings
    titles = [a.get_text(strip=True) for a in soup.find_all('a', class_='ipc-title-link-wrapper')]
    ratings = []
    data = [div.get_text(strip=True) for div in soup.findChildren('div', class_='cli-title-metadata')]
    year = [None] * len(data)
    runtime = [None] * len(data)
    age_rating = [None] * len(data)

    for i, info in enumerate(data):
        match = re.match(r"(\d{4})\s*((?:\d{1,2}h\s*)?(?:\d{1,2}m)?)\s*([A-Za-z0-9- ]+)?", info)
        if match:
            year[i] = match.group(1)
            runtime[i] = match.group(2)
            age_rating[i] = match.group(3)

    for rating in soup.find_all('div', class_='cli-ratings-container'):
        rating_span = rating.find('span', class_='ipc-rating-star--rating')

        if rating_span:
            ratings.append(rating_span.get_text(strip=True))
        else:
            ratings.append("No rating")

    # Return titles and ratings as a list of tuples
    return [(titles[i], ratings[i], year[i], runtime[i], age_rating[i]) for i in range(min(len(titles), len(ratings)))]
