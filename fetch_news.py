import requests
import datetime

# Function to fetch news from your news summary service
def fetch_news():
    url = https://github.com/blbenton/daily-news-brief.git  # Replace with the actual API or scraping source
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch news."

# Save news to a file
def save_news():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    news_content = fetch_news()
    
    with open(f"news_summary_{today}.txt", "w", encoding="utf-8") as file:
        file.write(news_content)
    
    print("News summary saved successfully.")

# Run the script
if __name__ == "__main__":
    save_news()

