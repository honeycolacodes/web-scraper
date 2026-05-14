# 🌐 Web Scraper

A Python script that scrapes data from websites and saves it to a CSV file.

## What it does
- Loops through multiple pages automatically
- Extracts text, authors, and tags from each entry
- Saves everything to a clean CSV file
- Stops automatically when there are no more pages

## How to use
1. Clone this repo
2. Install dependencies:
   pip install requests beautifulsoup4
3. Open `scraper.py` and change the `url` and `output_file` variables
4. Run: `python scraper.py`

## Example output
```
Scraped page 1...
Scraped page 2...
Scraped page 3...
Done! Scraped 100 quotes.
Saved to: quotes.csv
```

## Tech used
- Python 3
- `requests` — fetches web pages
- `BeautifulSoup` — parses HTML
- `csv` — saves the data
