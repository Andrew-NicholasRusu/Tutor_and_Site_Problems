"Let's improve the message labeling feature."

# Label urgent messages with links as phishing. Star urgent messages without links.

username = "Intern4eva"
messages = [
    "URGENT: verify your credentials at www.lockedin-secure-login.net",
    "URGENT: claim your offer at www.lockedin-leadersummit.com",
    "URGENT: exclusive offer - boost your company page visibility today!",
    "URGENT: special offer - upgrade to Premium Business before midnight!",
    "See this week's trending posts at www.lockedin.com/trending",
    "Your monthly analytics report is ready to download.",
    "Special offer: get 30 days of Premium Insights free!",
    "Team reminder: submit your goals for next quarter.",
    "URGENT: update your slides before the end of the day."
]
for msg in messages:
    text = msg.lower()
    label = "✉️ Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_urgent:
        if has_link:
            label = "🚨 Phishing"
        else: 
            label = "⭐️ Starred"
    print(f"[{label}]{msg}")
print() # Space

# Label non-urgent messages as "Link" when they contain a link, or as "inbox" when they don't. 

username = "Intern4eva"
messages = [
    "URGENT: verify your credentials at www.lockedin-secure-login.net",
    "URGENT: claim your offer at www.lockedin-leadersummit.com",
    "URGENT: exclusive offer - boost your company page visibility today!",
    "URGENT: special offer - upgrade to Premium Business before midnight!",
    "See this week's trending posts at www.lockedin.com/trending",
    "Your monthly analytics report is ready to download.",
    "Special offer: get 30 days of Premium Insights free!",
    "Team reminder: submit your goals for next quarter.",
    "URGENT: update your slides before the end of the day."
]
for msg in messages:
    text = msg.lower()
    label = "✉️ Inbox"
    has_link = "www" in text
    has_urgent = "urgent" in text
    if has_urgent:
        if has_link:
            label = "🚨 Phishing"
        else: 
            label = "⭐️ Starred"
    else:
        if has_link:
            label = "🔗 Link"
        else:
            label = "✉️ Inbox"
    print(f"[{label}]{msg}")
print() # Space


"Nesting if-else statements can help cover all possible cases."

# Label urgent offers as spam, and non-urgent offers as promos. Star urgent messages without offers.

username = "Intern4eva"
messages = [
    "URGENT: verify your credentials at www.lockedin-secure-login.net",
    "URGENT: claim your offer at www.lockedin-leadersummit.com",
    "URGENT: exclusive offer - boost your company page visibility today!",
    "URGENT: special offer - upgrade to Premium Business before midnight!",
    "See this week's trending posts at www.lockedin.com/trending",
    "Your monthly analytics report is ready to download.",
    "Special offer: get 30 days of Premium Insights free!",
    "Team reminder: submit your goals for next quarter.",
    "URGENT: update your slides before the end of the day."
]
for msg in messages:
    text = msg.lower()
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    if has_offer: # checks if the message has an offer.
        if has_urgent:
            label = "⚠️ Spam"
        else:
            label = "💸 Promos" 
    else:
        if has_urgent:
            label = "⭐️ Starred"
        else:
            label = "✉️ Inbox"
    print(f"[{label}]{msg}")
print() # Space
        
# Let's program the same feature in a different way.
# Label urgent offers as spam, and non-urgent offers as promos. Start urgent messages without offers.

username = "Intern4eva"
messages = [
    "URGENT: verify your credentials at www.lockedin-secure-login.net",
    "URGENT: claim your offer at www.lockedin-leadersummit.com",
    "URGENT: exclusive offer - boost your company page visibility today!",
    "URGENT: special offer - upgrade to Premium Business before midnight!",
    "See this week's trending posts at www.lockedin.com/trending",
    "Your monthly analytics report is ready to download.",
    "Special offer: get 30 days of Premium Insights free!",
    "Team reminder: submit your goals for next quarter.",
    "URGENT: update your slides before the end of the day."
]
for msg in messages:
    text = msg.lower()
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    if has_urgent:
        if has_offer:
            label = "⚠️ Spam"
        else:
            label = "⭐️ Starred"
    else:
        if has_offer:
            label = "💸 Promos"
        else:
            label = "✉️ Inbox"
    print(f"[{label}]{msg}")
print() # Space

# Users tend to prefer this labling style, but it doesn't flag phishing.
# Label urgent messages with links as phishing. Otherwise, label them as spam or starred as before.

username = "Intern4eva"
messages = [
    "URGENT: verify your credentials at www.lockedin-secure-login.net",
    "URGENT: claim your offer at www.lockedin-leadersummit.com",
    "URGENT: exclusive offer - boost your company page visibility today!",
    "URGENT: special offer - upgrade to Premium Business before midnight!",
    "See this week's trending posts at www.lockedin.com/trending",
    "Your monthly analytics report is ready to download.",
    "Special offer: get 30 days of Premium Insights free!",
    "Team reminder: submit your goals for next quarter.",
    "URGENT: update your slides before the end of the day."
]
for msg in messages:
    text = msg.lower()
    has_urgent = "urgent" in text
    has_offer = "offer" in text
    has_link = "www" in text
    # This triple-nested structure first checks if messages have offers, then if they're urgent, and finally if they have links.
    if has_offer:
        if has_urgent:
            if has_link:
                label = "🚨 Phishing"
            else:
                label = "⚠️ Spam"
            # labels urgent messages with offers: those with links are phishing, others are spam.
        else: 
            label = "💸 Promos"
    else:
        if has_urgent:
            if has_link:
                label = "🚨 Phishing"
            else:
                label = "⭐️ Starred"
            #  labels urgent messages without offers: those with links are phishing, others are starred.
        else:
            label = "✉️ Inbox"
    print(f"[{label}]{msg}")

"Nesting conditional statements can help cover all the logical cases"
