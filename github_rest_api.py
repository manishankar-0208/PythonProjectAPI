"""
CP1404/CP5632 Assignment
This program fetches data from the GitHub REST API including:
- User profile details
- List of user repositories
- Search results for a given keyword
Author: ManiShakar Reddy Ramapuram
Started 15/11/2025
"""

import requests

BASE_USER_URL = "https://api.github.com/users/"
BASE_SEARCH_URL = "https://api.github.com/search/repositories?q="


def main():
    """Main program function."""
    print("GitHub API Demonstration")
    username = get_valid_username()
    user_data = fetch_user_profile(username)
    if user_data is None:
        print("User not found.")
        return
    display_user_profile(user_data)

    # Fetch User Repositories
    repo_list = fetch_user_repos(username)
    if repo_list is None:
        print("Could not find any repositories for this user.")
        return
    display_user_repos(repo_list)

    # Search for repositories based on a keyword, e.g., "python" or "game"
    keyword = get_valid_keyword()
    search_data = search_repositories(keyword)
    if search_data is None:
        print("Could not find related repositories! Try again with a different keyword.")
        return
    display_search_results(search_data,keyword)


def get_valid_username():
    """Prompt user for a valid GitHub username."""
    username = input("Enter a GitHub username: ").strip()
    while username == "":
        print("Username cannot be empty!")
        username = input("Enter a GitHub username: ").strip()
    return username


def get_valid_keyword():
    """Prompt user for a valid search keyword."""
    keyword = input("Enter a search keyword: ").strip()
    while keyword == "":
        print("Keyword cannot be empty!")
        keyword = input("Enter a search keyword: ").strip()
    return keyword


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
    return None


def search_repositories(keyword):
    """Search GitHub repositories by keyword."""
    response = requests.get(BASE_SEARCH_URL + keyword)
    if response.status_code == 200:
        return response.json()
    return None


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
    """Print list of repositories and selected fields."""
    print("\n--- First 5 Repositories ---")
    for i, repo in enumerate(repo_list[:5], 1):
        print(f"\n{i}. Repository: {repo.get('name')}")
        print(f"Language: {repo.get('language')}")
        print(f"Stars: {repo.get('stargazers_count')}")
        print(f"URL: {repo.get('html_url')}")


def display_search_results(search_data,keyword):
    """Print first 5 search results."""
    print("\n--- Search Results (Top 5) ---")
    print(f"\n--- First 5 repositories related to '{keyword}' ---")
    items = search_data.get("items", [])
    for i, repo in enumerate(items[:5], 1):
        print(f"\n{i} Repository: {repo.get('full_name')}")
        print(f"Stars: {repo.get('stargazers_count')}")
        print(f"Language: {repo.get('language')}")
        print(f"URL: {repo.get('html_url')}")


if __name__ == "__main__":
    main()
