# Author: Harrison Toppen-Ryan
# Description : Lab 2, CSCI 141
# Date: 10/5/20
# get the first and second integers
firstInput = int(input("Please enter the first integer: "))
secondInput = int(input("Please enter a second integer: "))
# A. print out "Fixing notation!"
print("Fixing notation!")
# B. Extract the integer and decimal portions from the first integer input
divFirstInput = firstInput // 10
if firstInput <= -1:
    divFirstInput = firstInput // 10 + 1
    # if statement for negative numbers 
else: divFirstInput = firstInput // 10
divFirstInput2= (firstInput % divFirstInput) * 0.1  
divFirstInput3 = divFirstInput + divFirstInput2
# C. Print the reformatted first input
print("The value", firstInput, "reformated is", divFirstInput3)
# D. Extract the integer and decimal portions from the second integer input
divSecondInput = secondInput // 10 
if secondInput <= -1:
    divSecondInput = secondInput // 10 + 1
     # if statement for negative numbers
else: divSecondInput = secondInput // 10 
divSecondInput2 = (secondInput % divSecondInput) * 0.1
divSecondInput3 = divSecondInput + divSecondInput2
# E. Print the reformatted second input
print("The value", secondInput, "reformated is", divSecondInput3) 
# F. Perform calculations for the product of the reformatted (decimal) values
productInput = (divFirstInput3 * divSecondInput3)
# G. Print out the final result
print("The product of", divFirstInput3, "and", divSecondInput3, "is", productInput)
