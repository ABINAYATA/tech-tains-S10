slots=int(input("Enter the total parking slots:"))
park1 = int(input("Enter the vechicles number1:"))
park2 = int(input("Enter the vechicles number2:"))
slot=1
for slot in range(1,slots+1):
    if(slot==park1 ):
        print("Vehical can be parked at slot",slot)
    elif(slot==park2):
      print("Vehicle can be parked at slot",slot)
available=slots-2
print("Available parking slots =",available)
remove=int(input("Enter the vehicles number to be removed:"))
if(remove==park1 or remove==park2):
    available=available+1
    print("Vehicals removed from slot",slots)
    print("Available parking slots =",available)
else:
    print("Vechicle not found")

