"Let's add some methods to our agents for making updates."
"Create a helpful agent named Chet, and have it introduce itself and report its status."

class Agent:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0
    def introduce(self):
        if self.style == "helpful":
            print("Hi, I'm " + self.name + "!")
            print("How can I help you today?")
        elif self.style == "direct":
            print("I am", self.name)
            print("What do you want?")
        else:
            print("Hello, I'm",self.name)
    def report_status(self):
        print("Status report for", self.name)
        print(" Style:", self.style)
        print(" Gueries handled:", self.query_count)
        if self.premium:
            print(" Premium tier")
        else:
            print(" Free tier")

chet = Agent("Chet", "helpful")
chet.introduce()
chet.report_status()
print() # Space

# Hi, I'm Chet!
# How can I help you today?
# Status report for Chet
#  Style: helpful
#  Gueries handled: 0
#  Free tier

"Now, switch Chet's style to direct and report the status again."

chet = Agent("Chet", "helpful")
chet.introduce()
chet.report_status()
chet.style = "direct"
chet.report_status()
print() # Space

# # Hi, I'm Chet!
# How can I help you today?
# Status report for Chet
#  Style: helpful
#  Gueries handled: 0
#  Free tier
# Status report for Chet
#  Style: direct
#  Gueries handled: 0
#  Free tier

"Instead of updating the style directly, write a method that sets the style to direct."

class Agent2:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0
    def introduce(self):
        if self.style == "helpful":
            print("Hi, I'm " + self.name + "!")
            print("How can I help you today?")
        elif self.style == "direct":
            print("I am", self.name)
            print("What do you want?")
        else:
            print("Hello, I'm",self.name)
    def report_status(self):
        print("Status report for", self.name)
        print(" Style:", self.style)
        print(" Gueries handled:", self.query_count)
        if self.premium:
            print(" Premium tier")
        else:
            print(" Free tier")
    def make_direct(self):
        self.style = "direct" # The make_direct method sets the value of the agent's style to "direct".
        print(self.name, "is now direct")

chet = Agent2("Chet", "helpful")
chet.introduce()
chet.report_status()
chet.make_direct()
chet.report_status()
print() # Space

# Hi, I'm Chet!
# How can I help you today?
# Status report for Chet
#  Style: helpful
#  Gueries handled: 0
#  Free tier
# Chet is now direct
# Status report for Chet
#  Style: direct
#  Gueries handled: 0
#  Free tier
"Methods can update the attributes of an object."

"Let's improve our style update method to allow for direct, helpful, friendly, or cautious agents."
"Write a method to change the style to any valid style, or print a message if the style is invalid. Make Chet friendly."
class Agent3:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0
    def introduce(self):
        if self.style == "helpful":
            print("Hi, I'm " + self.name + "!")
            print("How can I help you today?")
        elif self.style == "direct":
            print("I am", self.name)
            print("What do you want?")
        else:
            print("Hello, I'm",self.name)
    def report_status(self):
        print("Status report for", self.name)
        print(" Style:", self.style)
        print(" Gueries handled:", self.query_count)
        if self.premium:
            print(" Premium tier")
        else:
            print(" Free tier")
    def make_direct(self):
        self.style = "direct" 
        print(self.name, "is now direct")

    def change_style (self, new_style):
        if new_style in ["direct", "helpful", "friendly", "cautious"]:
            self.style = new_style
            print(self.name, "is now", self.style)
        else:
            print(new_style, "is not a valid style")
    "Now that Chet is friendly, it's getting more queries."
    "Write a method that adds a given amount to an agent's query count. Update Chet with 5 new queries."

    def add_queries(self, amount):
        self.query_count += amount
        print(self.name, "has new query count:", self.query_count)

chet = Agent3("Chet", "helpful")
chet.report_status()
chet.change_style("friendly")
chet.report_status()

print() # Space

chet.add_queries(5)
chet.report_status()

# Status report for Chet
#  Style: helpful
#  Gueries handled: 0
#  Free tier
# Chet is now friendly
# Status report for Chet
#  Style: friendly
#  Gueries handled: 0
#  Free tier

# Chet has new query count: 5
# Status report for Chet
#  Style: friendly
#  Gueries handled: 5
#  Free tier

"When attributes are set using class methods, the class definition controls the updating process, so it can prevent unwanted changes."