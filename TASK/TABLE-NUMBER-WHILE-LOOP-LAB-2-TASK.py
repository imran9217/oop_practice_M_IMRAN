#########################################################
# table with while loop
#imramnliaqat
#baim-s20-003
tablenumber = int(input("Enter a number: "))
upperRANGE = int(input("Enter a lower limit: "))
lowerRANGE = int(input("Enter a upper limit: "))
i = upperRANGE
while (i <= lowerRANGE):
    print (i,"*",tablenumber,"=",i*tablenumber)
    i=i+1