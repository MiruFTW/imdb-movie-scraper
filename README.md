# IMDb Movie Scraper

This is a simple web scraper that fetches movie titles and ratings from IMDb's box office and popular movies charts. The project utilizes Selenium for web scraping and Tkinter for a basic GUI interface.

## Features

- Scrapes the top 10 movies from IMDb's box office or popular movies list.
- Displays the movie titles and ratings in a user-friendly format.
- Offers a simple graphical interface to choose between box office and popular movies.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- GeckoDriver for Firefox

### GeckoDriver

You need to have GeckoDriver installed on your system. You can download it from [the official GeckoDriver releases](https://github.com/mozilla/geckodriver/releases) and place it in a directory of your choice.

## Installation

1. Clone this repository:
    git clone https://github.com/miruftw/imdb-movie-scraper.git

2. Navigate to the project directory:
    cd imdb-movie-scraper

3. Install the required packages:
    pip install -r requirements.txt

## Usage

To run the scraper, execute the following command:
python imdb_gui.py

This will launch a Tkinter window where you can select either "Box Office Top 10" or "Popular Movies" to scrape.

## Acknowledgments
Selenium for web scraping.
Beautiful Soup for HTML parsing.
Tkinter for the GUI interface.

## License
This project is licensed under the MIT License
