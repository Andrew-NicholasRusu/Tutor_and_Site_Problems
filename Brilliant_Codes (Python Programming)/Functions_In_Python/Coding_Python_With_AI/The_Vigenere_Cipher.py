"Let's look at a cipher that's harder to crack than the shift cipher."
"Decode the message. Keep track of the number of lowercase letters."

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


message = "ymj fhhtzsyfsy gwjjix mfrxyjwx"
# clue: shift backward 5
letter_count = 0
for letter in message:
    if is_lowercase(letter):
        print(shift(letter, -5), end = "")
        letter_count += 1
    else:
        print(letter, end = "")
print(f"\nDecoded {letter_count} letters")
# the accountant breeds hamsters
# Decoded 27 letters

"Now, the message uses a list of shifts instead of just one. Decode the message using a list of shifts."

message = "ulbx jw osu mo xii gmmi"
# clue: alternate shifting letters backward 1 or 4, skip other characters
letter_count = 0
shifts = [1, 4]
for letter in message:
    if is_lowercase(letter):
        shift_amount = shifts [letter_count % 2]
        print(shift(letter, -1 * shift_amount), end = "")
        letter_count += 1
    else:
        print(letter, end = "")
# that is not in the file
print() # Space 

"This time there are three shifts to cycle through. Decode the message."

message = "wpk omjjmx kiy pwbhl"
# clue: cycle through backward shifts 3, 8, and 6
letter_count = 0
shifts = [3, 8, 6]
for letter in message:
    if is_lowercase(letter):
        shift_amount = shifts [letter_count % 3]
        print(shift(letter, -1 * shift_amount), end = "")
        letter_count += 1
    else:
        print(letter, end = "")
# the ledger has moved
print() # Space

"To produce the ciphertext, shift each letter of the plaintext forward by 3, 8, and 6, in a repeating pattern."
"A cipher disguises a plaintext message as encrypted ciphertext. The Vigenère cipher does this using a list of shifts."

"Write a decryption function for the Vigenère cipher."

def decrypt_vingenere(text, shifts):
    decrypted = ""
    letter_index = 0
    for letter in text:
        if is_lowercase(letter):
            shift_amount = shifts[letter_index % len(shifts)]
            decrypted += shift(letter, -1 * shift_amount)
            letter_index += 1
        else:
            decrypted += letter
    return decrypted

message = "fo tsv rkuweyx cn gyfiz"
# clue: cycle through backward shifts 2, 0, 6, 4
print(decrypt_vingenere(message, [2, 0, 6, 4])) # do not request an audit
print() # Space

"Let's encode the shifts as a keyword, where the shifts are the alphabet positions. For example, [2, 0, 6, 4] is the keyword 'cage' (c → 2, a → 0, g → 6, e → 4)."
"Update the function to take a keyword instead of a list of shifts."

def DecRyPt_V1ngenere (text, key):
    shifts = [position_of(letter) # builds that shift list by calling position_of on each letter in the key, converting the keyword into shifts automatically.
              for letter in key]
    decrypted = ""
    letter_index = 0
    for letter in text:
        if is_lowercase(letter):
            shift_amount = shifts[letter_index % len(shifts)]
            decrypted += shift(letter, -1 * shift_amount)
            letter_index += 1
        else:
            decrypted += letter
    return decrypted

message = "hirmpg lst bgrmratvce"
# clue: cycle through backward shifts 2 (c), 0 (a), 6 (g), and 4 (e).
print(DecRyPt_V1ngenere(message, "cage")) # filing for bankruptcy

"Although the Vigenère cipher dates back to the 16th century, a general method for cracking it (decrypting it without the key) was not discovered until much later."
"Why is the Vigenère cipher harder to crack than the shift cipher?"
# Answer: There are only 26 possible keys for the shift cipher, but the Vigenere cipher has vastly more possible keys.

"You decrypted the Vigenère cipher given the key."
"The Vigenère cipher is much tougher to crack when you don't know the key."