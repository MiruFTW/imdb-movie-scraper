# imdb_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

def scrape_imdb(choice):
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    service = Service(ChromeDriverManager().install())  # Automatically manages ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

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
    links = [f"https://www.imdb.com{a['href']}" for a in soup.find_all('a', class_='ipc-title-link-wrapper', href=True)]
    ratings = []
    if (choice == "Popular Movies"):
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
    else:
        titles = [re.sub(r'^\d+\.\s*', '', title) for title in titles]

    for rating in soup.find_all('div', class_='cli-ratings-container'):
        rating_span = rating.find('span', class_='ipc-rating-star--rating')

        if rating_span:
            ratings.append(rating_span.get_text(strip=True))
        else:
            ratings.append("No rating")

    # Return titles and ratings as a list of tuples
    if (choice != "Popular Movies"):
        return [(titles[i], ratings[i], links[i]) for i in range(min(len(titles), len(ratings)))]
    else:
        return [(titles[i], ratings[i], links[i], year[i], runtime[i], age_rating[i]) for i in range(min(len(titles), len(ratings)))]
