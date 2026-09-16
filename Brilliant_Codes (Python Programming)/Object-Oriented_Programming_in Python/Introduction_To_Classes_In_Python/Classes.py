"An agent needs a name and a style of communication. Make a helpful agent named Aria."

aria_name = "Aria"
aria_style = "helpful"

print(aria_name, "is a", aria_style, "agent") # Aria is a helpful agent

"Now, create two more agents, each with its own name and style."

rex_name = "Rex"
rex_style = "direct"

zig_name = "Zig"
zig_style = "cautious"

print(rex_name, "is a", rex_style, "agent")
print(zig_name, "is a", zig_style, "agent")

"Instead of using separate variables, we can bundle an agent's data by defining a class."
"Let's build one step by step. Start by naming the class Agent."

class Agent:
    pass # empty for now

print(Agent) # <class '__main__.Agent'>

class Agent2:
    def __init__ (self, name): # __init__ is the special method Python calls automatically whenever you create a new Agent.
        self.name = name

aria = Agent2("Aria")
rex = Agent2("Rex")
zig = Agent2("Zig")
print(aria.name, "is an agent")
print(rex.name, "is an agent")
print(zig.name, "is an agent")
# create three instances of the Agent class. Each time __init__ runs, self refers to the instance being created (aria, rex, or zig).

"A class describes a type of object that can have several instances. __init__ sets its attributes — variables that belong to it."

"Update the class definition to set an agent's communication style. Make aria helpful, rex direct, and zig cautious."

class Agent3:
    def __init__(self, name, style):
        self.name = name
        self.style = style

aria = Agent3("Aria", "helpful")
rex = Agent3("Rex", "direct")
zig = Agent3("Zig", "cautious")
print(aria.name, "is a", aria.style, "agent")
print(rex.name, "is a", rex.style, "agent")
print(zig.name, "is a", zig.style, "agent")

"This time, loop through all the agents to print each one's attributes."
"Make a friendly agent named Cora and a helpful agent named Gert. Loop through a list of all the instances to print the values of their attributes."
class Agent4:
    def __init__(self, name, style):
        self.name = name
        self.style = style

aria = Agent4("Aria", "helpful")
rex = Agent4("Rex", "direct")
zig = Agent4("Zig", "cautious")
cora = Agent4("Cora", "friendly")
gert = Agent4("Gert", "helpful")
for agent in [aria, rex, zig, cora, gert]:
    print(agent.name, "is a", agent.style, "agent")

"You defined a class to represent AI agents."
"In this course, you'll learn how to build and organize programs using classes, the foundation of object-oriented programming."