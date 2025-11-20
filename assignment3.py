"""
CP1404/CP5632 Assignment 3
This program demonstrates the use of two REST APIs:
1. GitHub REST API
   - Fetch user profile details
   - List user repositories
   - Search repositories by keyword

2. Wikipedia REST API
   - Fetch a summary of any topic

Author: ManiShakar Reddy Ramapuram
Started: 14/11/2025
"""

import requests

# GitHub API Base URLs
BASE_USER_URL = "https://api.github.com/users/"
BASE_SEARCH_URL = "https://api.github.com/search/repositories?q="

# Wikipedia API Base URL
WIKI_BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

MENU = """Menu:
(G)ithub API
(W)ikipedia API
(B)oth APIs
(Q)uit
"""
def main():
    """Main program function that integrates GitHub + Wikipedia API calls."""
    print(MENU)
    choice = input("Enter your choice from the menu: ").strip().upper()
    while choice != "Q":
        if choice == "G":
            run_github_section()
        elif choice == "W":
            run_wikipedia_section()
        elif choice == "B":
            run_github_section()
            run_wikipedia_section()
        else:
            print("Invalid choice. Please choose G, W, B, or Q.")
        print(f"\n{MENU}")
        choice = input("Enter your choice from the menu: ").strip().upper()

def run_github_section():
    """Run GitHub API operations."""
    print("\n--- GitHub API Section ---")
    username = get_valid_input("Enter a GitHub username: ")
    user_data = fetch_user_profile(username)
    if user_data:
        display_user_profile(user_data)
        repo_list = fetch_user_repos(username)
        display_user_repos(repo_list)
    else:
        print("GitHub user not found.")
    keyword = get_valid_input("\nEnter a GitHub repo search keyword: ")
    search_data = search_repositories(keyword)
    display_search_results(search_data, keyword)

def run_wikipedia_section():
    """Run Wikipedia API operations."""
    print("\n--- Wikipedia API Section ---")
    topic = get_valid_input("Enter a Wikipedia topic: ")
    summary_data = fetch_wikipedia_summary(topic)
    if summary_data:
        display_wikipedia_summary(summary_data)
    else:
        print("Topic not found. Please check the spelling or try a different topic.")

def get_valid_input(prompt):
    """Get a valid input from user."""
    user_input = input(prompt).strip()
    while not user_input:
        print("Input cannot be empty!")
        user_input = input(prompt).strip()
    return user_input

def fetch_user_profile(username):
    """Return GitHub user profile data."""
    response = requests.get(BASE_USER_URL + username)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_user_repos(username):
    """Return list of repositories for the given user."""
    response = requests.get(BASE_USER_URL + username + "/repos")
    if response.status_code == 200:
        return response.json()
    return []

def search_repositories(keyword):
    """Search GitHub repositories by keyword."""
    response = requests.get(BASE_SEARCH_URL + keyword)
    if response.status_code == 200:
        return response.json()
    return {"items": []}

def display_user_profile(user_data):
    """Print selected user profile details."""
    print("\n--- GitHub User Profile ---")
    print(f"Name: {user_data.get('name')}")
    print(f"Bio: {user_data.get('bio')}")
    print(f"Followers: {user_data.get('followers')}")
    print(f"Following: {user_data.get('following')}")
    print(f"Public Repos: {user_data.get('public_repos')}")
    print(f"Joined GitHub: {user_data.get('created_at')}")

def display_user_repos(repo_list):
    """Print first 5 repositories."""
    print("\n--- User Repositories ---")
    if not repo_list:
        print("No repositories found.")
        return
    for i, repo in enumerate(repo_list[:5], 1):
        print(f"\n{i}. {repo.get('name')}")
        print(f"Language: {repo.get('language')}")
        print(f"Stars: {repo.get('stargazers_count')}")
        print(f"URL: {repo.get('html_url')}")

def display_search_results(search_data, keyword):
    """Print first 5 search results for a keyword."""
    print(f"\nRepositories related to '{keyword}' Projects")
    items = search_data.get("items", [])
    if not items:
        print("No matching repositories found.")
        return
    for i, repo in enumerate(items[:5], 1):
        print(f"\n{i}. {repo.get('full_name')}")
        print(f"Stars: {repo.get('stargazers_count')}")
        print(f"Language: {repo.get('language')}")
        print(f"URL: {repo.get('html_url')}")

def fetch_wikipedia_summary(topic):
    """Fetch the summary of a topic from Wikipedia."""
    formatted_topic = topic.replace(" ", "_")
    url = WIKI_BASE_URL + formatted_topic
    headers = {"User-Agent": "Assignment3WikipediaAPIDemo"}

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

def display_wikipedia_summary(data):
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