try:
    num1=int(input("Enter numerator: "))
    num2=int(input("Enter denominator: "))
    result=num1/num2
    print("Result:",result) 
except ZeroDivisionError: 
    print("Error: Please enter valid integers.")
