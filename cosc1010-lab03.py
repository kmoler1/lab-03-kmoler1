# Kaleb Moler
# UWYO COSC 1010
# 9/25/24
# Lab 03 
# Lab Section: 15
# Sources, people worked with, help given to: 
# Jay Trujio, Jhett Carr




# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
States= ["Wyoming", "Colorado", "Montana"]


#print the entire list
print(States)

#now print the first element in the list
print(States[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(States[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{States[1].upper()} is south of {States[0].upper()}")



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
States.append("Washington")
States.append("Oregon")
States.append("California")
print(States)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
States[-2]="Maine"
print(States)
#Insert the state Texas to be the third element in the list, again printing your list
States.insert(2,"Texas")
print(States)
#Using the `del` statement remove the fourth item from the list, print your list 
del States[3]
print(States)
#Remove Texas using its value, print the list
del States[2]
print(States)
print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(States))
print(States)
#Permanently sort your list in reverse order, printing it out
States.sort(reverse = True)
print(States)
#Using the reverse method reverse the list and print it
States.reverse()
print(States)
