"Let's explore how the sie of the message log affects the computational work programs do."

# Find the greatest difference between any two timestamps.

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
first_msg = msg_log[0]
last_msg = msg_log[-1] # The program only accesses msg_log[0] and msg_log[-1], which are fixed-position lookups.
# The first message has the smallest timestamp and the last message has the largest, 
# so msg_log[0] and msg_log[-1] give us the timestamps with the greatest difference. 
first_time = first_msg["timestamp"]
last_time = last_msg["timestamp"]
max_diff = last_time - first_time # Subtracting the smaller from the larger gives a positive result.
print(f"Max difference: {max_diff}")
print() # SPACE
# It doesn't loop through the list, so adding more messages doesn't change how many operations it performs.

# Count the number of messages sent by "Intern4eva"

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
num_messages = 0
for msg in msg_log: # Initialize num_messages to 0, then loop through msg_log.
    # The loop iterates through every message in msg_log. With 1000 messages, the loop runs 1000 times, performing many more operations than with 9 messages.
    sender = msg["sender"]
    print(f"Message from; {sender}")
    if sender == "Intern4eva": # For each message, check if the sender equals "Intern4eva" and increment the counter when it matches.
        num_messages += 1
print(f"Number of messages sent by 'Intern4eva': {num_messages}")

"For some programs, the runtime depends on the size of the data structure it processes."
"Understanding how computational work depends on data is the first step to writing efficient programs."
