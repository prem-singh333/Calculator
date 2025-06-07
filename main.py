def calculator():
    print(f"{1} for Add")
    print(f"{2} for Subtract")
    print(f"{3} for Multiply")
    print(f"{4} for Divide")

    print("")
    
    option = int(input("Select chooice: "))

    if option not in [1, 2, 3, 4]:
        print("Invalide chooice")
    
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 1:
            result = num1 + num2

        elif option == 2:
            result = num1 - num2
        
        elif option == 3:
            result = num1 * num2

        else:
            if num2 == 0:
                print("Cannot divided by zero")

            else:
                result = num1 / num2

    while True:
        more = input("Do you want add more number? (Yes/No): ")

        if more.lower() == 'no':
            result
            break

        else:
            extra = float(input("Enter extra number: "))

            if option == 1:
                result += extra

            elif option == 2:
                result -= extra
        
            elif option == 3:
                result *= extra

            else:
                if num2 == 0:
                    print("Cannot divided by zero")

                else:
                    result /= extra
    print(result)


calculator()