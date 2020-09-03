#  python program table with for loop
#imran  liaqat
#baim-s20-003
num = int(input("Enter the number: "))

rangestart =int(input("ENTER THE TABLE START POINT =="))
rangeend =int(input("ENTER THE TABLE END POINT =="))

for i in range(rangestart, rangeend):
   print(num,"X",i,"=",num * i)