"Let's find out which users are sending the same message repeatedly. They might be spambots."

# For every message in the dataset, add a key that combines the sender and message text into a single string.

message_log = [
    {"text":
     "please shcedule a sync with marketing for next week.", 
     "sender": "chiefOfStuff", "recipient": "WFHomie", "folder":
     "✉️ Inbox", "timestamp": 210685},
    {"text":
      "exclusive deal: unlock your potential with this limited offer!",
      "sender": "rubiksCubicle", "recipient": "chiefOfStuff", 
      "folder": "⚠️ Spam", "timestamp": 211571},
    {"text": "how are you doing today?", "sender": "ExecEnvy",
     "recipient": "chiefOfStuff", "folder": "✉️  Inbox",
     "timestamp": 212631},
     ## 65 more rows...     
    ]
for message in message_log:
    text = message["text"]
    sender = message["sender"]
    # extract the text and sender fields. 
    sender_text = f"{sender}:{text}" # creates a composite key by combining sender and text with a colon.
    message["sender_text"] = sender_text #  adds this new field to the message dictionary.
    print(message["sender_text"])
    # Two messages will have the same sender_text value only if they have the same text were sent by the same user.
print() # SPACE
print(message_log)
print() # SPACE

"Combining tow keys into one can account for two factors at once."

# Count the number of times each sender/text combo occurs in the data set.

sender_text_counts = {} # initializes an empty dictionary.
for message in message_log:
    sender_text = message["sender_text"] # extracts the sender_text field. 
    if sender_text not in sender_text_counts: # checks if it's not in the dictionary yet.
        sender_text_counts[sender_text] = 0 # initializes the count to 0.
    sender_text_counts[sender_text] += 1 # increments the count for each occurrence.
    print(sender_text)
    print("Times found:", sender_text_counts[sender_text])
print() # Space

# Accounts that send the same message multiple times are suspected spambots. Make a list of suspects.

sender_text_counts = {}
suspects = [] #  initializes an empty list for suspects. 
for message in message_log:
    sender = message["sender"] #  extracts the sender from the message. 
    sender_text = message["sender_text"] # gets the sender_text field.
    if sender_text not in sender_text_counts: # counts occurrences.
        sender_text_counts[sender_text] = 0 # counts occurrences.
    sender_text_counts[sender_text] += 1 # counts occurrences.
    print("Checking", sender)
    if sender_text_counts[sender_text] == 2: # checks if the count reached 2 (meaning a user sent the same message multiple times).
        suspects.append(sender) # If so, this line appends the sender to the suspects list.
        print(f"🚨 New suspect: {sender} 🚨")
print("Suspects:", suspects)
print() # Space

# Now let's use the spammer log that we built in a previous lesson to flag accounts that behave like spambots.
# Flag spammers if they are suspects and send more than 50 percent spam.

suspects = [
    "rubiksCubicle",
    "SynergizerBunny",
    "vpOfVibes"
    ]
spammer_log = [
    {"username": "rubiksCubicle", "spam_count": 7, "msg_count": 10, "spam_percent": 70.0},
    {"username": "SynergizerBunny", "spam_count": 5, "msg_count": 5, "spam_percent": 100.0},
    {"username": "ExecEnvy", "spam_count": 6, "msg_count": 9, "spam_percent": 66.66666666666},
    {"username": "ExecuTroll_404", "spam_count": 3, "msg_count": 3, "spam_percent": 100.0},
    {"username": "cheifOfStuff", "spam_count": 1, "msg_count": 3, "spam_percent": 33.3333333333},
    {"username": "VeePeeWee", "spam_count": 1, "msg_count": 1, "spam_percent": 100.0},
    {"username": "MagnumKPI", "spam_count": 1, "msg_count": 1, "spam_percent": 100.0},
    {"username": "entrepreNerd", "spam_counts": 3, "msg_count": 11, "spam_percent": 27.2727272727272727272},
    ]
print("🤖 PROBABLE SPAMBOTS 🤖")
for spammer in spammer_log: #  loops through each spammer record.
    username = spammer["username"]
    spam_percent = spammer["spam_percent"]
    # extract the username and spam_percent fields.
    if username in suspects and spam_percent > 50: #  checks two conditions: the username must be in the suspects list AND spam_percent must be greater than 50. 
    # This identifies probable spambots.
        print(username)
print() # Space

"Complex data analysis often requires building and inspecting lists of dictionaries."


