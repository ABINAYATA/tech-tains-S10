password=input("Enter the password:")

if(password.isalpha() or password.isdigit()):
    print("password strength=week")
elif(password.isdigit()  password.isalpha()):
    print("password strength=medium")

else:
    print("password strength=strong")