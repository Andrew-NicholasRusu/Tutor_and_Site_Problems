"Let's format the security labels on messages."

# Print the message with an Inbox label enclosed in square brackets, [ and ].

username = "DigitalHomebody"
message = "Can you review the project notes before our meeting?" 
label = "Inbox"
print("[", label, "]", message)
print() # Space

# The comma in a print statement inserts a space. The = operator puts strings together without spaces.
# Enclose the label in square brackets without spaces, but keep the space between the label and the message. 

username = "DigitalHomebody"
message = "Can you review the project notes before our meeting?" 
label = "Inbox"
print("[" + label + "]", message) # uses the + operator to concatenate strings without spaces. 
# "[" + label + "]" creates [✉️ Inbox] with no spaces. 
# Then , message adds the message with a space separator. 
# The output is [✉️ Inbox] Can you review....
print() # Space

# Print the label and message using a formatted string.

username = "DigitalHomebody"
message = "We sent you the terms of our offer. Response requested."
label = "Inbox"
print (f"[{label}] {message}") # uses an f-string (formatted string) which starts with f before the opening quote. 
# Inside the f-string, curly braces {} are used to insert variable values. {label} inserts the value of label, 
# and {message} inserts the value of message.
print() # Space

"A formatted string, or f-string, fills in variable values wherever you place {} iin the string."

# Include sneder information in the printed message. Also, if the message is urgent and has a link, change its label to "Phishing".
username = "DigitalHomebody"
message = "Urgent password reset required: www.mymail-userserivce.com"
label_emoji = "✉️"
label_text = "Inbox"
sender = "GrowthSlacker84"
from_string = f"From: {sender}" # uses an f-string to create the sender info.

text = message.lower() # converts the message to lowercase. 
if "urgent" in text and "www" in text:
    label_emoji = "🚨 "
    label_text = "Phishing"
label = f"{label_emoji}{label_text}" # creates the label using an f-string. 
print(f"[{label}][{from_string}]{message}") # prints everything using an f-string with multiple variables.

"Python's f-strings are frequently used to customize program output."
