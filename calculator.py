


print("welcome to the calculator first chose which one of the calculation procsess would you like to run")


def addition(x,y):
    additionval = x + y
    print (additionval)

def subtraction(x,y):
    subtractionval = x - y
    print (subtractionval)

def multiplication(x,y):
    multiplicationval = x * y
    print (multiplicationval)

def division(x,y):
    divisionval = x / y
    print (divisionval)


gameover = False

while gameover != True:

    calculationC = input("for addition type (+), for subtraction (-), for multiplication (*), and for divison (/): ")
    val1 = int(input("Imput your first number: "))
    val2 = int(input("enter your second number: "))
    
    if calculationC == "+":
        addition(val1,val2)
    elif calculationC == "-":
        subtraction(val1,val2)
    elif calculationC == "*":
        multiplication(val1,val2)
    else:
        division(val1,val2)
    
    continueval = input("would you like to make a new calculation Y or n: ")

    if continueval == "Y":
        gameover = False
    else:
        print("Thank You for using the calculator see you next time :)")
        gameover = True





















