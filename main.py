def adder():
    print("Add New Record")
    roll = int(input("Enter Roll No."))
    name = input("Enter Name")
    currentClass = input("Enter Class")
    ptr = input("Enter Pointer")
    details = [name, currentClass, ptr]
    dict[roll] = details


def search():
    query = int(input("Enter Roll No."))
    print("Name: " + dict[query][0])
    print("Class: " + dict[query][1])
    print("Pointer: " + dict[query][2])


dict = {}
while(1):
    print("1. Add Record")
    print("2. Search Record")
    print("3. Exit")
    ch = input("Enter your Choice")
    if ch is '1':
        adder()
    elif ch is '2':
        search()
    else:
        break

print("ENDED")