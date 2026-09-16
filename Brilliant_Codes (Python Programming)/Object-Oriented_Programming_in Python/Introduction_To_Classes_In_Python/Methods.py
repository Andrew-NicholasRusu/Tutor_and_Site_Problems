"Let's give our agents some actions they can perform."
"Create two Agent instances: a helpful agent named Cora, and a direct agent named Gert."

class Agent:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0

cora = Agent("Cora", "helpful")
gert = Agent("Gert", "direct")
print(cora.name, "is an agent") # Cora is an agent
print(gert.name, "is an agent") # Gert is an agent
print() # Space

"Instead of printing the object's attributes, let's define a method so an agent can introduce itself."
"Make the introduce method print the object's name."

class Agent2:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0
    def introduce(self): # calls the introduce method. 
        print("Hello, I'm", self.name)

cora = Agent2("Cora", "helpful")
gert = Agent2("Gert", "direct")
cora.introduce() # Hello, I'm Cora
gert.introduce() # Hello, I'm Gert
# Python automatically passes the object before the dot (cora or gert) as the self input.
print() # Space

"Methods are functions attached to a class that define tasks an object can perform."

"Customize the introductions for helpful and direct agents."

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
            print("I am ", self.name + ".")
            print("What do you want?")
        else:
            print("Hello, I'm" , self.name)

cora = Agent3("Cora", "helpful")
gert = Agent3("Gert", "direct")
cora.introduce()
gert.introduce()
print() # Space

"This time, write a method that reports an agent's current attributes."

class Agent4:
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
            print("I am ", self.name + ".")
            print("What do you want?")
        else:
            print("Hello, I'm" , self.name)
    def report_status(self):
        print("Status report for", self.name)
        print(" Style:", self.style)
        print(" Queries handled:", self.query_count)
        if self.premium:
            print(" Premium tier")
        else:
            print(" Free tier")

cora = Agent4("Cora", "helpful")
gert = Agent4("Gert", "direct")
cora.report_status()
gert.report_status()
print() # Space

# Status report for Cora
#  Style: helpful
#  Queries handled: 0
#  Free tier
# Status report for Gert
#  Style: direct
#  Queries handled: 0
#  Free tier

"Gert has not been popular with users. Change its name to Gertie and make it friendly, then report its status."

gert.name = "Gertie"
gert.style = "friendly"
gert.report_status()
print() # Space

# Status report for Gertie
#  Style: friendly
#  Queries handled: 0
#  Free tier

"The updated Gertie is now more popular. Simulate it handling three queries, and report its final status."

user_queries = [
    "Tell me a joke",
    "CAn all birds swim?",
    "Is it going to rain?"
]
for user_query in user_queries:
    print("User:", user_query)
    print(gert.name + ": Thinking...")
    gert.query_count += 1
gert.report_status()

# User: Tell me a joke
# Gertie: Thinking...
# User: CAn all birds swim?
# Gertie: Thinking...
# User: Is it going to rain?
# Gertie: Thinking...
# Status report for Gertie
#  Style: friendly
#  Queries handled: 3
#  Free tier

"You wrote methods to add functionality to the Agent class."
"Combining state (attributes) and behavior (methods) into objects is a central theme in object-oriented programming."