def print_dash(print_yes_or_no):
    if (print_yes_or_no==1):
        return "-"
    else:
        return " "
def print_pipe(print_yes_or_no):
    if (print_yes_or_no==1):
        return "|"
    else:
        return " "
def print_blank():
    return " "

def print_column(val1,val2):
    print(print_pipe(val1),print_blank(),print_pipe(val2))

def print_row(val1):
    print(print_blank(),print_dash(val1),print_blank())

def printrowA(numb):
    if (numb== 1):
        print_row(0)
    elif(numb== 2):
        print_row(1)
    elif (numb == 3):
        print_row(1)
    elif (numb == 4):
        print_row(0)
    elif (numb == 5):
        print_row(1)
    elif (numb == 6):
        print_row(1)
    elif (numb == 7):
        print_row(1)
    elif (numb == 8):
        print_row(1)
    elif (numb == 9):
        print_row(1)
    elif (numb == 0):
        print_row(1)
def printrowB(numb):
    if (numb == 1):
        print_column(0,1)
    elif (numb == 2):
        print_column(0,1)
    elif (numb == 3):
        print_column(0,1)
    elif (numb == 4):
        print_column(1,1)
    elif (numb == 5):
        print_column(1,0)
    elif (numb == 6):
        print_column(1,0)
    elif (numb == 7):
        print_column(0,1)
    elif (numb == 8):
        print_column(1,1)
    elif (numb == 9):
        print_column(0,1)
    elif (numb == 0):
        print_column(1,1)

def printrowC(numb):
    if (numb == 1):
        print_row(0)
    elif (numb == 2):
        print_row(1)
    elif(numb == 3 ):
        print_row(1)
    elif (numb == 4):
        print_row(1)
    elif (numb == 5):
        print_row(1)
    elif (numb == 6):
        print_row(1)
    elif (numb == 7):
        print_row(0)
    elif (numb == 8):
        print_row(1)
    elif (numb == 9):
        print_row(1)
    elif (numb == 0):
        print_row(0)
def printrowD(numb):
    if (numb == 1):
        print_column(0, 1)
    elif (numb == 2):
        print_column(1, 0)
    elif (numb == 3):
        print_column(0, 1)
    elif (numb == 4):
        print_column(0,1)
    elif (numb == 5):
        print_column(0,1)
    elif (numb == 6):
        print_column(1,1)
    elif (numb == 7):
        print_column(0,1)
    elif (numb == 8):
        print_column(1,1)
    elif (numb == 9):
        print_column(0,1)
    elif (numb == 0):
        print_column(1,1)
def printrowE(numb):
    if (numb == 1):
        print_row(0)
    elif (numb == 2):
        print_row(1)
    elif (numb == 3):
        print_row(1)
    elif (numb == 4):
        print_row(0)
    elif (numb == 5):
        print_row(1)
    elif (numb == 6):
        print_row(1)
    elif (numb == 7):
        print_row(0)
    elif (numb == 8):
        print_row(1)
    elif (numb == 9):
        print_row(0)
    elif (numb == 0):
        print_row(1)

def printnumber(number):
        printrowA(number)
        printrowB(number)
        printrowC(number)
        printrowD(number)
        printrowE(number)

inputt=1
while (inputt != "0,0"):
    inputt = (input(" Write number: "))
    if (inputt !="0,0"):
        inputt=float(inputt)
        printnumber(inputt)


