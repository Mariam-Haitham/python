
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

operation = input("Choose the operation (+, -, /, *): ")

 

try:
    first_number = float(first_number)
    second_number = float(second_number)
    
    
    if operation != "+" and operation != "-" and operation != "/" and operation != "*":
        print("Invalid operation!")
    else:
        
        answer = 0.0
        
        if operation == "+":
            answer = first_number + second_number
        elif operation == "-":
            answer = first_number - second_number
        elif operation == "/":
            answer = first_number / second_number
        else:
            answer = first_number * second_number
            
        print ("The answer is " + str(answer))
    
except ValueError:
    print("Invalid numbers!")
    