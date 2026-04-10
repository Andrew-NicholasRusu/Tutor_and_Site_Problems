"Let's continue working on the message labeling feature"

# Label urgent messages with links as phishing,
username = "ChiefLatteOfficer"
messages = [
    "URGENT: verify your login at www.lockedin-secure-access.com",
    "URGENT: confirm participation at www.lockedin-conference-checkin.com",
    "Special offer: unlock recruiter insights for your team!",
    "URGENT: exclusive offer - boost your company page visibility now!",
    "Team update: project milestones and new hires this week.",
    "Connection request - see who viewed your profile at www.lockedin.com/viewers",
    "Special offer: try Premium Insights free for 7 days!",
    "URGENT: finalize your limited-time offer at www.lcokedin-business-plus.com",
    "Event reminder: company town hall starts in one hour."
]
for msg in messages:
    text = msg.lower()
    label = "✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_link: # checks if has_link is True. When it is, next line checks if has_urgent is also True.
        if has_urgent:
            label = "🚨 Phishing" # Sets to phishing if both are true.
    print(f"[{label}]{msg}")
print() # Space

# Make a "Link" label for messages that have links but aren't urgent.

username = "ChiefLatteOfficer"
messages = [
    "URGENT: verify your login at www.lockedin-secure-access.com",
    "URGENT: confirm participation at www.lockedin-conference-checkin.com",
    "Special offer: unlock recruiter insights for your team!",
    "URGENT: exclusive offer - boost your company page visibility now!",
    "Team update: project milestones and new hires this week.",
    "Connection request - see who viewed your profile at www.lockedin.com/viewers",
    "Special offer: try Premium Insights free for 7 days!",
    "URGENT: finalize your limited-time offer at www.lcokedin-business-plus.com",
    "Event reminder: company town hall starts in one hour."
]
for msg in messages:
    text = msg.lower()
    label = "✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_link: 
        if has_urgent:
            label = "🚨 Phishing"
        else:
            label = "🔗 Link"
# Here, the two branches of the nested if-else statement describe different scenarios of messages
# that contain links - whether they're urgent or not.
    print(f"[{label}]{msg}")
print() # Space

"An if-else statement can be nexted in an if statement."

# Label urgent messages with links as phishing

username = "ChiefLatteOfficer"
messages = [
    "URGENT: verify your login at www.lockedin-secure-access.com",
    "URGENT: confirm participation at www.lockedin-conference-checkin.com",
    "Special offer: unlock recruiter insights for your team!",
    "URGENT: exclusive offer - boost your company page visibility now!",
    "Team update: project milestones and new hires this week.",
    "Connection request - see who viewed your profile at www.lockedin.com/viewers",
    "Special offer: try Premium Insights free for 7 days!",
    "URGENT: finalize your limited-time offer at www.lcokedin-business-plus.com",
    "Event reminder: company town hall starts in one hour."
]
for msg in messages:
    text = msg.lower()
    label = "✉️  Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_urgent:
        if has_link:
            label = "🚨 Phishing"
        else:
            label = "⭐️ Starred"
    print(f"[{label}]{msg}")
print() # Space

# Label urgent offers as spam. Star urgent messages without offers.

username = "ChiefLatteOfficer"
messages = [
    "URGENT: verify your login at www.lockedin-secure-access.com",
    "URGENT: confirm participation at www.lockedin-conference-checkin.com",
    "Special offer: unlock recruiter insights for your team!",
    "URGENT: exclusive offer - boost your company page visibility now!",
    "Team update: project milestones and new hires this week.",
    "Connection request - see who viewed your profile at www.lockedin.com/viewers",
    "Special offer: try Premium Insights free for 7 days!",
    "URGENT: finalize your limited-time offer at www.lcokedin-business-plus.com",
    "Event reminder: company town hall starts in one hour."
]
for msg in messages:
    text = msg.lower()
    label = "✉️  Inbox"
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    if has_urgent:
        if has_offer:
            label = "⚠️ Spam"
        else:
            label = "⭐️ Starred"
    print(f"[{label}]{msg}")
print() # Space

# Label urgent offers as spam, and non-urgent offers as promos. 

username = "ChiefLatteOfficer"
messages = [
    "URGENT: verify your login at www.lockedin-secure-access.com",
    "URGENT: confirm participation at www.lockedin-conference-checkin.com",
    "Special offer: unlock recruiter insights for your team!",
    "URGENT: exclusive offer - boost your company page visibility now!",
    "Team update: project milestones and new hires this week.",
    "Connection request - see who viewed your profile at www.lockedin.com/viewers",
    "Special offer: try Premium Insights free for 7 days!",
    "URGENT: finalize your limited-time offer at www.lcokedin-business-plus.com",
    "Event reminder: company town hall starts in one hour."
]
for msg in messages:
    text = msg.lower()
    label = "✉️  Inbox"
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    if has_offer:
        if has_urgent:
            label = "⚠️ Spam"
        else:
            label = "💸 Promos"
    print(f"[{label}]{msg}")
print() # Space

"Nesting conditional statements makes it possible to layer logical steps."