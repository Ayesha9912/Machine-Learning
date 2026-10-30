# Strings are very helpful in real-world projects
# A string is a sequence of characters
# In Python, strings are sequences of Unicode characters

# - Creating strings
# - Accessing strings
# - Adding characters to strings
# - Editing strings
# - Deleting strings
# - Operations on strings
# - String functions


# ---------- Creating ----------
print("hello")
print("""hello""")


# ---------- Accessing substrings ----------
# Concept of indexing
c = 'hello'
print(c[0])      # h

# Types of indexing
# - Positive indexing
# - Negative indexing

print(c[-2])     # l  (useful to get the last values of a string
                 #     when you don't know its length)


# ---------- Slicing ----------
# Slicing gets one or more characters: c[start:stop:step]
print('slicing', c[0:3])     # hel
print('new', c[0:5:4])       # ho
print(c[0:3:-2])             # '' (empty: with a positive range, don't use a negative step)

c = 'hello'

print(c[0:3:1])   # hel   (every character from 0 to 2)
print(c[0:3:2])   # hl    (indexes 0, 2)
print(c[0:5:3])   # hl    (indexes 0, 3)
print(c[::-1])    # olleh (negative step reverses the string)


s = 'programming'

print(s[0:4])        # prog
print(s[2:8:2])      # orm
print(s[::3])        # pgmn
print(s[3:])         # gramming
print(s[:5])         # progr
print(s[::-2])       # gimrop
print(s[-3:])        # ing
print(s[1:9:4])      # ra
print(s[8:2:-2])     # imr
print(s[-1:-6:-1])   # gnimm


# ---------- Editing and deleting ----------
r = "heloo"

try:
    r[0] = 'x'   # strings are immutable, this raises TypeError (very important)
except TypeError as e:
    print('Error:', e)

# Immutable means we can't change the string in place.
# We can only reassign the variable to a new string.
r = 'x' + r[1:]
print(r)         # xeloo

# Deletion
try:
    del r[2]     # we cannot delete single characters
except TypeError as e:
    print('Error:', e)

del r            # but we can delete the whole variable
try:
    print(r)
except NameError as e:
    print('Error:', e)   # name 'r' is not defined, because it was deleted


# ---------- Operations on strings ----------
# - Arithmetic operators
# - Relational operators
# - Logical operators
# - Looping on strings
# - Membership operators

# Arithmetic: concatenation
r = 'hello' + ' ' + 'world'
print('concatenation', r)

# String multiplication
print("*" * 59)
print('hell' * 4)


# Relational operators (compared lexicographically, like a dictionary)
print("hello" == "world")   # False
print("america" > "india")  # False, 'a' comes before 'i'
print("kol" < "Kol")        # False, lowercase letters have bigger Unicode values than uppercase


# Logical operators
print(bool("hell"))         # True  (non-empty string is truthy)
print(bool(""))             # False (empty string is falsy)

print("hell" and '')        # ''      (left truthy, returns right)
print("" or "world")        # 'world' (left falsy, returns right)

print("hello" and "World")  # 'World' (left truthy, returns right)
print("" and "World")       # ''      (left falsy, returns left)
print("hello" or "World")   # 'hello' (or returns the first truthy value)
print("" or "World")        # 'World'
print(not "hello")          # False
print(not "")               # True


# Looping on strings
c = "hello World"

for i in c:
    print(i)


# Membership operators
print("H" in c)       # False (case-sensitive)
print('world' in c)   # False (case-sensitive)
print('World' in c)   # True