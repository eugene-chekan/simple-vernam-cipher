import cipher

if __name__ == '__main__':
    code = [b'00011000', b'00000100', b'00001001']
    key = 'RED'

    print(cipher.vernam_decrypt(code, key))
