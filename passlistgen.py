import argparse
import random
import subprocess
import sys

try:
    from colorama import Fore, Back, Style
except ImportError:
    print("colorama is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Back, Style

def generate_suffixes():
    suffixes = ['01', '01!']
    numbers = '1234567890'
    for i in range(1, 11):
        num_seq = numbers[:i]
        if num_seq not in suffixes:
            suffixes.append(num_seq)

    specials = '!@#$%^&*()'
    for i in range(1, len(specials) + 1):
        special_seq = specials[:i]
        if special_seq not in suffixes:
            suffixes.append(special_seq)

    combined = numbers + specials
    for i in range(1, 11):
        combined_seq = combined[:i]
        if combined_seq not in suffixes:
            suffixes.append(combined_seq)

    random.shuffle(suffixes)
    return suffixes[:100]

def modify_words(file_path, characters=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        word = line.strip()
        if characters:
            # Append each character or character group from the user's list to the word
            for char_group in characters:
                modified_lines.append(f"{word}{char_group}")
        else:
            suffixes = generate_suffixes()
            for suffix in suffixes:
                modified_word = f"{word}{suffix}"
                modified_lines.append(modified_word)

    return modified_lines

def main():
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}#############################")
    print(f"{Fore.LIGHTMAGENTA_EX}#      {Style.RESET_ALL}Created by: \033[4myZ\033[0m       {Style.DIM}{Fore.LIGHTMAGENTA_EX}#")
    print(f"{Fore.LIGHTMAGENTA_EX}#############################{Style.RESET_ALL}\n")
    parser = argparse.ArgumentParser(description=f'{Fore.LIGHTMAGENTA_EX}Modify words in a file by appending characters and save output.')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist file')
    parser.add_argument('-a', '--add', type=str, help='Characters to use, comma separated')
    parser.add_argument('-o', '--output', type=str, help='File to save the modified words')

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
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Words generated: {Fore.LIGHTBLUE_EX}{count}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Output saved to: {Fore.LIGHTBLUE_EX}{args.output}{Style.RESET_ALL}")
        else:
            for word in modified_words:
                print(word)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
