import random

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
