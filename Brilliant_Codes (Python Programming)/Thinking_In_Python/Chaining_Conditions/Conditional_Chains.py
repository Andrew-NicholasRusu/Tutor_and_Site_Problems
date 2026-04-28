"Let's start bulding a feature to sort messages into folders"

# If a message has an offer, put it in the Promos folder.

username = "MagnumKPI"
messages = [
    "Password reset urgently needed: www.locked-in.com",
    "Special offer for repeat customers",
    "Urgent: time is running out on this offer.",
    "Click this one-time urgent offer: www.not-a-scam.co",
    "Security training Monday"
]
promos = [] # initializes an empty list to store promo messages.
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    if has_offer: # checks if a message contains "offer"
        promos.append(msg) # If so, this line adds that message to the promos list.
for msg in promos:
    print(f"[💸 Promos]{msg}")
print() # Space

# If an offer claims to be urgent, put it in the Spam folder.

username = "MagnumKPI"
messages = [
    "Password reset urgently needed: www.locked-in.com",
    "Special offer for repeat customers",
    "Urgent: time is running out on this offer.",
    "Click this one-time urgent offer: www.not-a-scam.co",
    "Security training Monday"
]
promos = []
spam = [] #  creates a list for spam messages.
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    has_urgent = "urgent" in text
    if has_offer and has_urgent: # checks if a message has both an offer and is urgent.
        spam.append(msg) # if so, it adds it to the spam list
    if has_offer: # checks if the message has an offer and adds it to promos
        promos.append(msg)
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
    # Messages meeting both conditions get added to both lists.
print() # Space

"We can use elif to make the program put each message in only one folder."
"In Python, elif stands for else if"

# If a message isn't spam, put it in the Promos folder only if it has an offer.

username = "MagnumKPI"
messages = [
    "Password reset urgently needed: www.locked-in.com",
    "Special offer for repeat customers",
    "Urgent: time is running out on this offer.",
    "Click this one-time urgent offer: www.not-a-scam.co",
    "Security training Monday"
]
promos = []
spam = [] #  creates a list for spam messages.
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    has_urgent = "urgent" in text
    if has_offer and has_urgent: # checks if a message has both an offer and is urgent, adding it to spam.
        spam.append(msg) 
    elif has_offer: # uses elif (else if) to check if it just has an offer. 
    # The elif only runs when the first condition is False, so messages already added to spam won't be added to promos. 
    # Each message goes to only one folder.
        promos.append(msg)
# print messages...
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
print() # Space

# Make a Phishing folder for urgent messages with links. Put urgent offers without linkes in Spam, not Phishing.

username = "MagnumKPI"
messages = [
    "Password reset urgently needed: www.locked-in.com",
    "Special offer for repeat customers",
    "Urgent: time is running out on this offer.",
    "Click this one-time urgent offer: www.not-a-scam.co",
    "Security training Monday"
]
promos = []
spam = []
phishing = [] # creates a phishing folder.
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    has_urgent = "urgent" in text
    has_link = "www" in text
    if has_link and has_urgent:
        phishing.append(msg) # handles urgent messages with links; these go to phishing.
    elif has_offer and has_urgent:
        spam.append(msg) # check if a message has an offer and is urgent (but didn't match the first condition, so no link); these go to spam.
    elif has_offer:
        promos.append(msg) # check if a message just has an offer; these go to promos
# print messages;
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
for msg in phishing:
    print(f"[🚨 Phishing]{msg}")
print() # Space

"Conditional chains organize logic by considering each case in order."
