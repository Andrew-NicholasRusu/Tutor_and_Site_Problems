"Let's try to crack a Vigenère cipher without knowing the key."
"Try the list of keys to see if any can decrypt the ciphertext."

def position_of(letter):
    alphabet_start = ord('a')
    return ord(letter) - alphabet_start
def letter_at(position):
    alphabet_start = ord('a')
    return chr(position + alphabet_start)
def shift_number(position, n):
    return (position + n) % 26
def is_lowercase(letter):
    return letter in "abcdefghijklmnopqrstuvwxyz"
def shift(letter, n):
    if is_lowercase(letter):
        pos = position_of(letter)
        shifted = shift_number(pos, n)
        return letter_at(shifted)
    return letter
def decrypt (text, key):
    decrypted = ""
    for letter in text:
        decrypted += shift(letter, -1 * key)
    return decrypted
def uses_common_word(text):
    common_words = ["the", "and", "or", "for", "it", "are", "not", "at", "to", "of", "is", "be", "do"]
    for word in text.split():
        if word in common_words:
            return True
        return False
def decrypt_vingenere(text, key):
    shifts = [position_of(letter) 
              for letter in key]
    decrypted = ""
    key_index = 0
    for letter in text:
        if is_lowercase(letter):
            key_shift = shifts[key_index % len (shifts)]
            decrypted += shift(letter, -1 * key_shift)
            key_index += 1
        else:
            decrypted += letter
    return decrypted

ciphertext = "vhr kmwsr lq utvoj qn gkc oaencv, bhw rje " \
            "ehyntbu gu tnngpg n ompg glkg tb jcv hruc"
keys_to_try = ["dog", "cat", "penguin", "candy", "x"]
for key in keys_to_try:
    decrypted = decrypt_vingenere(ciphertext, key)
    print(decrypted) 

# stl hyqpd fn gnsad nz aho ixqhzh, vei lgq yekhqno dg nkzams h lyjd sfhs ny vws tlro
# thy imdqr so uatoq on nic vyeuav, ifw yhe lfyurbb eu alnnng u mmwe gsig az jjt hysc
# gde esofc hd oznbu ma aqu blaawb, tuh nwy kzlypoo mm gyjtjm f bxlt arct ex wwb zefy
# the house is still on the market, but the realtor is taking a long time to get here
# yku npzvu ot xwyrm tq jnf rdhqfy, ekz umh hkbqwex jx wqqjsj q rpsj jonj we mfy kuxf

"Let's write a specification for the count_frequencies function. What types of data should it input and return?"

"""
Function name: count_frequencies
Inputs: a decrypted message (str)
Returns: letter frequencies (dict {str: int})

Returns a dictionary that maps each letter to the number of times it appears in the drcypted message.
"""

"A function contract describes what the function should do. An AI coding assistant can write a function given a function contract."
"The count_frequencies function should take a string as input and return a dictionary mapping letters to counts."

"When a letter is not in the input text, its frequency should be zero."
"Update the function contract to specify that the dictionary should contain all the letters in the alphabet."

"""

Function name: count_frequencies
Inputs: a decrypted message(str)
Returns: letter frequencies (dict {str: int})

Returns a dictionary that maps each letter in the alphabet
to the number of times it appears in the text. All 26 letters 
are included, with a count of 0 for letters that don't appear.
"""

"The AI updated the function using the new contract and added code to count e's (common in English) and z's (uncommon)."
"Based on the output, which key seems most likely to produce English text?"

def decrypt_vigenere(text, key):
    shifts = [position_of(letter)
              for letter in key]
    decrypted = ""
    key_index = 0
    for letter in text:
        if is_lowercase(letter):
            key_shift = shifts[key_index % len(shifts)]
            decrypted += shift(letter, -1 * key_shift)
            key_index += 1
        else:
            decrypted += letter
    return decrypted
def count_frequencies (text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return {letter: text.count(letter)
            for letter in letters}

# message and keys to try ...
message = "vhr kmwsr lq utvoj qn gkc oaencv, bhw rje ehyntbu gu tnngpg n ompg glkg tb jcv hruc"
keys_to_try = ["dog", "cat", "penguin", 'candy', "x"]
decrypted = [decrypt_vigenere(message, key) 
             for key in keys_to_try]
freqs = [count_frequencies(text) for text in decrypted]
for i in range(len(keys_to_try)):
    freq = freqs[i]
    print(f"{keys_to_try[i]}: e's: {freq['e']}, z's: {freq['z']}") # The program decrypts the message with each key, then counts e's and z's.
# The key "candy" produced 1010 e's and 00 z's, the best match.

"Write a contract for a function that checks whether a decrypted message looks like English based on the frequency of e's and z's."

"""
Function name: looks_english
Inputs: a decrypted message (str)
Returns: whether it looks like English (bool)

Returns True if the input text contains more than 
8 percent e's and less than 1 percent z's. Uses 
count_frequencies as a helper functions.
"""

"Here's what the AI assistant wrote based on the function contract. Use it to print the decrypted messages that look like English."

def decrypt_vigenere(text, key):
    shifts = [position_of(letter)
              for letter in key]
    decrypted = ""
    key_index = 0
    for letter in text:
        if is_lowercase(letter):
            key_shift = shifts[key_index % len(shifts)]
            decrypted += shift(letter, -1 * key_shift)
            key_index += 1
        else:
            decrypted += letter
    return decrypted
def count_frequencies (text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return {letter: text.count(letter)
            for letter in letters}
def looks_english(text):
    text = text.lower()
    freqs = count_frequencies(text)
    total_letters = sum(freqs.values())
    if total_letters == 0:
        return False
    percent_e = freqs['e'] / total_letters
    percent_z = freqs['z'] / total_letters
    return percent_e > 0.08 and percent_z < 0.01

# message and keys to try...
message = "vhr kmwsr lq utvoj qn gkc oaencv, bhw rje ehyntbu gu tnngpg n ompg glkg tb jcv hruc"
keys_to_try = ["dog", "cat", "penguin", "candy", "x"]
decrypted = [decrypt_vingenere(message, key)
             for key in keys_to_try]
for text in decrypted:
    if looks_english(text): # checks looks_english(text) — only results that read like English get printed.
        print(text) # the house is still on the market, but the realtor is taking a long time to get here


"You wrote function contracts to guide an AI coding assistant."
"In the age of AI-assisted coding, writing complete and accurate specifications is a crucial skill."