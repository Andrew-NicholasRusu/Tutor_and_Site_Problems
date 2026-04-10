"Let's use send information in the message labeling feature."

# Start by starring urgent messages and labeling the rest as inbox.

username = "ScroogeMakeDeck"
messages = [
    "URGENT: to join all hands, confirm your details at www.lockedin-allhands.com",
    "URGENT: approve the budget now.",
    "URGENT: limited-time offer - boost your team page today.",
    "Agenda link: www.lockedin.com/meet",
    "Heads up: deck review moved to Friday",
    "URGENT: confirm attendance at www.lockedin-checkin.com",
    "Special offer: try Premium free for 7 days.",
    "Got an urgent question about the Q4 roadmap."
]
for msg in messages:
    text = msg.lower()
    has_urgent = "urgent" in text
    if has_urgent: # checks if has_urgent is True
        label = "⭐️ Starred"
    else:
        label = "✉️ Inbox"
    print(f"[{label}]{msg}")
print() # Space

# Go through the senders of each message, and label each as either a contact or unknown sender. 
username = "ScroogeMakeDeck"
messages = [
    "URGENT: to join all hands, confirm your details at www.lockedin-allhands.com",
    "URGENT: approve the budget now.",
    "URGENT: limited-time offer - boost your team page today.",
    "Agenda link: www.lockedin.com/meet",
    "Heads up: deck review moved to Friday",
    "URGENT: confirm attendance at www.lockedin-checkin.com",
    "Special offer: try Premium free for 7 days.",
    "Got an urgent question about the Q4 roadmap."
    ]
senders = [
    "WFHomie",
    "Micr0-Mngr"
    "Chief_Excuse_Officer99",
    "VeePeeWee",
    "chiefOfStuff",
    "entrepreNerd",
    "rubiksCubicle",
    "MagnumKPI"
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "chiefOfStuff",
    "WFHomie"
    ]
for i in range (len(messages)):
    sender = senders[i]
    is_contact = sender in contacts # checks if sender is in the contacts list using the in operator.
    if is_contact: # checks if is_contact is True
        label = "✅ Contact"
    else:
        label = "❔ Unknown"
    print(f"[{label}]{sender}:{messages[i]}")
print() # Space

# Label messages from contacts as starred if they're urgent, or inbox if they're not
# Label messages from unknown senders as unknown.

username = "ScroogeMakeDeck"
messages = [
    "URGENT: to join all hands, confirm your details at www.lockedin-allhands.com",
    "URGENT: approve the budget now.",
    "URGENT: limited-time offer - boost your team page today.",
    "Agenda link: www.lockedin.com/meet",
    "Heads up: deck review moved to Friday",
    "URGENT: confirm attendance at www.lockedin-checkin.com",
    "Special offer: try Premium free for 7 days.",
    "Got an urgent question about the Q4 roadmap."
    ]
senders = [
    "WFHomie",
    "Micr0-Mngr"
    "Chief_Excuse_Officer99",
    "VeePeeWee",
    "chiefOfStuff",
    "entrepreNerd",
    "rubiksCubicle",
    "MagnumKPI"
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "chiefOfStuff",
    "WFHomie"
    ]
for i in range (len(messages)):
    text = messages[i].lower()
    sender = senders[i]
    is_contact = sender in contacts
    has_urgent = "urgent" in text
    if is_contact: # checks if the sender is a contact.
        if has_urgent:
            label = "⭐️ Starred"
        else:
            label = "✉️ Inbox"
        # When True, lines 100-103 classify the message by urgency (starred or inbox).
    else:
        label = "❔ Unknown"
        # When False, previous line labels all non-contact messages as unknown, regardless of urgency.
    print(f"[{label}]{sender}: {messages[i]}")
    # This nested structure separates contact messages from non-contact messages.
print() # Space

# Users find urgent messages from non-contacts spammy.
# Label messages from non-contracts as spam if they're urgent, or unknown otherwise.

username = "ScroogeMakeDeck"
messages = [
    "URGENT: to join all hands, confirm your details at www.lockedin-allhands.com",
    "URGENT: approve the budget now.",
    "URGENT: limited-time offer - boost your team page today.",
    "Agenda link: www.lockedin.com/meet",
    "Heads up: deck review moved to Friday",
    "URGENT: confirm attendance at www.lockedin-checkin.com",
    "Special offer: try Premium free for 7 days.",
    "Got an urgent question about the Q4 roadmap."
    ]
senders = [
    "WFHomie",
    "Micr0-Mngr"
    "Chief_Excuse_Officer99",
    "VeePeeWee",
    "chiefOfStuff",
    "entrepreNerd",
    "rubiksCubicle",
    "MagnumKPI"
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "chiefOfStuff",
    "WFHomie"
    ]
for i in range (len(messages)):
    text = messages[i].lower()
    sender = senders[i]
    is_contact = sender in contacts
    has_urgent = "urgent" in text
    if is_contact:
        if has_urgent:
            label = "⭐️ Starred"
        else:
            label = "✉️ Inbox"
    else:
        if has_urgent: #  checks urgency for non-contact messages.
            label = "⚠️ Spam" #  When True, labels them as spam. 
        else:
            label = "❔ Unknown" # When false, labels them as unknown
    print(f"[{label}] {sender}: {messages[i]}")
    # completes the classification for both contacts and non-contacts.
print() # Space 

# Users want to be aware of phishing attempts. 
# Label urgent messages that include a link as phishing, no matter the sender.

username = "ScroogeMakeDeck"
messages = [
    "URGENT: to join all hands, confirm your details at www.lockedin-allhands.com",
    "URGENT: approve the budget now.",
    "URGENT: limited-time offer - boost your team page today.",
    "Agenda link: www.lockedin.com/meet",
    "Heads up: deck review moved to Friday",
    "URGENT: confirm attendance at www.lockedin-checkin.com",
    "Special offer: try Premium free for 7 days.",
    "Got an urgent question about the Q4 roadmap."
    ]
senders = [
    "WFHomie",
    "Micr0-Mngr"
    "Chief_Excuse_Officer99",
    "VeePeeWee",
    "chiefOfStuff",
    "entrepreNerd",
    "rubiksCubicle",
    "MagnumKPI"
    ]
contacts = [
    "MagnumKPI",
    "VeePeeWee",
    "chiefOfStuff",
    "WFHomie"
    ]
for i in range(len(messages)):
    text = messages[i].lower()
    sender = senders[i]
    is_contact = sender in contacts
    has_urgent = "urgent" in text
    has_link = "www" in text
    if has_link and has_urgent:
        label = "🚨 Phishing"
    else:
        if is_contact:
            if has_urgent:
                label = "⭐ Starred"
            else:
                label = "✉️ Inbox"
        else:
            if has_urgent:
                label = "⚠️ Spam"
            else:
                label = "❔ Unknown"
        print(f"[{label}]{sender}: {messages[i]}")
print() # Space

"Prioritizing conditions when nesting logic keeps programs clear and efficient."