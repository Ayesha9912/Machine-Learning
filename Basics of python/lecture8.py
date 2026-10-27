#operators
#arithmetic operators
#comparison operators
#logical operators
#bitwise operators
#assignment operators
#identity operators
#membership operators


#arithmetic operators
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b) # exponentiation
print(a // b) # floor division


#comparison operators
print(a > b)   # greater than
print(a < b)   # less than
print(a == b)  # equal to



#logical operators
x = True
y = False
print(x and y)  # logical AND
print(x or y)   # logical OR
print(not x)    # logical NOT


#bitwise operators - image filters, image processing, encryption, compression, etc
a = 10 # 1010
b = 5  # 0101
print(a & b)  # bitwise AND
print(a | b)  # bitwise OR
print(a ^ b)  # bitwise XOR
print(~a)     # bitwise NOT
print(a << 2) # left shift
print(a >> 2) # right shift



#assignment operators
a = 10
a += 5  # equivalent to a = a + 5
a -= 3  # equivalent to a = a - 3
a *= 2  # equivalent to a = a * 2
a /= 4  # equivalent to a = a / 4
a %= 3  # equivalent to a = a % 3
a **= 2 # equivalent to a = a ** 2
a //= 2 # equivalent to a = a // 2

# a++ don't work in python because python does not support increment and decrement operators like C, C++, Java, etc. Instead, you can use a += 1 to increment a by 1 and a -= 1 to decrement a by 1.





#identitiy operators
a = 10
b = 10
print(a is b)  # True, because both a and b refer to the same object in memory
print(a is not b)  # False, because both a and b refer to the same object in memory
#id doen't matter same values have same memory allocation
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, because a and b refer to different objects in memory
print(a is not b)  # True, because a and b refer to different objects in memory



#membership operators
d = "Delhi"
print("D" in d)  # True, because "D" is a character in the string d
print("x" not in d)  # True, because "x" is not a character in the string d