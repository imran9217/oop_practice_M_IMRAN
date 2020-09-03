# Python program to check if the input number is odd or even
# A number is even if division by 2 gives a remainder of 0
# If the remainder is 1 it is an odd number
#imranliaqat
#baim-s20-003

num: int = int(input("Enter a number: "))
if (num % 2) == 0:
    print( " is Even")

else:
     print( " is Odd")