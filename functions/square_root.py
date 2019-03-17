from cmath import sqrt
from math import *

num = 0
tempt = True
ans = ""
def square_root(ans):
    global tempt
    global num
    square = (str(input("enter number to get square root: ")))
    if square != str('quit()'):
         square = float(square)
         ans = sqrt(square)
         print('the square root of', square, 'is', ans)

    elif square == (str('quit()')):
        print('Thank you for using my experimental calculator! see you next time.')
        tempt = False
    

while tempt:
    square_root(ans)

if tempt == False:
        print('Thank you for helping my python learning experience!')
