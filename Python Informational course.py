# Integration-project
# Zachary Mixson
# Educational Program
name = input("What is your name?")
print("Hello,", name, "welcome to my new game!")


def print_statements():
    print('To print a string in python you must use the "print" statement.')
    print("Here is an example of a print statement:")
    print('print("Hello World!")')
    print("That statement would show the user:")
    print("Hello World!")
    print("To print a value of a variable do not use quotations just place "
          "the name of the variable inside the parenthesis.")
    print("For example:")
    print("x = 4")
    print('print(x)')
    print("The user would see:")
    print("4")
    closing_statement()


def variables(x):
    # The definition of a variable came from W3 schools
    # https://www.w3schools.com/python/python_variables.asp
    print('According to W3 schools "Variables are containers for '
          'storing data values."')
    print("When creating a variable you must follow the naming rules.")
    print("Here are the naming rules:")
    print('1) Function names can only start with an underscore "_"or any '
          'letter and may not start with a number.')
    print('2) Name can only contain numbers, letters and underscores("_")')
    print("3) Variable names are case sensitive.")
    print('To assign a value to a variable you must use the assignment '
          'operator "="')
    print('For example:')

    print('number = ', x)
    print('print(number)')
    print("The output would be ", x)
    closing_statement()


def math_statements():
    a = int(input("Enter any random number!"))
    b = int(input("Enter another random number!"))
    int(a)
    int(b)
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("sum = a + b")
    print("difference = a - b")
    print("product = a * b")
    print("quotient = a / b")
    print("The sum of your numbers is", sum)
    print("The difference  of your numbers is", difference)
    print("The product of your numbers is", product)
    print("The quotient of your numbers is", quotient)
    closing_statement()


def inputs():
    print('In python the "input()" function is used to prompt and gather data '
          'from the user.')
    print('To prompt the user for input write the prompt between quotations '
          'inside the parenthesis.')
    print('For example:')
    print('input("Write the prompt here.")')
    print('To save the input of a user assign it to a variable')
    print('For example:')
    user_input = input("Type to save to user_input")
    print('user_input = input("Prompt")')
    print('Whatever the user types will be saved to the "user_input" '
          'variable and can be displayed by')
    print("print(user_input)")
    print("Would output:")
    print(user_input)
    closing_statement()


def boolean_values_and_comparison_operators():
    print("Boolean values are either true or false.")
    print('comparison operators are operators that only respond with Boolean '
          'values.')
    print('-----------------------------------------')
    print('|      ==      |        Equal to        |')
    print('|      !=      |      Not Equal to      |')
    print('|      <       |       Less Than        |')
    print('|      >       |      Greater Than      |')
    print('|      <=      | Less than or equal to  |')
    print('|      >=      |Greater than or equal to|')
    print('-----------------------------------------')
    print("")
    print("For example:")
    print("1==1")
    print('Would return', '"', 1 == 1, '"')
    closing_statement()


def if_else_statements():
    print("An if statement only runs if the condition returns true.")
    print("For example:")
    print("x = 0")
    print("if x < 1:")
    print('    print("yes")')
    print("Would output:")
    x = 0
    if x < 1:
        print("yes")
    print("An else statement is what happens when the if statement returns "
          "false.")
    print("For example:")
    print("x = 2")
    print("if x < 1:")
    print('    print("yes")')
    print("else:")
    print('    print("no"')
    print("Would output:")
    x = 2
    if x < 1:
        print("yes")
    else:
        print("no")
    closing_statement()


def nested_if_else_statements():
    print("A nested if else statement is when one if statement is inside "
          "another so for the inner one to run both the inner and the outer "
          "statement must be true.")
    print("For example:")
    print("x = 4")
    print("if x = 4:")
    print("    if x < 5:")
    print('        print("Both loops are true")')
    print("Would output:")
    x = 4
    if x == 4:
        if x < 5:
            print("Both loops are true")
    closing_statement()


def while_loops():
    print("A while loop executes as long as the statement is true.")
    print("For example:")
    print("i = 1")
    print("while i < 6:")
    print("    print(i)")
    print("    i += 1")
    print("")
    print("That outputs:")
    x = 1
    while x < 6:
        print(x)
        x += 1
    closing_statement()


def for_loops():
    print("The for loop executes for each item in a list.")
    print("For example:")
    print("colors = [red, blue, yellow]")
    print("for x in colors:")
    print("    print(x)")
    print("Would output:")
    colors = ["red", "blue", "yellow"]
    for x in colors:
        print(x)
    closing_statement()


def nested_loops():
    print("A nested loop is a loop inside of a loop so the inside loop "
          "only runs every time the outside loop runs and the inside loop "
          "is also true.")
    print("For example:")
    print("for i in range(1,11):")
    print("    for j in range(1,11):")
    print("        k = i * j")
    print('        print(k, end=" ")')
    print("    print()")
    print("Would output:")
    for i in range(1, 11):
        for j in range(1, 11):
            k = i * j
            print(k, end=" ")
        print()
    closing_statement()


def end():
    print("Thank you " + name + " for trying my educational program, i "
                                "hope you enjoyed it!")


def closing_statement():
    decision = int(input('When done press "1" for menu and "2" to end the '
                         'program.'))
    x = 0
    for x in range(1, 24):
        print("/", end="")
    i = 0
    for i in range(1, 6):
        print()
    if decision == 1:
        main()
    if decision == 2:
        end()


def main():
    print("1) Print Statements")
    print("2) Variables")
    print("3) Math Statements")
    print("4) Inputs")
    print("5) Boolean Values and Comparison Operators")
    print("6) if else Statements")
    print("7) Nested if else Statements")
    print("8) While Loops")
    print("9) For Loops")
    print("10) Nested Loops")
    print("11) End Program")
    topic = int(input("Enter the number next to the topic you would like to "
                      "learn about:"))
    x = 0
    for x in range(1, 24):
        print("/", end="")
    i = 0
    for i in range(1, 6):
        print()

    if topic == 1:
        print_statements()
    if topic == 2:
        variables(4)
    if topic == 3:
        math_statements()
    if topic == 4:
        inputs()
    if topic == 5:
        boolean_values_and_comparison_operators()
    if topic == 6:
        if_else_statements()
    if topic == 7:
        nested_if_else_statements()
    if topic == 8:
        while_loops()
    if topic == 9:
        for_loops()
    if topic == 10:
        nested_loops()
    if topic == 11:
        end()
    else:
        print("Invalid entry. Please try again.")
        input("Press enter to continue")
        x = 0
        for x in range(1, 24):
            print("/", end="")
        i = 0
        for i in range(1, 6):
            print()

        main()


main()
