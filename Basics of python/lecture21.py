#tuples
#similar to lists but immutable
#crete a tuple
t1 = (1, 2, 3, 4, 5) #homegeneous tuple
print(t1)
t2 = (1, "hello", 3.14, True) #heterogeneous tuple
print(t2)
#2d tuples
t3 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(t3)
#when single itme in tuple act as string or int
#like 
t4 = (1) #int
print(type(t4))
#to make it tupes it must be 
t5 = (1,) #tuple
print(type(t5))

#to create a tuple using tuple() function
t6 = tuple("Goa") #tuple of characters
print(t6)



#Accessing a tuple
print(t1[0])  # Access first element
print(t2[1])  # Access second element
print(t3[0][1])  # Access second element of first sublist

#Edit a tuple
#we cannot edit tuples as they are immutable, but we can convert them to a list, edit the list, and convert it back to a tuple
#we can't add or remove elements from a tuple, but we can concatenate two tuples to create a new tuple
#we can't delete single element from tuple, but we can delete the entire tuple using del keyword


#operations on tuples
t7 = t1 + t2  # Concatenation
print(t7)
#we can multiply a tuple by an integer to create a new tuple with repeated elements
t8 = t1 * 2  # Repetition
print(t8)

#loop on tuples
for item in t1:
    print(item)

#functions on tuples
print(len(t1))  # Length of tuple
print(max(t1))  # Maximum element
print(min(t1))  # Minimum element
print(sum(t1))  # Sum of elements
print(sorted(t1))  # Sorted tuple
