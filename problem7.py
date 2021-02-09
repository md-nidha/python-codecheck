#Given two integers x and y, print their sum, but if it is more than 100 or less than 0, print "out of range"

x = int(input("Value of x: "))
y = int(input("Value of y: "))
sum= x+y
range=(0,100)
if (sum>100 or sum<0):
   print("out of range")
else:
   print(sum)

