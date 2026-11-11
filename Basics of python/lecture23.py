#sets
#sets do not allow duplicate values
#set has no idexing/slicing
#set don't allow mutable data types like list, dict, set
#set itself is a mutable data type


#create a set
s1 = {1, 2, 3, 4, 5} #homogeneous set
print(s1)
s2 = {1, "hello", 3.14, True} #heterogeneous set
print(s2)


#sets don't allow duplicates
s3 = {1,1,2,2,3,3,4,4,5,5}  
print(s3) #output will be {1, 2, 3, 4, 5}


s4 = {[1,2], [3,4]} #this will give error because list is mutable data type
s5 = {{1,2}, {3,4}} #this will give error because set is mutable data type
s6 = {{"name": "John"}, {"age": 30}} #this will give error because dict is mutable data type
s7 = {(1,2), (3,4)} #this will work because tuple is immutable data type


#sets have no indexing , it allow hashing 
#like 
s8 = {(1,2,3), "Hello"} 
print(s8) #output {('Hello',), (1, 2, 3)} #it change the order of the elements because set is unordered data type
#hashing is a process of converting a data into a fixed size value, which is used to identify the data.
#set don't create 2d or 3d

#no indexing / slicing we can not access the elements of a set using index or slice, but we can use for loop to iterate through the elements of a set
print(s2[2]) #error
#Edit
#we can't edit data sets

#we can add elements to a set using add() method, but we can't remove elements from a set using remove() method, but we can use discard() method to remove an element from a set, if the element is not present in the set, it will not give error.
s1.add(6) #adding an element to the set


#delete
del s2 #it will remove
del s2[1] #error because set has no indexing

s3.remove(3) #removing an element from the set
s3.pop() #removing a random element from the set



#we can't concatenate two sets using + operator, but we can use union() method to concatenate two sets, it will return a new set with all the elements from both sets, but it will not allow duplicate values.
#we can't repeat or multiply a set using * operator, but we can use intersection() method to get the common elements from both sets, it will return a new set with all the common elements from both sets.
#we can run loop
for i in s2:
    print(i)

#functions on sets
print(len(s1)) #length of set
print(max(s1)) #maximum element of set
print(min(s1)) #minimum element of set
print(sorted(s1)) #sorted set it will return a new list with sorted elements of set

#new functions
print(s1.union(s2)) #union of two sets
print(s1.intersection(s2)) #intersection of two sets
print(s1.difference(s2)) #difference of two sets
print(s1.symmetric_difference(s2)) #symmetric difference of two sets

print(s1.issubset(s2)) #check if s1 is subset of s2
print(s1.issuperset(s2)) #check if s1 is superset of
print(s1.isdisjoint(s2)) #check if s1 and s2 are disjoint sets