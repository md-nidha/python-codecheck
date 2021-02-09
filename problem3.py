#On a chessboard, fields are marked with a letter between a and h for the column and a number between 1 and 8 for the row.
#Given a position string, print the color of the field (white or black)

inputstr='a1'
if(inputstr[0]=='a' or inputstr[0]=='c' or inputstr[0]=='e'):
    if (inputstr[1]=='1' or inputstr[1]=='3' or inputstr[1]=='5' or inputstr[1]=='7'):
        print("Black ")
else:
    print("White")
