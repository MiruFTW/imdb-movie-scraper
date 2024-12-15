# IMDb Movie Scraper

The **IMDb Movie Scraper** is a Python project that uses Selenium and BeautifulSoup to scrape movie data from IMDb. It allows users to choose between fetching information about "Box Office Top 10" movies or "Popular Movies." The scraper retrieves titles, ratings, and additional metadata for popular movies. The project also includes a PyQt5-based GUI for a user-friendly experience.

---

## Features

- **Scrape Box Office Top 10:** Retrieves the top 10 movies currently at the box office, including titles and ratings.
- **Scrape Popular Movies:** Fetches a list of popular movies along with:
  - Title
  - Rating
  - Release year
  - Runtime
  - Age rating (e.g., PG-13, R)
- **Headless Browser Support:** Uses Selenium in headless mode for faster and UI-less scraping.
- **Interactive GUI:** Provides an intuitive interface for users to scrape and view IMDb data.
- **Clickable Movie Links:** Embedded hyperlinks to directly access movie IMDb page.

---

## Prerequisites

- Python 3.9+
- Google Chrome browser
- The following Python libraries:
  - `selenium`
  - `beautifulsoup4`
  - `webdriver_manager`
  - `re`
  - `pyqt5`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/miruftw/imdb-movie-scraper.git
   cd imdb-movie-scraper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Google Chrome is installed on your system.

---

## Usage

### Running the GUI Application

1. Launch the GUI:
   ```bash
   python movie_scraper.py
   ```

2. Use the dropdown menu to select "Box Office Top 10" or "Popular Movies."

3. Click the "Scrape IMDb" button to fetch and display the data in a sortable table.

---

## Output Format

- **Box Office Top 10:**
  A list of tuples where each tuple contains:
  - Title
  - Rating

  Example:
  ```
  [
      ('The Marvels', '8.5'),
      ('Killers of the Flower Moon', '8.4'),
      ...
  ]
  ```

- **Popular Movies:**
  A list of tuples where each tuple contains:
  - Title
  - Rating
  - Release Year
  - Runtime
  - Age Rating

  Example:
  ```
  [
      ('Dune: Part Two', '8.7', '2024', '2h 35m', 'PG-13'),
      ('Oppenheimer', '9.1', '2023', '3h 0m', 'R'),
      ...
  ]
  ```

---

## File Structure

- **imdb_scraper.py:** Contains the main scraping logic.
- **movie_scraper.py:** Provides a graphical interface for the scraper.
- **requirements.txt:** Lists the Python dependencies required for the project.

---

## Known Issues

- IMDb frequently updates its page structure, which might break the scraper.
- In case of missing ratings or metadata, "No rating" or `None` is returned.
- **Headless Mode Parsing Issue:** Running the scraper in headless mode with `options.add_argument("--headless=new")` might lead to incomplete parsing. If no results are returned, try simulating non-headless behavior with the following workaround:
  - Use `options.add_argument("--disable-blink-features=AutomationControlled")`.
  - Run without headless mode to verify page content loading.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

---

## Acknowledgments

- IMDb for providing movie data.
- Selenium and BeautifulSoup for making web scraping seamless.
- PyQt5 for enabling the development of a user-friendly GUI.

