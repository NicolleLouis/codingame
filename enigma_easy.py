import sys
import math


def move_letter_n(letter, n):
    ascii_letter = ord(letter) - 65
    moved_ascii = (ascii_letter + n) % 26
    return chr(moved_ascii + 65)


def encode_ceasar_shifted(word, initial_shift):
    encrypted = ""
    shift = initial_shift
    for letter in word:
        encrypted += move_letter_n(letter, shift)
        shift += 1
    return encrypted


def decode_ceasar_shifted(word, initial_shift):
    decrypted = ""
    shift = - initial_shift
    for letter in word:
        decrypted += move_letter_n(letter, shift)
        shift -= 1
    return decrypted


def encode_with_rotor(message, rotor):
    encrypted = ""
    for letter in message:
        encrypted += rotor[ord(letter) - 65]
    return encrypted


def decode_with_rotor(message, rotor):
    decrypted = ""
    for letter in message:
        decrypted += chr(65 + rotor.find(letter))
    return decrypted


operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotors.append(input())
message = input()

if operation == "ENCODE":
    encode = encode_ceasar_shifted(message, pseudo_random_number)
    for rotor in rotors:
        encode = encode_with_rotor(encode, rotor)
    print(encode)
else:
    decrypted = decode_with_rotor(message, rotors[2])
    decrypted = decode_with_rotor(decrypted, rotors[1])
    decrypted = decode_with_rotor(decrypted, rotors[0])
    decrypted = decode_ceasar_shifted(decrypted, pseudo_random_number)
    print(decrypted)
