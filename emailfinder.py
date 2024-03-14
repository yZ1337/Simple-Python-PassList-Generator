import requests
from bs4 import BeautifulSoup
import re
import datetime
from colorama import Fore, Back, Style

def save_emails_to_file(emails, file_name):
    with open(file_name, 'w') as file:
        file.write(emails + '\n')

def find_emails(url):
    try:
        print(f"Scanning for emails... \n")
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the parsed HTML
        text = soup.get_text()

        # Regular expression pattern for finding emails
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        filename = f'found_emails_{datetime.datetime.now().strftime("%Y-%m-%d")}.txt'
        count = 0
        for email in emails:
            print(
                f"{Fore.LIGHTGREEN_EX}[+]{Style.RESET_ALL} {Fore.YELLOW}{email}{Style.RESET_ALL}")
            filename = f'found_emails_{datetime.datetime.now().strftime("%Y-%m-%d")}.txt'
            with open(filename, 'w') as file:
                file.write(email + '\n')
            count += 1
        print(
            f"\n{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}{count}{Style.RESET_ALL} found on the website.")
        print(
            f"{Fore.LIGHTGREEN_EX}[SUCCESS]{Style.RESET_ALL} File saved to: {Fore.LIGHTBLUE_EX}{filename}{Style.RESET_ALL}")
        return set(emails)  # Return a set of unique email addresses


    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return set()
