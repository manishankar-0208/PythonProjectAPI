"""
CP1404/CP5632 Assignment
This program fetches a summary of any topic using the Wikipedia REST API.
Author: ManiShakar Reddy Ramapuram
Started 14/11/2025
"""
import requests

BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def main():
    """Main function."""
    print("Wikipedia API Demonstration")
    topic = get_valid_topic()
    data = fetch_summary(topic)
    if data is None:
        print("Topic not found. Please check the spelling or try a different topic.")
        return
    display_summary(data)

def get_valid_topic():
    """Get a valid topic from the user"""
    topic = input("Enter a Wikipedia topic: ").strip()
    while not topic:
        print("Topic cannot be empty.")
        topic = input("Enter a Wikipedia topic: ").strip()
    return topic

def fetch_summary(topic):
    """Fetch the summary of a topic from Wikipedia."""
    formatted_topic = topic.replace(" ", "_")
    url = BASE_URL + formatted_topic

    headers = {"User-Agent": "WikipediaSummaryAPIDemo"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()

    if "extract" in data and data["extract"]:
        return data
    return None

def display_summary(data):
    """Display the summary of a topic."""
    print("\n--- Wikipedia Summary ---")
    print(f"Title: {data.get('title')}")
    print(f"Description: {data.get('description')}")
    print(f"Summary:\n{data.get('extract')}")
    page_url = data.get("content_urls", {}).get("desktop", {}).get("page")
    if page_url:
        print(f"Full Article: {page_url}")

if __name__ == "__main__":
    main()
