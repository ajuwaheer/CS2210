#TASK 1
#Declaration and initialisation of the variables
length = 0
width = 0
height = 0
weight = 0.0
dimensionsSum = 0

accepted = False

#Entering the dimensions of the package and making sure that they are greater than 0
while ( length <= 0 or width <= 0 or height <= 0 ):
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))

    if (length <= 0 or width <= 0 or height <= 0):
        print("One of the dimension is incorrect. Please enter a number greater than 0.")

#Entering the weight of the package and making sure that it is greater than 0
while (weight <= 0):
    weight = int(input("Enter weight of box: "))

    if (weight <= 0):
        print("Weight should be greater than 0.")

#Finding the sum of the three dimensions
dimensionsSum = length + width + height

#Determining if the package is accepted or rejected
if (length > 80 or width > 80 or height > 80 or dimensionsSum > 200 or weight > 10 ):
    accepted = False
else:
    accepted = True

#Outputting the correct message (accepted or rejected)
print("")
if (accepted == True):
    print("The box package has been accepted.")
else:
    print("The box package has been rejected beacause of the folowing reasons:")

#Outputting all the reasons reasons if rejected
if (length > 80):
    print("The length of the package is greater than 80 cm.")
if (width > 80):
    print("The width of the package is greater than 80 cm.")
if (height > 80):
    print("The height of the package is greater than 80 cm.")
if (dimensionsSum > 200):
    print("The sum of the three dimensions of the package is greater than 200 cm.")
if (weight > 10):
    print("The weight of the package is greater than 10 kg.")

############################################################################################################
#TASK 2
#Declaration and initialisation of the variables
numOfBoxes = 0
numberAccepted = 0
totalWeight = 0.0

numOfBoxes = int(input("Enter the number of box packages in the consignment: "))

for i in range(numOfBoxes):
    length = 0
    width = 0
    height = 0
    weight = 0.0
    dimensionsSum = 0

    accepted = False

    #Entering the dimensions of the package and making sure that they are greater than 0
    while (length <= 0 or width <= 0 or height <= 0):
        print("")
        length = int(input("Enter length: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))

        if (length <= 0 or width <= 0 or height <= 0):
            print("One of the dimension is incorrect. Please enter a number greater than 0.")

    #Entering the weight of the package and making sure that it is greater than 0
    while (weight <= 0):
        weight = int(input("Enter weight of box: "))

        if (weight <= 0):
            print("Weight should be greater than 0.")

    #Finding the sum of the three dimensions
    dimensionsSum = length + width + height

    #Determining if the package is accepted or rejected
    if (length > 80 or width > 80 or height > 80 or dimensionsSum > 200 or weight > 10):
        accepted = False
    else:
        accepted = True
        numberAccepted = numberAccepted + 1
        totalWeight = totalWeight + weight

    #Outputting the correct message (accepted or rejected)
    if (accepted == True):
        print("The box package has been ACCEPTED.")
    else:
        print("The box package has been REJECTED beacause of the folowing reasons:")

    #Outputting all the reasons reasons if rejected
    if (length > 80):
        print("The length of the package is greater than 80 cm.")
    if (width > 80):
        print("The width of the package is greater than 80 cm.")
    if (height > 80):
        print("The height of the package is greater than 80 cm.")
    if (dimensionsSum > 200):
        print("The sum of the three dimensions of the package is greater than 200 cm.")
    if (weight > 10):
        print("The weight of the package is greater than 10 kg.")

#Outputting the data asked in task 2
print("")
print("The number of box package accepted is", numberAccepted, ".")
print("The total weight of box package accepted is", totalWeight, "kg.")
print("The number of box package rejected is", numOfBoxes - numberAccepted, ".")

############################################################################################################
#TASK 3 (Extending task 2 to complete task 3)
#Declaration and initialisation of the variables
numOfBoxes = 0
numberAccepted = 0
totalWeight = 0.0
totalPrice = 0.0

numOfBoxes = int(
    input("Enter the number of box packages in the consignment: "))

for i in range(numOfBoxes):
    length = 0
    width = 0
    height = 0
    weight = 0.0
    dimensionsSum = 0

    accepted = False
    price = 600.0

    #Entering the dimensions of the package and making sure that they are greater than 0
    while (length <= 0 or width <= 0 or height <= 0):
        print("")
        length = int(input("Enter length: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))

        if (length <= 0 or width <= 0 or height <= 0):
            print(
                "One of the dimension is incorrect. Please enter a number greater than 0.")

    #Entering the weight of the package and making sure that it is greater than 0
    while (weight <= 0.0):
        weight = float(input("Enter weight of box: "))

        if (weight <= 0.0):
            print("Weight should be greater than 0.")

    #Finding the sum of the three dimensions
    dimensionsSum = length + width + height

    #Determining if the package is accepted or rejected
    if (length > 80 or width > 80 or height > 80 or dimensionsSum > 200 or weight > 10.0):
        accepted = False
    else:
        accepted = True
        numberAccepted = numberAccepted + 1
        totalWeight = totalWeight + weight

    #Outputting the correct message (accepted or rejected)
    if (accepted == True):
        print("The box package has been ACCEPTED.")
    else:
        print("The box package has been REJECTED beacause of the folowing reasons:")

    #Outputting all the reasons reasons if rejected
    if (length > 80):
        print("The length of the package is greater than 80 cm.")
    if (width > 80):
        print("The width of the package is greater than 80 cm.")
    if (height > 80):
        print("The height of the package is greater than 80 cm.")
    if (dimensionsSum > 200):
        print("The sum of the three dimensions of the package is greater than 200 cm.")
    if (weight > 10.0):
        print("The weight of the package is greater than 10.0 kg.")

    #Calculating the price for each box package accepted
    if (accepted == True):
        if (weight < 5):
            print("This box package costs Rs 600")
            totalPrice = totalPrice + price
        else:
            weightDifference = weight - 5.0
            numberOf100Grams = weightDifference / 0.1
            price = price + (numberOf100Grams * 65.10)
            print("This box package costs Rs", price)
            totalPrice = totalPrice + price


print("")
print("The number of box package accepted is", numberAccepted, ".")
print("The total weight of box package accepted is", totalWeight, "kg.")
print("The number of box package rejected is",numOfBoxes - numberAccepted, ".")
print("The total price of the consignment is Rs", totalPrice)
