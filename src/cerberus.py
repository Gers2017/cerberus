from random import randrange
from string import ascii_lowercase
from typing import Tuple
from functools import reduce


def get_seed_from_factors(factors):
    prod = reduce(lambda x, y: x * y, factors)
    return [int(i) for i in str(prod).split()]


def generate_seed(st=1, to=797):
    seed = [randrange(st, to) for i in range(7)]
    return seed


def shift_letter(index: int, shift: int):
    alpha_len = len(ascii_lowercase)
    return ascii_lowercase[(index + shift) % alpha_len]


def get_character_index(ch) -> Tuple[bool, int]:
    index = ascii_lowercase.find(ch)
    return index != -1, index


def cerberus_cipher(message: str):
    message = message.lower()
    seed = generate_seed()
    cipher = ""
    seed_index = 0

    for ch in message:
        is_valid, index = get_character_index(ch)
        if is_valid:
            shift = seed[seed_index]
            cipher += shift_letter(index, shift)
            seed_index = (seed_index + 1) % len(seed)
        else:
            cipher += str(randrange(0, 9))

    return cipher, seed


def cerberus_decipher(cipher, seed):
    message = ""
    seed_index = 0

    for ch in cipher:
        is_valid, index = get_character_index(ch)
        if is_valid:
            shift = -seed[seed_index]
            message += shift_letter(index, shift)
            seed_index = (seed_index + 1) % len(seed)
        else:
            message += " "
    return message
