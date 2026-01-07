n=int(input("enter total class held:"))
m=int(input("enter class attended:"))
percentage=(m/n)*100
if(percentage>=75):
    print("eligible ")
else:
    print("not eligible")
additional_classes =((75 *100/n)-m)
print ("additional classes needed =",additional_classes)