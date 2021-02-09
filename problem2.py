#On a chessboard, positions are marked with a letter between a and h for the column and a number between 1 and 8 for the row.
#Given an input string with a letter and number, print whether it is in a corner, at the border, or in the inside of the chess board.

inputStr = 'a1'
corner=['a1','h1','a8','h8']
border=['b1','c1','d1','e1','f1','g1','a2','a3','a4','a5','a6','a7','b8','c8','d8','e8','f8','g8','h2','h3','h4','h5','h6','h7']
if inputStr in corner:
        print("corner")
elif(inputStr in border):
    print("Border")
else:
    print("Inside")
