#list
#what is list
#list vs Array
#Creating a list
#Accessing a list
#Editing a list
#Adding elements to a list
#Deleting elements from a list
#operations on lists
#functions on lists




#what is List
#it's a data that hold multiple values in a single variable

#diff from Array
#Array is homogenous data type while list you can have diff datatypes in a single list
#Array is faster because memory is allocated in a contiguous block while list is slower because memory is allocated in a non-contiguous block
#list are more pragrammatic friendly because they have more built-in functions and methods than array




#Create a list
my_list = [1, 2, 3, 4, 5]

#homogeneous list
my_list1 = [1, 2, 3, 4, 5]

#heterogeneous list
my_list2 = [1, "hello", 3.14, True]

#multi-dimensional list
#2d list
my_list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#3d list
my_list4 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]



#Accessing a list
#accessing elements of a list
print(my_list[0])  # accessing the first element
print(my_list[-1])  # accessing the last element






#extract from multi-dimensional list
multi_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_list[0][0])  # accessing the first element of the first sublist
print(multi_list[1][2])  # accessing the third element of the second sublist



#editing a list
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # changing the first element
#list in python are mutable, so we can change the value of an element in a list by accessing it using its index and assigning a new value to it.

my_list[1:5] = [20, 30, 40, 50]  # changing multiple elements at once



#Adding elements to a list
#append() method
my_list.append(6)  # adding an element to the end of the list
#extend() method to add multiple elements to the end of the list
my_list.extend([7, 8, 9])  # adding multiple elements to the end of the list



l= [1, 2, 3, 4, 5]
l.append([6,7])  # adding a list as a single element to the end of the list
l.extend('goa') #l=[1, 2, 3, 4, 5, [6, 7], 'g', 'o', 'a'] adding each character of the string as a separate element to the end of the list

#insert() method to add an element at a specific index
my_list.insert(0, 0)  # adding an element at the beginning of the list



#deleting elements from a list
#remove() method to remove an element by value
my_list.remove(3)  # removing the element with value 3
#pop() method to remove an element by index
my_list.pop(0)  # removing the element at index 0    remove last element if no index is specified
#del statement to remove an element by index
del my_list[0]  # removing the element at index 0
#clear() method to remove all elements from the list
my_list.clear()  # removing all elements from the list



#operations on lists
#conctenation of lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2  # concatenating two lists #[1, 2, 3, 4, 5, 6]


list1 * 3  # repeating a list multiple times #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#looping through a list
for i in my_list:
    print(i)  # printing each element of the list


#functions on lists
len(my_list)  # getting the length of the list
min(my_list)  # getting the minimum value in the list
max(my_list)  # getting the maximum value in the list
sum(my_list)  # getting the sum of all elements in the list
sorted(my_list)  # getting a sorted version of the list it'will create a new list
sorted(my_list, reverse=True)  # getting a sorted version of the list in descending order it'will create a new list
sort() #method to sort the list in place chnage the exising list
#index() method to get the index of an element in the list


