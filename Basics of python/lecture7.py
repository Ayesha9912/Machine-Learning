#literal - a raw data given to an variable
#there are four types
#numeric literal - int, float, complex
#String literal - str
#bollean literal - bool
#special literal - None



#Numeric literal
a = 0b1010 #binary literal
b = 100 #decimal literal
c=  0o310 #octal literal
d = 0x15c #hexadecimal literal

print(a,b,c,d)

#float literal
f = 10.5e-5
print(f)

#complex literal
z = 3+4j
print(z , z.real, z.imag, z.conjugate())


#string literal
string = "Hello World"
char = 'A'
multiline_string = """This is a multiline string"""
unicode = u"\U0001F602"
raw_string = r"raw \n string"
print(string,char,multiline_string,unicode,raw_string)



#boolean literal
d = True + 3
print(d) #this will return 4 because True is equal to 1 and False is equal to 0


#special literal
a = None #to declare variable as we cannot declare variable without value in python
print(a)
