"Let's finish up the message sorting feature."

# Put non-urgent offers in the Promos folder and urgent offers in the Spam folder.
username = "vpOfVibes"
messages = [
    "Urgent: Check out this offer at www.braindrain.com",
    "Please use the team password manager",
    "I'm in urgent need of that report!",
    "Special offer for repeat customers",
    "Situation urgent: only 5 tickets left!",
    "There's an urgent situation with our offer",
    "Turns out that report is urgent",
    "Check out this offer, urgently please."
    ]
senders = [
    "ThoughtLeader",
    "StakeHandHolder",
    "EmilyVP",
    "PusherOfPaper",
    "CorporateOverload",
    "WFHomie",
    "GoldenParachuter",
    "TeamPlaya79"
    ]
contacts = [
    "EmilyVP",
    "WFHomie",
    "ThoughtLeader"
    ]
# initialize folder lists...
inbox = []
promos = []
spam = []
for i in range(len(messages)):
    print("Sorting message", i)
    # variables:
    text = messages[i].lower()
    is_contact = senders[i] in contacts
    has_urgent = "urgent" in text
    has_link = "www" in text
    has_offer = "offer" in text
    msg_string = f"{senders[i]}: {messages[i]}"
    if has_urgent and has_offer: #  checks if a message has an offer AND is urgent.
        spam.append(msg_string) # When both are True, this line adds it to spam.
    elif has_offer: # checks if the message has an offer (but is not urgent, since line 37 was False).
        promos.append(msg_string) #  If True, this line adds it to promos.
    else:
        inbox.append(msg_string)
# print messages:
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
    # This chain prioritizes spam over promos.
print() # SPACE

"When building a conditional chain, check the strongest conditions first."

# Put urgent messages with lins in Phishin, and urgent offers in Spam. Prioritize Phishing over Spam.

username = "vpOfVibes"
messages = [
    "Urgent: Check out this offer at www.braindrain.com",
    "Please use the team password manager",
    "I'm in urgent need of that report!",
    "Special offer for repeat customers",
    "Situation urgent: only 5 tickets left!",
    "There's an urgent situation with our offer",
    "Turns out that report is urgent",
    "Check out this offer, urgently please."
    ]
senders = [
    "ThoughtLeader",
    "StakeHandHolder",
    "EmilyVP",
    "PusherOfPaper",
    "CorporateOverload",
    "WFHomie",
    "GoldenParachuter",
    "TeamPlaya79"
    ]
contacts = [
    "EmilyVP",
    "WFHomie",
    "ThoughtLeader"
    ]
# initialize folder lists...
inbox = []
promos = []
spam = []
phishing = []
for i in range(len(messages)):
    print("Sorting message", i)
    # variables:
    text = messages[i].lower()
    is_contact = senders[i] in contacts
    has_urgent = "urgent" in text
    has_link = "www" in text
    has_offer = "offer" in text
    msg_string = f"{senders[i]}: {messages[i]}"
    if has_urgent and has_link: # checks if a message has a link AND is urgent.
        phishing.append(msg_string) # adds it to phishing.
    elif has_urgent and has_offer: #  uses elif to check for urgent offers (but no link, since line 103 was False). 
        spam.append(msg_string)
    elif has_offer:
        promos.append(msg_string)
    else:
        inbox.append(msg_string)
# print messages:
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
for msg in phishing:
    print(f"[🚨 Phishing]{msg}")
    # The chain prioritizes flagging phishing over spam.
print() # SPACE

# Users want an update to the sorting rules. Put urgent messages with links in Phishing, no matter who sent them. 
# Put urgent offers in Spam, unless they're from contacts. Star urgent messages from contacts.

username = "vpOfVibes"
messages = [
    "Urgent: Check out this offer at www.braindrain.com",
    "Please use the team password manager",
    "I'm in urgent need of that report!",
    "Special offer for repeat customers",
    "Situation urgent: only 5 tickets left!",
    "There's an urgent situation with our offer",
    "Turns out that report is urgent",
    "Check out this offer, urgently please."
    ]
senders = [
    "ThoughtLeader",
    "StakeHandHolder",
    "EmilyVP",
    "PusherOfPaper",
    "CorporateOverload",
    "WFHomie",
    "GoldenParachuter",
    "TeamPlaya79"
    ]
contacts = [
    "EmilyVP",
    "WFHomie",
    "ThoughtLeader"
    ]
# initialize folder lists...
inbox = []
promos = []
spam = []
phishing = []
starred = []
for i in range (len(messages)):
    print("sorting message", i)
    # variables:
    text = messages[i].lower()
    is_contact = senders[i] in contacts
    has_urgent = "urgent" in text
    has_link = "www" in text
    has_offer = "offer" in text
    msg_string = f"{senders[i]}: {messages[i]}"
    if has_urgent and has_link:
        phishing.append(msg_string)
    elif has_urgent and is_contact:
        starred.append(msg_string)
    elif has_urgent and has_offer:
        spam.append(msg_string)
    elif has_offer:
        promos.append(msg_string)
    else:
        inbox.append(msg_string)
# print messages:
for msg in starred:
    print(f"[⭐ Priority]{msg}")
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in promos:
    print(f"[💸 Promos]{msg}")
for msg in spam:
    print(f"[⚠️ Spam]{msg}")
for msg in phishing:
    print(f"[🚨 Phishing]{msg}")

"Conditional chains express logical priority in programs."