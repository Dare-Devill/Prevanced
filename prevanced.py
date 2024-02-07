#!/usr/bin/env python3
# Prevanced - A Python script to check for updates and open the download URL of the latest release from GitHub in the browser
# Author: Prathxm
# Repository: https://github.com/Dare-Devill/Prevanced

import requests
import webbrowser
from colorama import Fore, Style
from pyfiglet import figlet_format

# Current version of the script
VERSION = "1.0.0"
UPDATE_REPO_OWNER = 'Dare-Devill'
UPDATE_REPO_NAME = 'Prevanced'
UPDATE_FILE_NAME = 'update.txt'

# Function to fetch the latest release from GitHub
def fetch_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Failed to fetch the latest release information. Error: {e}{Style.RESET_ALL}")
        return None

# Function to fetch the version from update.txt in the update repository
def fetch_version_from_update_file(owner, repo, file_name):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{file_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Failed to fetch the version from update.txt. Error: {e}{Style.RESET_ALL}")
        return None

# Function to display the release information
def display_release_info(release_info):
    if release_info:
        print(f"{Fore.GREEN}Release Name: {release_info['name']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Release Tag: {release_info['tag_name']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Release Published At: {release_info['published_at']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}\nAssets:{Style.RESET_ALL}")
        for i, asset in enumerate(release_info['assets'], start=1):
            print(f"{Fore.CYAN}{i}. {asset['name']}{Style.RESET_ALL}")
            print(f"    {Fore.MAGENTA}Download URL: {asset['browser_download_url']}{Style.RESET_ALL}")
        print()

# Function to open a URL in the default web browser
def open_url_in_browser(url):
    webbrowser.open(url)

# Main function to run the script
def main():
    # Fetch the version from update.txt in the update repository
    latest_version = fetch_version_from_update_file(UPDATE_REPO_OWNER, UPDATE_REPO_NAME, UPDATE_FILE_NAME)

    # Check if the fetched version is newer than the current version
    if latest_version and latest_version != VERSION:
        update = input(f"{Fore.YELLOW}A new version of Prevanced is available ({latest_version}). Do you want to update? (yes/no): {Style.RESET_ALL}")
        if update.lower() == 'yes':
            # Update logic would go here, but it's not necessary for this task
            pass
        else:
            print(f"{Fore.YELLOW}Continuing with the current version ({VERSION}).{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}You are using the latest version of Prevanced.{Style.RESET_ALL}")

    # Fetch the latest release
    release_info = fetch_latest_release('Dare-Devill', 'Revanced-apps')

    # Display ASCII art with the name of the repository
    ascii_art = figlet_format(f"Revanced-apps Releases", font="standard")
    print(f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}")

    # Display the release information
    display_release_info(release_info)

    # Prompt the user to select an asset to open in the browser
    if release_info and release_info['assets']:
        while True:
            try:
                selection = int(input(f"{Fore.YELLOW}Enter the number of the asset you want to open in the browser (or 0 to cancel): {Style.RESET_ALL}"))
                if selection == 0:
                    print(f"{Fore.RED}Opening in browser cancelled.{Style.RESET_ALL}")
                    break
                elif 1 <= selection <= len(release_info['assets']):
                    # User selected a valid asset
                    selected_asset = release_info['assets'][selection - 1]
                    print(f"{Fore.GREEN}Opening {selected_asset['name']} in the browser...{Style.RESET_ALL}")
                    open_url_in_browser(selected_asset['browser_download_url'])
                    break
                else:
                    print(f"{Fore.RED}Invalid selection. Please try again.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No assets available to open.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
