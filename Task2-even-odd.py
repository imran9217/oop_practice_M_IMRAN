# Python program to check if the input number is odd or even
# A number is even if division by 2 gives a remainder of 0
# If the remainder is 1 it is an odd number
#imranliaqat
#baim-s20-003

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(num, " is Even")

else:
     print(num, " is Odd")
        
#######################################################################################################
for loop even odd




minimum = int(input("PLEASE ENTER THE minimum VALUE :="))
maximum = int(input("PLEASE ENTER THE maximum VALUE :="))

for number in range(minimum, maximum+1):
    if(number % 2==0):
        print("EVEN NUMBER")
        print (number )
print("#########################################")
for number in range(minimum, maximum+1):
    if (number % 2 == 1):
        print("ODD NUMBER")
        print (number)
