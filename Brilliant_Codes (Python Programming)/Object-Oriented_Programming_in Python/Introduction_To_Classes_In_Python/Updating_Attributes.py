"Let's update an agent's attributes as conditions change."
"Change Zig's style to friendly."

class Agent:
    def __init__(self, name, style):
        self.name = name
        self.style = style

aria = Agent("Aria", "helpful")
rex = Agent("Rex", "direct")
zig = Agent("Zig", "cautious")
zig.style = "friendly" # changes Zig's style to friendly
for agent in [aria, rex, zig]:
    print(agent.name, agent.style)
print() # Space

"Add an attribute called premium to flag when an agent is serving a premium subscription. "
"Every new agent should start out on the free (non-premium) tier."

class Agent2:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False

aria = Agent2("Aria", "helpful")
rex = Agent2("Rex", "direct")
zig = Agent2("Zig", "cautious")
zig.style = "friendly"
for agent in [aria, rex, zig]:
    print(agent.name, agent.style, agent.premium)
print() # Space

# Aria helpful False
# Rex direct False
# Zig friendly False

"Upgrade Rex to a premium instance."

rex.premium = True # updates the rex instance.
for agent in [aria, rex, zig]:
    print(agent.name, agent.style, agent.premium)
print() # Space

# # Aria helpful False
# Rex direct True
# Zig friendly False

"Each instance of a class has its own attributes. Updating one instance doesn't affect the others."

"An agent should track how many user queries it has handled. Add a query count attribute that starts at zero."

class Agent3:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.premium = False
        self.query_count = 0

aria = Agent3("Aria", "helpful")
rex = Agent3("Rex", "direct")
zig = Agent3("Zig", "cautious")
zig.style = "friendly"
rex.premium = True
for agent in [aria, rex, zig]:
    print(agent.name, agent.style, agent.premium, agent.query_count)
print() # Space

# Aria helpful False 0
# Rex direct True 0
# Zig friendly False 0

"Aria just handled a user query. Update the appropriate attribute."

aria.query_count += 1
for agent in [aria, rex, zig]:
    print(agent.name, agent.style, agent.premium, agent.query_count)
print() # Space

# Aria helpful False 1
# Rex direct True 0
# Zig friendly False 0

"Zig handles 5 user queries in a row. Simulate this by updating the appropriate attribute in a loop."

user_queries = [
    "What is the capital of Italy?",
    "How do I tie a shoe",
    "Are frogs reptiles",
    "Where is the nearest car wash",
    "Should I drive or wal to it"
]
for user_query in user_queries:
    print("User:", user_query)
    print("Zig: Thinking...")
    zig.query_count += 1
for agent in [aria, rex, zig]:
    print(agent.name, agent.style, agent.premium, agent.query_count)

# User: What is the capital of Italy?
# Zig: Thinking...
# User: How do I tie a shoe
# Zig: Thinking...
# User: Are frogs reptiles
# Zig: Thinking...
# User: Where is the nearest car wash
# Zig: Thinking...
# User: Should I drive or wal to it
# Zig: Thinking...
# Aria helpful False 1
# Rex direct True 0
# Zig friendly False 5

"You updated some attributes of different instances of the Agent class."
"Classes make it possible to create several similar objects, each with its own properties."


