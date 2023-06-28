def get_user_input():
    global first_number
    first_number = int(input("Please input the first number:"))
    global second_number
    second_number = int(input("Please input the second number:"))
    global type_of_calculation
    type_of_calculation = input("Tell me the type of calculation(+,-,*,/):")

def calculate():
    x = type_of_calculation
    if x == "+":
        solution = first_number + second_number
    elif x == "-":
        solution = first_number - second_number
    elif x == "*":
        solution = first_number * second_number
    elif x == "/":
        solution = first_number / second_number
    else:
        solution = "Please try again"   
    print(solution)

get_user_input()
calculate()

