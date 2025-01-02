from string import ascii_lowercase
from os import system, name
import sys

logo = """
------------------------------------------------
         oo          dP                         
                     88                         
.d8888b. dP 88d888b. 88d888b. .d8888b. 88d888b. 
88'  `"" 88 88'  `88 88'  `88 88ooood8 88'  `88 
88.  ... 88 88.  .88 88    88 88.  ... 88       
`88888P' dP 88Y888P' dP    dP `88888P' dP       
            88                                  
            dP                                                 
------------------------------------------------
"""
alphabet = list(ascii_lowercase)


def clear():
    system('cls' if name == 'nt' else 'clear')


def main():
    clear()
    print(logo)
    print('\n\nSelect from the menu: ')
    print('1. Encode')
    print('2. Decode')
    print('3. Decode by BruteForce method')
    print('4. Quit')
    user_input = input('\n\nEnter here: ')
    valid_inputs = ('1', '2', '3', '4')
    while user_input not in valid_inputs:
        user_input = input('Enter here: ')

    if user_input == '1':
        encode_menu()
    elif user_input == '2':
        decode_menu()
    elif user_input == '3':
        brute_force_menu()
    else:
        sys.exit()


def encode_menu():
    clear()
    print(logo)
    print('\t\t   ENCODE ')
    word = input('Enter a message to encode or q to go back: ').strip()
    while not word:
        word = input(
            'Message cannot be blank. Enter a message to encode or q to go back: '
        ).strip()
    if word == 'q':
        main()
    else:
        key = input("Enter a key: ")
        while not key.isdigit():
            key = input("Enter a key: ")
        encoded_message = encode(word, int(key))
        clear()
        print(logo)
        print(f"Message {word} encoded with key:{key}\n{encoded_message}")
    print('\nSelect from the menu: ')
    print('1. Try Again')
    print('2. MainMenu')
    print('3. Quit')
    user_input = input('\n\nEnter here: ')
    valid_inputs = ('1', '2', '3')
    while user_input not in valid_inputs:
        user_input = input('Enter here: ')

    if user_input == '1':
        encode_menu()
    elif user_input == '2':
        main()
    else:
        sys.exit()


def decode_menu():
    clear()
    print(logo)
    print('\t\t   DECODE ')
    word = input('Enter a message to decode or q to go back: ').strip()
    while not word:
        word = input(
            'Message cannot be blank. Enter a message to decode or q to go back: '
        ).strip()
    if word == 'q':
        main()
    else:
        key = input("Enter a key: ")
        while not key.isdigit():
            key = input("Enter a key: ")
        decoded_message = decode(word, int(key))
        clear()
        print(logo)
        print(f"Message {word} decoded with key:{key}\n{decoded_message}")
    print('\nSelect from the menu: ')
    print('1. Try Again')
    print('2. MainMenu')
    print('3. Quit')
    user_input = input('\n\nEnter here: ')
    valid_inputs = ('1', '2', '3')
    while user_input not in valid_inputs:
        user_input = input('Enter here: ')

    if user_input == '1':
        decode_menu()
    elif user_input == '2':
        main()
    else:
        sys.exit()


def brute_force_menu():
    clear()
    print(logo)
    print('\t\t   BRUTE FORCE')
    word = input(
        'Enter a message to perform a BruteForce decode or q to go back: '
    ).strip()
    while not word:
        word = input(
            'Message cannot be blank. Enter a message to perform a BruteForce decode or q to go back: '
        ).strip()
    if word == 'q':
        main()
    else:
        decoded_messages = brute_force_decode(word)
        clear()
        print(logo)
        for item in decoded_messages:
            print(item)
    print('\nSelect from the menu: ')
    print('1. Try Again')
    print('2. MainMenu')
    print('3. Quit')
    user_input = input('\n\nEnter here: ')
    valid_inputs = ('1', '2', '3')
    while user_input not in valid_inputs:
        user_input = input('Enter here: ')

    if user_input == '1':
        brute_force_menu()
    elif user_input == '2':
        main()
    else:
        sys.exit()


def encode(word, key):
    word = list(word.lower())
    encoded_word = ''

    for letter in word:
        if letter.isalpha():
            shift = alphabet.index(letter) + key
            encoded_word += alphabet[shift % 26]
        else:
            encoded_word += letter
    return encoded_word


def decode(word, key):
    word = list(word.lower())
    encoded_word = ''

    for letter in word:
        if letter.isalpha():
            shift = alphabet.index(letter) - key
            encoded_word += alphabet[shift % 26]
        else:
            encoded_word += letter
    return encoded_word


def brute_force_decode(word):
    shifts = [x for x in range(1, 27)]
    word = list(word.lower())
    decoded_word = ''
    decoded_words = []

    for shift in shifts:
        for letter in word:
            if letter.isalpha():
                key = alphabet.index(letter) - shift
                decoded_word += alphabet[key % 26]
            else:
                decoded_word += letter
        decoded_words.append(f"Key: {shift} Decoded Word: {decoded_word}")
        decoded_word = ''
    return decoded_words


if __name__ == '__main__':
    main()
