"Let's analyze how fast runtime grows when the message log grows."

# Count the number of messages that have attachments

msg_log = [
    {
        "text": "can you send me a quick update before close of day",
        "sender": "WFHomie",
        "recipient": "ChiefOfStuff",
        "attachments": [],
        "timestamp": 598267,
        "status": "Not set"
    },
    {
        "text": "hey, try opening this when you get a second",
        "sender": "ExecEnvy",
        "recipient": "rubiksCubicle",
        "attachments": ["meeting_minutes.scr"],
        "timestamp": 600136,
        "status": "Not set"
    },
    {
        "text": "run these for me and tell me what you see",
        "sender": "ScroogMakeDeck",
        "recipient": "Micr0_Mngr",
        "attachments": ["stx99p.exe", "runme.bat"],
        "timestamp": 600834,
        "status": "Not set",
    },
    {
        "text": "lunch on friday if you're free",
        "sender": "Intern4eva",
        "recipient": "VeePeeWee",
        "attachments": [],
        "timestamp": 612887,
        "status": "Not set"
    },
    {
        "text": "i'm sending the setup just in case",
        "sender": "PusherOfPaper",
        "recipient": "rubiksCubicle",
        "attachments": ["printer_setup.msi"],
        "timestamp": 623710,
        "status": "Not set"
    },
    {
        "text": "found this pack online, might help with your project",
        "sender": "rubiksCubicle",
        "recipient": "ExecEnvy",
        "attachments": ["coupon.zip", "readme.txt", "avatar.png"],
        "timestamp": 635451,
        "status": "Not set"
    },
    {
        "text": "here's the backup and the instructions i mentioned",
        "sender": "Micr0_Mngr",
        "recipient": "PusherOfPaper",
        "attachments": ["instructions.pdf", "backup.zip"],
        "timestamp": 645363,
        "status": "Not set"
    },
    {
        "text": "here's the backup and the instructions i mentioned",
        "sender": "Micr0_Mngr",
        "recipient": "ChiefOfStuff",
        "attachments": ["instructions.pdf", "backup.zip"],
        "timestamp": 645363,
        "status": "Not set"
    },
    {
        "text": "attached are a few things for you to review", 
        "sender": "VeePeeWee",
        "recipient": "Intern4eva",
        "attachments": ["notes.pdf", "agenda.docx", "funnycat.jpg"],
        "timestamp": 652343,
        "status": "Not set"
    }
    ]
iterations = 0
count = 0 # Initialize count = 0 before the loop.
for msg in msg_log: # Use for to iterate through each message. 
    # Update iterations...
    iterations += 1
    print(f"Iterations: {iterations}")
    attachments = msg["attachments"]
    if len(attachments) > 0: # Check if len(attachments) > 0 to find messages with attachments, 
        count += 1 # and count += 1 to increment the counter.
print(f"Found {count} messages")
print() # SPACE

# Big-O notations is a common way to describe a program's time complexity. If n is the size of the data, then functions like 1, 
# n, or n^2 describe how the runtime grows as the data grows.

# What's the worst-case time complexity of this program?
found = False
for i in range (len(msg_log) - 1):
    j = i + 1
    msg1 = msg_log[i]
    msg2 = msg_log[j]
    time1 = msg1["timestamp"]
    time2 = msg2["timestamp"]
    if time1 == time2:
        found = True
        same_time = time1
        break
# Answer: Linear time

# What's the worst-case time complexity of this program?
last_msg = msg_log[-1]
last_time = last_msg["timestamp"]
any_after = last_time >= 628193
print(any_after)
# Answer: Constant time

# What's the worst-case time complexity of this program?
for i in range(len(msg_log)):
    for j in range(len(msg_log)):
        msg1 = msg_log[i]
        msg2 = msg_log[j]
        text1 = msg1["text"]
        text2 = msg2["text"]
        if i < j and text1 == text2:
            print(f"Duplicated: {text1}")
# Answer: Quadratic time

"Describing program performance with Big-O is the key to recognizing and writing more efficient programs."