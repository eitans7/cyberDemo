"""
Author: Eitan Shoshan
Program name: Sukkot_assingment
Description:
for parameter encrypt - encrypts an input and saves in file
for parameter decrypt - decrypts a file content and prints it
Date: 27-09-23
"""
import sys
import logging
import os


LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'


encryption_dict = {'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, "I": 44, "J": 45,
                   "K": 46, "L": 47, "M": 48, "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63, "S": 64, "T": 65,
                   "U": 66, "V": 67, "W": 68, "X": 69, "Y": 10, "Z": 11, "a": 12, "b": 13, "c": 14, "d": 15,
                   "e": 16, "f": 17, "g": 18, "h": 19, "i": 30, "j": 31, "k": 32, "l": 33, "m": 34, "n": 35,
                   "o": 36, "p": 37, "q": 38, "r": 39, "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
                   "y": 96, "z": 97, " ": 98, ",": 99, ".": 100, ";": 101, "'": 102, "?": 103, "!": 104,
                   ":": 105}

decryption_dict = {}
for key, value in encryption_dict.items():
    decryption_dict[value] = key


def valid_parameter():
    """
    returns true if the first parameter equals to encrypt or decrypt, false if it isn't.
    """
    return sys.argv[1] == "encrypt" or sys.argv[1] == "decrypt"


def encrypt_assert():
    """
    checks if using the exact same encryption method as the regular encryption function encrypts the message
    as it supposed to.
    """
    str_tst = 'My bounty is as boundless as the sea, My love as deep; the more' \
              ' I give to thee, The more I have, for both are infinite.'
    encrypted_str_tst_supposedly = '48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,' \
                                   '90,98,12,90,98,91,19,16,98,90,16,12,99,98,48,96,98,33,36,93,16,98,12,90,98' \
                                   ',15,16,16,37,101,98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,' \
                                   '36,98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,' \
                                   '99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100'
    encrypted_str_tst = []
    for char in str_tst:
        if char in encryption_dict:
            encrypted_str_tst.append(str(encryption_dict[char]))
        else:
            encrypted_str_tst.append(char)
    return ','.join(encrypted_str_tst) == encrypted_str_tst_supposedly


def main():
    """
    using all the functions in the code to encrypt a message and save it to a file,
    or decrypt from a file.
    """
    if sys.argv[1] == 'encrypt':
        print("you chose to encrypt.")
        encrypted_message = (input("what's the message you would like to encrypt: "))
        logging.debug('the message: ' + encrypted_message)
        encrypted_message = encrypt(encrypted_message)
        logging.debug('the encrypted message: ' + encrypted_message)
        save_to_file(encrypted_message)
    if sys.argv[1] == 'decrypt':
        print("you chose to decrypt.")
        decrypted_message = decrypt_from_file('encrypted_message.txt')
        print(decrypted_message)


def encrypt(input_str):
    """
    gets a string as a parameter and encrypts it by the dictionary, then saves it in a file.
    """
    encrypted_str = []
    for char in input_str:
        if char in encryption_dict:
            encrypted_str.append(str(encryption_dict[char]))
        else:
            encrypted_str.append(char)
    return ','.join(encrypted_str)


def save_to_file(encrypted_text):
    """
    copies text to a file and save it.
    """
    with open('encrypted_message.txt', 'w') as f:
        f.write(encrypted_text)


def decrypt_from_file(filename):
    """
    decrypts the text from the file to the original message that was written.
    """
    with open(filename, 'r') as f:
        encrypted_text = f.read()

    # Check if the file is empty
    if not encrypted_text.strip():
        return "The file is empty."

    encrypted_numbers = encrypted_text.split(',')
    decrypted_text = []

    for num_str in encrypted_numbers:
        num = int(num_str.strip())  # Remove any extra whitespace and convert to integer
        if num in decryption_dict:
            decrypted_text.append(decryption_dict[num])
        else:
            decrypted_text.append('?')  # If the number is not in the dictionary, append a question mark

    return ''.join(decrypted_text)


if __name__ == '__main__':
    assert valid_parameter()
    assert encrypt_assert()
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
