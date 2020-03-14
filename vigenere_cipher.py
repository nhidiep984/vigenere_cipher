from string import ascii_lowercase

def key_generation(plaintext, key_string):
    plaintext_len = len(plaintext)
    repeated_key = key_string
    repeatedkey_len = len(key_string)

    while repeatedkey_len < plaintext_len:
        repeated_key = repeated_key + key_string
        repeatedkey_len = len(repeated_key)
        leftover_chars = repeatedkey_len - plaintext_len
        repeated_key = repeated_key[0:repeatedkey_len - leftover_chars]
    return ''.join(repeated_key)

def encryption(plaintext, repeated_key):
    plaintext_pos = [letter_to_index[letter] for letter in plaintext]
    key_pos = [letter_to_index[letter] for letter in repeated_key]
    ciphertext_pos = []
    ciphertext = []

    for x, y in zip(plaintext_pos, key_pos):
        sum = x+y
        if sum >= 26:
            sum = sum - 26
        ciphertext_pos.append(sum)

    for num in ciphertext_pos:
        letter = index_to_letter[num]
        ciphertext.append(letter)
    return ''.join(ciphertext)

def decryption(ciphertext, repeated_key):
    ciphertext_pos = [letter_to_index[letter] for letter in ciphertext]
    key_pos = [letter_to_index[letter] for letter in repeated_key]
    plaintext_pos = []
    plaintext = []

    for x,y in zip(ciphertext_pos, key_pos):
        difference = x - y
        if difference < 0:
            difference = difference + 26
        plaintext_pos.append(difference)

    for num in plaintext_pos:
        letter = index_to_letter[num]
        plaintext.append(letter)
    return ''.join(plaintext)


if __name__ == '__main__':
    letter_to_index = dict(zip(ascii_lowercase, range(len(ascii_lowercase))))
    index_to_letter = dict(zip(range(len(ascii_lowercase)), ascii_lowercase))
    plaintext = input("Enter string to encrypt: ").lower().replace(" ", "")
    key_string = list(input("Enter key string: "))
    repeated_key = key_generation(plaintext, key_string)
    ciphertext = encryption(plaintext, repeated_key)
    print('Ciphertext:', ciphertext)
    plaintext = decryption(ciphertext, repeated_key)
    print('Decrypted message: ', plaintext)