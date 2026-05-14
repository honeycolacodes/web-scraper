import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes(url, output_file):
    quotes_data = []
    page = 1

    while True:
        # Fetch the page
        response = requests.get(f"{url}/page/{page}/")
        
        # Stop if page doesn't exist
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        
        # Stop if no quotes found
        if not quotes:
            break
        
        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            
            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags)
            })
        
        print(f"Scraped page {page}...")
        page += 1
    
    # Save to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes_data)
    
    print(f"Done! Scraped {len(quotes_data)} quotes.")
    print(f"Saved to: {output_file}")

# Target URL and output file
url = "https://quotes.toscrape.com"
output_file = "quotes.csv"

scrape_quotes(url, output_file)
