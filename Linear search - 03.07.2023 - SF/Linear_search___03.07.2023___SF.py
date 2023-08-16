#MAIN
from IDCard import IdentificationCard

def printItems(myPrintList,length):
	print()
	for i in range(length):
		print(myPrintList[i].getfirstName(),"-",myPrintList[i].getIDNumber(),end = " | ")
	print("")
	print()

def checkIDNum(idNum):
	print("\nChecking if valid ID Entered...")
	print(idNum[:3],idNum[3:6],idNum[6:])
	acceptedID = True
	if idNum[:3].isnumeric() == False or idNum[6:].isnumeric() == False or idNum[3:6].isalpha() == False or idNum[3:6].isupper() == False or len(idNum) != 9:
		acceptedID = False
	print(acceptedID)
	return acceptedID

def bubbleSortList(myList):
	swapped = True
	i = 0
	while i < len(myList) and swapped == True:
		swapped = False
		print("\n\nOuter Loop:",i+1,"\nNo. inner loops/Length of list still sorting:",len(myList)-1-i,"\nCurrent Sorting List:")
		printItems(myList,len(myList)-i)

		j = 0
		while j < len(myList)-1-i:
			if myList[j].getIDNumber() > myList[j+1].getIDNumber():
				print("- Swap:",myList[j].getfirstName(),"(",myList[j].getIDNumber(),") -",myList[j+1].getfirstName(),"(",myList[j+1].getIDNumber(),")")
				temp = myList[j]
				myList[j] = myList[j+1]
				myList[j+1] = temp
				swapped = True
			j+=1
		if swapped == False:
			print("\nList sorted!")

		i+=1


IDs = []
for i in range(5):
    print("\nNew ID")
    firstN = input("Enter FirstName: ").title()
    lastN = input("Enter LastName: ").title()
    while True:
        idNum = input("Enter ID (e.g 000AAA000): ")
        if checkIDNum(idNum) == True:
            break
        else:
            print("Not valid.")

    newID = IdentificationCard(firstN,lastN,idNum)
    IDs.append(newID)

printItems(IDs,5)

bubbleSortList(IDs)

printItems(IDs,5)

while True:
	searchNum = input("\n\nEnter ID Number to search for: ")
	if checkIDNum(searchNum) == True:
		break

found = False
i = 0
while found == False:
	if searchNum == IDs[i].getIDNumber():
		found = True
		print("\nAll info for - ID: "+searchNum+":")
		print("First Name:",IDs[i].getfirstName(),"\nLast Name:",IDs[i].getlastName(),"\nId Number:",IDs[i].getIDNumber())

	elif i == len(IDs):
		print("ID does not exist.")
	i += 1
