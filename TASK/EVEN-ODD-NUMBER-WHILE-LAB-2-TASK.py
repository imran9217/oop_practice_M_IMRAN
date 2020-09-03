#IMRAN LIAQAT
#BAIM-S20-003
# EVEN ODD WITH WHILE LOOP
################################################################
Minimum = int(input(" Please Enter the Minimum Value : "))
Maximum = int(input(" Please Enter the Maximum Value : "))
number = 1
Minimum = number

while number <= Maximum:
    if (number % 2 != 0):
        print(number,"IS ODD")
    number = number + 1


################################################################
Minimum = int(input(" Please Enter the Minimum Value : "))
Maximum = int(input(" Please Enter the Maximum Value : "))
number = 1
Minimum = number

while number <= Maximum:
    if (number % 2 == 0):
        print(number,"IS EVEN")
    number = number + 1
