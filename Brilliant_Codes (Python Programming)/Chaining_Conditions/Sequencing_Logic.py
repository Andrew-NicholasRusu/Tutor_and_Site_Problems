"Let's continue building the message sorting feature."

# Put messages with offers in the Promos folder.

username = "Micr0-Mngr"
messages = [
    "Check out www.treefarm.com to reedeem this offer!",
    "Holiday season deals on offer!",
    "URGENT: go to www.appple.com and enter your credentials to claim your offer!",
    "Do you know the code for the copier?",
    "Uploaded that spreadsheet to the shared drive.",
    "Limited Time Special Offer for Bosses. Urgent!"
    ]
promos = []
for msg in messages:
    print("sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    if has_offer: # Checks if has_offer is True.
        promos.append(msg) # If true, it appends the message to the promos list.
# After the loop completes, lines 22-23 print all messages in the promos list.
for msg in promos:
    print(f"[💸 Promos]{msg}")
print() # Space

# If a message is not a promo, put it in the Inbox.

username = "Micr0-Mngr"
messages = [
    "Check out www.treefarm.com to reedeem this offer!",
    "Holiday season deals on offer!",
    "URGENT: go to www.appple.com and enter your credentials to claim your offer!",
    "Do you know the code for the copier?",
    "Uploaded that spreadsheet to the shared drive.",
    "Limited Time Special Offer for Bosses. Urgent!"
    ]
promos = []
inbox = [] # creates an empty inbox list.
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    if has_offer:
        promos.append(msg)
    else:
        inbox.append(msg) # checks each message: if it has an offer (line 43), it goes to promos (line 44).
        # Otherwise, line 46 runs and appends the message to inbox. This separates messages into two categories.
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")

# In an offer claims to be urgent, put it in Spam, not Promos.

username = "Micr0-Mngr"
messages = [
    "Check out www.treefarm.com to reedeem this offer!",
    "Holiday season deals on offer!",
    "URGENT: go to www.appple.com and enter your credentials to claim your offer!",
    "Do you know the code for the copier?",
    "Uploaded that spreadsheet to the shared drive.",
    "Limited Time Special Offer for Bosses. Urgent!"
    ]
promos = []
inbox = []
spam = []
for msg in messages:
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    has_urgent = "urgent" in text
    if has_offer and has_urgent: # checks if a message has an offer AND is urgent.
        spam.append(msg)
    elif has_offer:
    # When both are True, line 73 adds it to spam. Otherwise, line 74 checks if it has an offer (but not urgent).
        promos.append(msg)
    else: # The final else branch runs if none of the previous condtions are True
        inbox.append(msg)
    # If True, line 76 adds it to promos. If neither condition matches, line 77 adds it to inbox.
# print messages.
for msg in inbox:
    print(f"[[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")

"A conditional chain checks a sequence of conditions in order."

# Put urgent messages with links in Phishing. Urgent messages with offers and no links go in Spam.

username = "Micr0-Mngr"
messages = [
    "Check out www.treefarm.com to reedeem this offer!",
    "Holiday season deals on offer!",
    "URGENT: go to www.appple.com and enter your credentials to claim your offer!",
    "Do you know the code for the copier?",
    "Uploaded that spreadsheet to the shared drive.",
    "Limited Time Special Offer for Bosses. Urgent!"
    ]
promos = []
inbox = []
spam = []
phishing = []
for msg in messages: 
    print("Sorting message...")
    text = msg.lower()
    has_offer = "offer" in text
    has_urgent = "urgent" in text
    has_link = "www" in text
    if has_link and has_urgent: # checks if a message has a link AND is urgent.
        phishing.append(msg) # When both are True, this adds it to phishing.
    elif has_offer: # uses elif to check if the message has an offer and is urgent (but no link). 
        # If True, next line adds it to spam.
        spam.append(msg)
    elif has_offer:
        promos.append(msg)
    else:
        inbox.append(msg)
    # The chain prioritizes flagging phishing attempts over spam.
# print messages...
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
for msg in phishing:
    print(f"[🚨 Phishing]{msg}")

"Conditional chains can organize a sequence of logical conditions."