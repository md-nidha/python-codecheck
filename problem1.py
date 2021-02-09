#Given an input string, print the string with the first and last letter removed if they were equal, or the original string if they were not.

inputStr = 'test' 
if inputStr[0]==inputStr[-1]:
   print(inputStr[1:3])
else:
   print(inputStr)
