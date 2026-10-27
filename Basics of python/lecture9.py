#if-else statement
a = 10
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")



#small dummy login App
username = "admin"
password = "admin123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")


if(input_username == username and input_password != password):
    print("Invalid password")
    new_password = input('Enter password again: ')
   
    if(new_password == password):
        print("Login successful")
elif(input_username != username and input_password == password):
    print("Invalid username")
      
elif(input_username == username and input_password == password):
    print("Login successful")
else:
    print("Invalid username or password")
