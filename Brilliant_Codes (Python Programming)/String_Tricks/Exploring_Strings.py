"Let's scan messages sent in the app to protect users from potential threats."

# Start by counting the number of characters in this message.

username = "WFHomie445"
message = "URGENT!!! Go to www.lockedin-secure01.com and verify your login"
length = len (message) # uses len(message) to count the number of characters in the message string.

print("Message has", length, "characters")
# returns 63 because the message has 63 characters.
print(message)
print() # Space

# If the message contains the word "URGENT", let the user know.

username = "WFHomie445"
message = "URGENT!!! Go to www.lockedin-secure01.com and verify your login"

if "URGENT" in message: # checks if the string "URGENT" is contained in the message string.
    # The in operator searches for the substring and returns True if found.
    print("Message claims to be urgent")
print(message)
print() # Space

"Strings are sequences of characters. You can measure their length and search them, among other things."

# Messages with links (containing "www") might be phishing attacks that try to steal sensitive user information.
# If a message contains both "URGENT" and "www", warn the user of phishing.

username = "WFHomie445"
message = "URGENT!!! Go to www.lockedin-secure01.com and verify your login"

if "URGENT" in message and "www" in message:
    print("Phishing!")
print(message)
print() # Space

# Heres a protip: to find a word no matter how it's capitalized, convert the string to lowercase using Python's lower method.

username = "WFHomie445"
message = "Click here: www.free-stuff99.biz. Hurry, it's UrGEnT!"

text = message.lower() # converts the message to lowercase using message.lower() and stores it in the variable text.
if "urgent" in text and "www" in text: # hecks if both "urgent" and "www" are in the lowercase text.
    print("Phishing!")
print(message)
print() # Space

"Scanning strings is key to reading data and detecting patterns."


