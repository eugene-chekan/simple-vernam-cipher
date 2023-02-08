from typing import List


def xor_step(a, b):
    a_ascii = a if isinstance(a, int) else ord(a)
    b_ascii = ord(b)
    # Convert ASCII codes to binary numbers
    a_bin = bin(a_ascii)[2:].zfill(8)
    b_bin = bin(b_ascii)[2:].zfill(8)
    # XOR operation on binary numbers
    xor_result = b''
    for i in range(8):
        if a_bin[i] == b_bin[i]:
            xor_result += b'0'
        else:
            xor_result += b'1'
    return xor_result


def vernam_encrypt(message: str, key: str) -> List[int]:
    if len(message) != len(key):
        raise ValueError(f'Message={len(message)} symbols, key={len(key)} symbols. Must be equal.')

    return [int(xor_step(message[i], key[i]), 2) for i in range(len(message))]


def vernam_decrypt(code: List[int], key: str) -> str:
    if len(code) != len(key):
        raise ValueError(f'Code={len(code)} symbols, key={len(key)} symbols. Must be equal.')

    return ''.join(chr(int(xor_step(code[i], key[i]), 2)) for i in range(len(code)))
