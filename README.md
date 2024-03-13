# Generate Password List From Wordlist in Python

This python script can generate possible passwords from a list of words (or passwords), by adding characters to the end of the word. You can also specify your own characters and output this all to a .txt file.

## Download

```
# Clone this repository

$ git clone https://github.com/yZ1337/python-passlist-gen.git
```

## Install Libraries

```
# Install Coloroma Python library (will be installed automatically on run)

$ pip install colorama
```

## Usage

```
$ python3 passlistgen.py -h

usage: passlistgen.py [-h] [-w WORDLIST] [-a ADD] [-o OUTPUT]

Modify words in a file by appending characters and save output.

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to the wordlist file
  -a ADD, --add ADD     Characters to use, comma separated
  -o OUTPUT, --output OUTPUT
                        File to save the modified words
```

```
$ python3 passlistgen.py -w old-pass-list.txt -o new-pass-list.txt

# Generates output file: new-pass-list.txt
```

```
$ python3 passlistgen.py -w old-pass-list.txt -a "!, 01, @, &, 7777, 1234, 0123" -o new-pass-list.txt

# Generates output file: new-pass-list.txt with specified special characters
```

## To Do List

Will try to add more updates in the feature!
