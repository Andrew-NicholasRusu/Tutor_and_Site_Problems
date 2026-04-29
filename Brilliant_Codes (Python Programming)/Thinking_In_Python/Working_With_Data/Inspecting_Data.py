"Lets look for spambots - acounts that automate sending spam - by tracking messages that have been sent multiple times."

# Count the number of tiems each message text was sent.

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
text_counts = {} #  initializes an empty dictionary.
for message in message_log:
    print(f"Processig messages...")
    text = message["text"]
    if text not in text_counts: # checks if the text is not yet in the dictionary.
        text_counts[text] = 0 #  initializes the count to 0
    text_counts[text] += 1 # increments the count for each text.
# print first 3 text counts...
print("First 3 text counts:")
for text, count in list(text_counts.items())[:3]:
    print(f"Message text:{text}")
    print(f"Times sent: {count}")
print() # Space

# Build a dictionary. For each message text, compile a list of the users who sent it. 

text_counts = {}
text_senders = {} #  initializes an empty dictionary for sender lists. 
for message in message_log:
    text = message["text"]
    sender = message["sender"]
    if text not in text_counts:
        text_counts[text] = 0
        text_senders[text] = [] #  initializes an empty list for each new text.
    text_counts[text] += 1
    if sender not in text_senders[text]: # checks if the sender is not already in the list.
        text_senders[text].append(sender) # appends the sender to the list.
        print("new sender:", sender)
# print first 3 text counts...
print("First 3 text counts:")
for text, senders in list(text_senders.items())[:3]:
    print(f"Message text:{text}")
    print(f"Times sent: {senders}")
print() # Space

# BUild a list of dictionaries to store information about repeated messages. Store the text, times sent, sender list, and number of senders in each dictionary.

text_counts_2 = {
    "please schedule a sync with marketing for next week.": 1, 
    "exclusive deal: unlock you potential with this limited offer!": 1,
    "how are you doing today?": 5,
    # continued...
    }
text_senders_2 = {
    "please schedule a sync with marketing for next week.": ["chiefOfStuff"],
    "exclusive deal: unlcok your potential with this limited offer!":["rubiksCubicle"],
    # continued...
    }
repeat_log = [] #  initializes an empty list for the repeated message dictionaries.
for text, count in text_counts.items():
    if count > 1: # filters for messages sent more than once. 
        senders = text_senders[text] # gets the sender list.
        repeat = {}
        repeat["text"] = text
        repeat["times_sent"] = count
        repeat["senders"] = senders
        repeat["num_senders"] = len(senders)
        # builds a dictionary with four fields. 
        repeat_log.append(repeat) # appends the dictionary to the list of dictionaries.
        # print updates...
        print(f"📑 Repeated message: {text}")
        print(f"Sent {repeat["times_sent"]} times")
        print(f"Distinct senders: {repeat["num_senders"]}")
print() # Space

"A single dictionary can store data in many different forms."

# A spambot will often send the same message multiple times. Print only the texts of messages that were sent multiple times by the same sender.

repeat_log = [
    {'text': 'how are you doing today?', 'times_sent': 5, 'senders': ['ExecEnvy', 'Micr0_Mngr', 'rubiksCubicle'], 'num_senders': 3},
    {'text': 'enhance your workflow with this upgrade.', 'times_sent': 3, 'senders': ['SynergizerBunny'], 'num_senders': 1}, 
    {'text': 'can someone proofread the executive summary before we send it?', 'times_sent': 2, 'senders': ['vpOfVibes'], 'num_senders': 1},
    {'text': 'happy birthday!', 'times_sent': 3, 'senders': ['entrepreNerd', 'middlingManager', 'EmilyVP'], 'num_senders': 3}
    ]
print("messages sent multiple times by the same sender:")
for repeat in repeat_log: # iterates over each repeat record.
    text = repeat["text"]
    num_senders = repeat["num_senders"]
    times_sent = repeat["times_sent"] # extract the three relevant values.
    if num_senders < times_sent: # checks if the number of distinct senders is less than times sent, meaning at least one sender must have sent it multiple times.
        print(f"📑 {text}")
print() # Space

"Since they can contain many different types of information, dictionaries are versatile tools for storing data."



