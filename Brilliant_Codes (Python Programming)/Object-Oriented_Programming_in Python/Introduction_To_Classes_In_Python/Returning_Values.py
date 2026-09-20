"Let's make our agents respond to queries from users."
"Make a direct agent named Maya and a helpful agent named Rolf. Upgrade Rolf to the premium tier."

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
    def change_style (self, new_style):
            if new_style in ["direct", "helpful", "friendly", "cautious"]:
                self.style = new_style
                print(self.name, "is now", self.style)
            else:
                print(new_style, "is not a valid style")
    def add_queries(self, amount):
            self.query_count += amount
            print(self.name, "has new query count:", self.query_count)
    "Write a method that takes a query as input and responds by returning 'Thinking...'. Test how each agent responds."
    def respond(self, query): # returns the string "Thinking..." for any input query and agent.
         return "Thinking..."


maya = Agent("Maya", "direct")
rolf = Agent("Rolf", "helpful")
rolf.premium = True
maya.report_status()
rolf.report_status()

# Status report for Maya
#  Style: direct
#  Gueries handled: 0
#  Free tier
# Status report for Rolf
#  Style: helpful
#  Gueries handled: 0
#  Premium tier

print() # Space
user_query = "What is the boiling point of water?"
print(f"User: {user_query}") # User: what is the boiling point of water?
print(f"{maya.name}: {maya.respond(user_query)}") # Maya: Thinking...
print(f"{rolf.name}: {rolf.respond(user_query)}") # Rolf: Thinking...
"Since methods are functions, they can return values."

"---------------------------------------------"


"If the agent is helpful and the query contains '?', make the response include 'Good question!''."

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
    def change_style (self, new_style):
            if new_style in ["direct", "helpful", "friendly", "cautious"]:
                self.style = new_style
                print(self.name, "is now", self.style)
            else:
                print(new_style, "is not a valid style")
    def add_queries(self, amount):
            self.query_count += amount
            print(self.name, "has new query count:", self.query_count)

    def respond(self, query): 

         "Let's limit the number of responses an agent will make without a premium subscription."
         "After a non-premium agent has responded to 3 queries, return a message that the limit has been reached, and don't update the query count."
         if not self.premium and self.query_count >= 3:
              return "Free tier limit reached."
                 
         "Update an agent's query count when it responds to a query. Test each agent on a list of queries."
         self.query_count += 1
         if self.style == "helpful" and "?" in query:
              return "Good question! Let me think."
         else:
              return "Thinking..."

print() # Space
maya = Agent2("Maya", "direct")
rolf = Agent2("Rolf", "helpful")
rolf.premium = True
user_query = "What is the boiling point of water?"
print(f"User: {user_query}") # What is the boiling point of water?
print(f"{maya.name}: {maya.respond(user_query)}") # Maya: Thinking...
print(f"{rolf.name}: {rolf.respond(user_query)}") # Rolf: Good question! Let me think.

print() # Space
user_queries = [
     "When is the equinox?",
     "Write a poen about cats",
     "Where is Papua?",
     "Are tomatoes vegetables?"
]
for user_query in user_queries:
    print(f"User: {user_query}")
    print(f"{maya.name}: {maya.respond(user_query)}")
    print(f"{rolf.name}: {rolf.respond(user_query)}") 
print("Queries handled:")
print(maya.name, maya.query_count)
print(rolf.name, rolf.query_count)

# User: When is the equinox?
# Maya: Thinking...
# Rolf: Good question! Let me think.
# User: Write a poen about cats
# Maya: Thinking...
# Rolf: Thinking...
# User: Where is Papua?
# Maya: Thinking...
# Rolf: Good question! Let me think.
# User: Are tomatoes vegetables?
# Maya: Thinking...
# Rolf: Good question! Let me think.
# Queries handled:
# Maya 5
# Rolf 5
     
"Methods make objects flexible: because they're functions, they can implement a wide variety of behaviors."
