#string functions

#common functions
#len
#Max
#min
#sorted

c = 'Pakistan'
len(c) #8 show the length

max(c)
# t biggest value

min(c)
# a smalles value


print(sorted(c))
#ascending order

sorted(c,reverse=True)
#descending


#capitalize/Title/Lower/Swapcase
print("it is raining".capitalize())
print("it is raining".title())
print("it is raining".upper())
print("it is raining".lower())
print("it Is Raining".swapcase())



#count
print("it is raining".count("i"))
print("it is raining".count("is"))

#find/index
print("it is raining".find("is"))
print("it is raining".index("is"))
#both are same but if you add any value which is not in string it give -1 while index give error


#endswith/startswith
print("it is raining".endswith("is")) #false
print("it is raining".startswith("is")) #false


#format
print("hello my name is {} and I am {}".format("Ayesha" , 30)) #fill the blanks
print("hello my name is {1} and I am {0}".format("Ayesha" , 30)) #fill the blanks
print("hello my name is {name} and I am {age}".format(name="Ayesha" , age=30)) #fill the blanks



#isalnum/isalpha/isdecimal/isdigit/isidentifier

print("flat20".isalnum)
print("flat20%".isalpha)



#split
print("it is raining".split())
print("it is raining".split('i'))



#join
'-'.join(['it', 'is', 'raining'])   # 'it-is-raining'
''.join(['it', 'is', 'raining'])    # 'itisraining'
', '.join(['it', 'is', 'raining'])  # 'it, is, raining'

print(' '.join(['it', 'is', 'raining']))


#replace
print("Hi my name is Ayesha".replace("Ayesha" , "Neha"))


#strip
name="                Ayesha                   "
print(name.strip())







