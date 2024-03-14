import subprocess
import sys
import argparse
from passlistgen import *
from emailfinder import *

try:
    from colorama import Fore, Back, Style
except ImportError:
    print("colorama is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Back, Style

try:
    import requests
except ImportError:
    print("requests is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("bs4 is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])
    from bs4 import BeautifulSoup

def is_website_link(s):
    # Regular expression pattern for matching a URL
    pattern = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    return bool(re.match(pattern, s))

def main():
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}#############################")
    print(f"{Fore.LIGHTMAGENTA_EX}#      {Style.RESET_ALL}Created by: \033[4myZ\033[0m       {Style.DIM}{Fore.LIGHTMAGENTA_EX}#")
    print(f"{Fore.LIGHTMAGENTA_EX}#############################{Style.RESET_ALL}\n")
    parser = argparse.ArgumentParser(description=f'Modify words in a file by appending characters and save output.')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist file')
    parser.add_argument('-a', '--add', type=str, help='Characters to use, comma separated')
    parser.add_argument('-o', '--output', type=str, help='File to save the modified words')
    parser.add_argument('-fe', '--findemails', type=str, help='Find emails on a website by URL and outputs it to a file.')

    args = parser.parse_args()

    if args.wordlist:
        characters = None
        if args.add:
            characters = args.add.replace(' ', '').split(',')

        modified_words = modify_words(args.wordlist, characters)
        if args.output:
            with open(args.output, 'w') as file:
                count = 0
                for word in modified_words:
                    file.write(word + '\n')
                    count += 1
            print(f"{Fore.BLUE}[INFO] {Style.RESET_ALL}Words generated: {count}")
            print(f"{Fore.LIGHTGREEN_EX}[SUCCESS] {Style.RESET_ALL}Output saved to: {args.output}")
        else:
            for word in modified_words:
                print(word)
    if args.findemails:
        if is_website_link(args.findemails):
            find_emails(args.findemails)
        else:
            print(f"{Fore.RED}[ERROR] Given URL is not a URL{Style.RESET_ALL}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
