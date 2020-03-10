alphabet = 'abcdefghijklmnpoqrstuvwxyz'

def key_generation(plaintext, key_string):
    #key_string = list(key_string)
    #keystring_len = len(key_string)
    plaintext_len = len(plaintext)
    repeated_key = key_string
    repeatedkey_len = len(key_string)

    while repeatedkey_len < plaintext_len:
        repeated_key = repeated_key + key_string
        repeatedkey_len = len(repeated_key)
        leftover_chars = repeatedkey_len - plaintext_len
        repeated_key = repeated_key[0:repeatedkey_len - leftover_chars]
    print(''.join(repeated_key))

def encryption():
    for letter in plaintext:



def decryption(ciphertext, repeated_key):
    pass


if __name__ == '__main__':
    plaintext = input("Enter string to encrypt: ").lower().replace(" ", "")
    key_string = list(input("Enter key string: "))
    key_generation(plaintext, key_string)