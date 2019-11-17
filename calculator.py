import re

print("Continuos Calculator")
print("Type 'quit' to exit \n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous)," ")

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-z][A-Z],.:()" "', '', equation)
        if type(equation[-1]) == type(1):
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous)+ equation)
        else:
            print("Wrong equation. Exiting calculator")
            run = False

while run:
    performMath()