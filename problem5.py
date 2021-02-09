# Given three numbers x, y, z, determine if one of them is the sum of the other two. 
# If so, print the equation, otherwise print "None found". For example, if x = 2,
# y = 1, and z = 3, print "z = x + y". If there are multiple possibilities (such as
# all values equal to 0) favor the solutions in this order: "x = y + z", "y = x + z",
# and "z = x + y".

x = 0 
y = 0 
z = 0 
if (x==0 and y==0 and z==0):
   print("x = y + z")
elif (x+y == z):
   print("z = x + y")
elif (x+z == y):
   print("y = x + z")
elif (y+z == x):
   print("x = y + z")
elif (x==y==z):
   print("None found")
