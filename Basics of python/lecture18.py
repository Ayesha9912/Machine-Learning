#string is soo helpful in real world projects
#strings are aequence of characters
#in pythn strings are sequence of unicode character

#- creating strings
# - Accessing strings
# - adding char to strings
# - edititng strings
# - deleting strings
# - operations strings
# - strings functions



#creatng 
print("hello")
print("""hello""")



#Accessing substrings from a string
#concept of indexing
c= 'hello'
print(c[0])
#types of  indesing
 #- positive indexing
 #- Negative indxing

print(c[-2]) # usefull in whn you want a last value of string from user and you ctually don't know the value of string



#slicing - to get all character or more than one character
print('slicing', c[0:3]) # c[start, stop , step]
print('new',c[0:5:4])
# print(c[0,3,-2]) #- empty stromg whn workimg with positive , don't use negative  
# 
c = 'hello'

print(c[0:3:1])   # hello  (every character)
print(c[0:3:2])   # hlo    (indexes 0, 2, 4)
print(c[0:5:3])   # hl     (indexes 0, 3)
print(c[::-1])    # olleh  (negative step reverses the string)



s = 'programming'

print(s[0:4])        # prog
print(s[2:8:2])      # ormn
print(s[::3])        # pgmn
print(s[3:])         # gramming
print(s[:5])         # progr
print(s[::-2])       # gimrop
print(s[-3:])        # ing
print(s[1:9:4])      # ra
print(s[8:2:-2])     # imr
print(s[-1:-6:-1])   # gnimm






#editing and deleting string
r = "heloo"
r[0] = 'x' #it will throw error that you can't edit srings - ver imporant
 #strings are immutable datatype
 #mutataion mens change so i python we can't mute or change the string


 #we can reassign but can mute and also don't add characters



 #Deletion
 del r
print(r) - #it give r not define as it deleted

del[2]  #error we cannot delete items




#operaions in string
#arthematic operators
#Relational operators
#logical operators
#lops on strings
#membership operations


#arthematic

r = 'hello'+ ' ' + 'world'
print('concatenation',r)

#string multuplication
print("*" * 59)
print('hell' * 4)



#Relational operators


"hello" == "world" #false
"america" > "india" #false whyyyy #lexiographical - according to dictionary i comes before tha A

"kol" < "Kol" #false kuin ka choty letters bad ma aty hain jo bad ma ata ha it's bigger


#logical operators

"hell" - #True
"" #-false

"hell" and '' # '' false
"" or "world" #-true


"hello" and "World" #= 'world
"hello" and "World"   # 'World'  (left truthy, returns right)
"" and "World"        # ''       (left falsy, returns left)
"hello" or "World"    # 'hello'  (or returns the first truthy value)
"" or "World"         # 'World'
not "hello" #false
not "" #true




#loop in strings
 c= "hello World"

for i in c
print(i)


#membership operators

"H" in c
#false

'world' in c
#false


