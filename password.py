password="abinaya6@"
if(password.isalpha()):
    print("password strength=week")
elif(password.isdigit() and password.isalpha()):
    print("password strength=medium")
else:
    print("password strength=strong")