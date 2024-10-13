running = True
while running:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operation = input("Enter an operation: ")
    match operation:
        case "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            if num2 == 0:
                print("Error")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        case "^":
            if num2 == 0:
                result = "1"
                print(f"{num1} ^ {num2} = {result}")
            else:
                result = num1 ^ num2
                print(f"{num1} ^ {num2} = {result}")
        case "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")