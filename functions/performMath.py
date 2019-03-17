"""
first of all, it is important to understand that in python3, 're' stands for ReGex or Regular Expression.
because i intend splitting strings at some point in this program, i had to import the ReGex library on line 5.
"""
import re
previous = 0
run = True
def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0: 
        equation = input("enter equation: ")
    else:
        equation = input(str(previous))
    if equation == (str(' quit()')):
        print('Thank you for using my experimental calculator! see you next time.')
        run = False
    
    elif equation == (str('quit()')) and previous == 0:
         print('Thank you for using my experimental calculator! see you next time.')
         run = False
    else:
        equation = re.sub('[a-zA-Z,.:()""]', '', equation) #at this point, the ReGex is put into use
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)
while run:
    perform_math()
