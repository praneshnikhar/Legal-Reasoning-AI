from bs4 import BeautifulSoup
import requests
import json
import os
import time

def scrape_section(url, title):
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(separator='\n')

        # Save the section as a JSON file
        os.makedirs("data", exist_ok=True)
        filename = title.replace(" ", "_").replace(":", "").replace("/", "").lower() + ".json"
        
        with open(os.path.join("data", filename), "w") as f:
            json.dump({
                "title": title,
                "text": text.strip()
            }, f, indent=2)

        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Failed to scrape {title}: {e}")

def bulk_scrape(case_list):
    for i, (url, title) in enumerate(case_list):
        print(f"\n📄 [{i+1}/{len(case_list)}] Scraping: {title}")
        scrape_section(url, title)
        time.sleep(2)  # Be kind to Indian Kanoon

# Example usage
if __name__ == "__main__":
    case_list = [
        ("https://indiankanoon.org/doc/1030211/", "Section 73 - Compensation for loss or damage caused by breach of contract"),
        ("https://indiankanoon.org/doc/78902411/", "Ram Chandra Sharma & Ors vs State Of Bihar (2010)"),
        ("https://indiankanoon.org/doc/1348301/", "Kartar Singh vs State of Punjab"),
        ("https://indiankanoon.org/doc/1483639/", "D.K. Basu vs State of West Bengal")
        # 🔁 Add more here
    ]

    bulk_scrape(case_list)
