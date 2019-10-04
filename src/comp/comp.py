# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print('\n')

print("Starts with D:")
a = []

for i in humans:
    if 'D' in i.name[0]:
        a.append(i.name)

print(a)
print('\n')

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for i in humans:
    if 'e' in i.name[len(i.name)-1]:
        b.append(i.name)

print(b)
print('\n')

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

letters = ['C','D','E','F','G']
for i in humans:
    for l in letters:
        if l in i.name[0]:
            c.append(i.name)

print(c)
print('\n')

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for i in humans:
    d.append(i.age + 10)

print(d)
print('\n')

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for i in humans:
    e.append(f'{i.name}-{i.age}')

print(e)
print('\n')

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for i in humans:
    if i.age > 27 and i.age <= 32:
        f.append((i.name, i.age))

print(f)
print('\n')

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for i in humans:
    g.append(Human(i.name.upper(), (i.age + 5)))

print(g)
print('\n')

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []

for i in humans:
    h.append(math.sqrt(i.age))

print(h)
print('\n')
