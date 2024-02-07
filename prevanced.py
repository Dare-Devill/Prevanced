import requests
import webbrowser
from colorama import Fore, Style
from pyfiglet import figlet_format

# Function to fetch the latest release from GitHub
def fetch_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release_info = response.json()
        return release_info
    else:
        print(f"{Fore.RED}Failed to fetch the latest release information.{Style.RESET_ALL}")
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

# Function to handle the download of an asset
def download_asset(url):
    webbrowser.open(url)

# Replace 'owner' and 'repo' with your actual GitHub repository details
owner = 'Dare-Devill'
repo = 'Revanced-apps'

# Fetch the latest release
release_info = fetch_latest_release(owner, repo)

# Display ASCII art with the name of the repository
ascii_art = figlet_format(f" Prathxm's {repo} Releases", font="standard")
print(f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}")

# Display the release information
display_release_info(release_info)

# Prompt the user to select an asset to download
if release_info and release_info['assets']:
    try:
        selection = int(input(f"{Fore.YELLOW}Enter the number of the asset you want to download (or 0 to cancel): {Style.RESET_ALL}"))
        if 1 <= selection <= len(release_info['assets']):
            # User selected a valid asset
            selected_asset = release_info['assets'][selection - 1]
            print(f"{Fore.GREEN}Downloading {selected_asset['name']}...{Style.RESET_ALL}")
            download_asset(selected_asset['browser_download_url'])
        elif selection == 0:
            print(f"{Fore.RED}Download cancelled.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid selection. Download cancelled.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}No assets available to download.{Style.RESET_ALL}")
