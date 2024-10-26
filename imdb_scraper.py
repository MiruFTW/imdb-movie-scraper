# imdb_scraper.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

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

    for rating in soup.find_all('div', class_='cli-ratings-container'):
        rating_span = rating.find('span', class_='ipc-rating-star--rating')

        if rating_span:
            ratings.append(rating_span.get_text(strip=True))
        else:
            ratings.append("No rating")

    # Return titles and ratings as a list of tuples
    return [(titles[i], ratings[i]) for i in range(min(len(titles), len(ratings)))]
