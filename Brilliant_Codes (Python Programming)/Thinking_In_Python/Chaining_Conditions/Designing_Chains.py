"Let's consider sender information when sorting messages into folders."

# Add sender information to messages, and put messages from contacts in the inbox.

username = "entrepreNerd"
messages = [
    "Install security updates today",
    "Do you have time to chat?",
    "Go to www.urgent-updates.com right away!!",
    "URGENT: click on www.pwd-changeme.biz and do what it says.",
    "Security training urgently needed",
    "fyi: Team sync postponed"
    ]
senders = [
    "MagnumKPI",
    "WFHomie",
    "DealDigger",
    "MicrO-Mngr",
    "VeePeeWee",
    "chiefOfStuff",
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "cheifOfStuff",
    "MicrO-Mngr",
    ]
inbox = []
for i in range (len(messages)):
    print("Sorting message", i)
    sender = senders[i]
    is_contact = sender in contacts # checks if the sender is in the contacts list.
    msg_string = f"{sender}:{messages[i]}" # creates a message string combining the sender and message.
    if is_contact: # checks if the sender is a contact
        inbox.append(msg_string) # if so, this adds the formatted message to the inbox.
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
print() # SPACE

# Which messages does this program leave out of the folders it creates?

username = "entrepreNerd"
messages = [
    "Install security updates today",
    "Do you have time to chat?",
    "Go to www.urgent-updates.com right away!!",
    "URGENT: click on www.pwd-changeme.biz and do what it says.",
    "Security training urgently needed",
    "fyi: Team sync postponed"
    ]
senders = [
    "MagnumKPI",
    "WFHomie",
    "DealDigger",
    "MicrO-Mngr",
    "VeePeeWee",
    "chiefOfStuff",
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "cheifOfStuff",
    "MicrO-Mngr",
    ]
starred = []
inbox = []
for i in range (len(messages)):
    print("Sorting message", i)
    text = messages[i].lower()
    sender = senders[i]
    is_contact = sender in contacts
    has_urgent = "urgent" in text
    msg_string = f"{sender}: {messages[i]}"
    if has_urgent and is_contact: # checks if a message is both urgent and from a contact.
        # If so, line 77 adds it to the starred list.
        starred.append(msg_string)
    elif is_contact: # uses elif to check if the message is from a contact (but wasn't urgent, since the first condition was False).
        # If so, line 80 adds it to the inbox list.
        inbox.append(msg_string)

    #  Messages from non-contacts don't match either condition and aren't added to any list.
# print messages:
for msg in starred:
    print(f"[⭐ Starred] {msg}")
for msg in inbox:
    print(f"[✉️ Inbox] {msg}")
print() # SPACE

"In a conditional chain, a condition is checked only if all the previous conditions were False"

# Put urgent messages with links in Phishing, even if they're from contacts. 
# Star other urgent messages from contacts. Put all other messages in the inbox.

username = "entrepreNerd"
messages = [
    "Install security updates today",
    "Do you have time to chat?",
    "Go to www.urgent-updates.com right away!!",
    "URGENT: click on www.pwd-changeme.biz and do what it says.",
    "Security training urgently needed",
    "fyi: Team sync postponed"
    ]
senders = [
    "MagnumKPI",
    "WFHomie",
    "DealDigger",
    "MicrO-Mngr",
    "VeePeeWee",
    "chiefOfStuff",
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "cheifOfStuff",
    "MicrO-Mngr",
    ]
starred = []
inbox = []
phishing = []
for i in range(len(messages)):
    print("Sorting message", i)
    # variables:
    text = messages[i].lower()
    sender = senders[i]
    is_contact = sender in contacts
    has_urgent = "urgent" in text
    has_link = "www" in text
    msg_string = f"{sender}: {messages[i]}"
    if has_urgent and has_link: # checks if a message is both urgent and has a link.
        # These go to phishing, even if from a contact.
        phishing.append(msg_string)
    elif has_urgent and is_contact: # uses elif to check if the message is urgent and from a contact (but didn't match the first condition, so no link). 
        # These go to starred.
        starred.append(msg_string)
    else: # uses else to put all remaining messages in inbox.
        inbox.append(msg_string)
# print messages:
for msg in starred:
    print(f"[⭐ Starred]{msg}")
for msg in inbox:
    print(f"[✉️ Inbox]{msg}")
for msg in phishing:
    print(f"[🚨 Phishing]{msg}")

"Designing conditional chains is a key technique for dealing with logical tasks."


