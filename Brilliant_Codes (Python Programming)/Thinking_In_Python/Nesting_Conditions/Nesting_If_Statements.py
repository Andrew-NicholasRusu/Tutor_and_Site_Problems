"Let's label a user's messages to warn them of unsafe ones."

# Start by labeling all messages as inbox.

username = "MagnumKPI"
messages = [
    "Special offer: Join our leadership webinar at www.lockedin.com/events",
    "URGENT: The deck for board meeting due by end of day",
    "Weekly digest: top posts from your network.",
    "New connection - view profile at www.lockedin.com/profiles/ajones",
    "Special offer: get Premium free for 1 month",
    "URGENT: limited-time offer - claim at www.lockedin-business-spotlight.com",
    "Career meetup next week - RSVP opens Monday.",
    "URGENT: To claim your offer, verify your account at www.lockedin-secure-login.com"
]
for msg in messages: # starts a loop that iterates over each message in the messages list. 
    label = " ✉️  Inbox"
    print(f"[{label}] {msg}") # prints each message with the inbox label.
print() # Space

# Label urgent messages with links as phishing.

username = "MagnumKPI"
messages = [
    "Special offer: Join our leadership webinar at www.lockedin.com/events",
    "URGENT: The deck for board meeting due by end of day",
    "Weekly digest: top posts from your network.",
    "New connection - view profile at www.lockedin.com/profiles/ajones",
    "Special offer: get Premium free for 1 month",
    "URGENT: limited-time offer - claim at www.lockedin-business-spotlight.com",
    "Career meetup next week - RSVP opens Monday.",
    "URGENT: To claim your offer, verify your account at www.lockedin-secure-login.com"
]
for msg in messages:
    text = msg.lower()  # converts the message to lowercase for easier searching.
    label = " ✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_link and has_urgent: # checks if both conditions are true.
        label = " 🚨  Phishing"
    print(f"[{label}] {msg}")
print() # Space

# We can achieve the same result another way.
# Label urgent messages with links as phishing

username = "MagnumKPI"
messages = [
    "Special offer: Join our leadership webinar at www.lockedin.com/events",
    "URGENT: The deck for board meeting due by end of day",
    "Weekly digest: top posts from your network.",
    "New connection - view profile at www.lockedin.com/profiles/ajones",
    "Special offer: get Premium free for 1 month",
    "URGENT: limited-time offer - claim at www.lockedin-business-spotlight.com",
    "Career meetup next week - RSVP opens Monday.",
    "URGENT: To claim your offer, verify your account at www.lockedin-secure-login.com"
]
for msg in messages:
    text = msg.lower()  
    label = " ✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_urgent:
        if has_link:
        # Here, the program labels messages ah phishing only ig it meets both of the conditons has_link and has_urgent.
            label = " 🚨  Phishing"
    print (f"[{label}]{msg}")
print() # Space

"Nesting if y inside if x is equivalent to if x and y."

# Label urgent messages without links as starred

username = "MagnumKPI"
messages = [
    "Special offer: Join our leadership webinar at www.lockedin.com/events",
    "URGENT: The deck for board meeting due by end of day",
    "Weekly digest: top posts from your network.",
    "New connection - view profile at www.lockedin.com/profiles/ajones",
    "Special offer: get Premium free for 1 month",
    "URGENT: limited-time offer - claim at www.lockedin-business-spotlight.com",
    "Career meetup next week - RSVP opens Monday.",
    "URGENT: To claim your offer, verify your account at www.lockedin-secure-login.com"
]
for msg in messages:
    text = msg.lower()  
    label = " ✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_link:
        if has_urgent:
            label = " 🚨  Phishing"
    if has_urgent:
        if not has_link:
        #  check if a message does NOT have a link (not has_link) and IS urgent.
            label = " ⭐️  Starred"
    print(f"[{label}]{msg}") # This catches urgent messages without links.
print() # Space

# Label urgent messages with offers as spam, and non-urgent messages with offers as promos.

username = "MagnumKPI"
messages = [
    "Special offer: Join our leadership webinar at www.lockedin.com/events",
    "URGENT: The deck for board meeting due by end of day",
    "Weekly digest: top posts from your network.",
    "New connection - view profile at www.lockedin.com/profiles/ajones",
    "Special offer: get Premium free for 1 month",
    "URGENT: limited-time offer - claim at www.lockedin-business-spotlight.com",
    "Career meetup next week - RSVP opens Monday.",
    "URGENT: To claim your offer, verify your account at www.lockedin-secure-login.com"
]
for msg in messages:
    text = msg.lower()  
    label = " ✉️  Inbox"
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    if has_urgent:
        if has_offer:
            label = "⚠️ Spam"
    if not has_urgent:
        if has_offer:
            label = "💸 Promos"
    print(f"[{label}] {msg}")

"Nesting condtional statements helps express logic."