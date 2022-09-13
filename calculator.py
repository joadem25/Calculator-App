firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
print("Operations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor division")
operationQuestion = input("Enter the corresponding number to the operation you want to perform: ")
if operationQuestion == "1":
    print("Anwser: " + str(firstNumber + secondNumber))
elif operationQuestion == "2":
    print("Anwser: " + str(firstNumber - secondNumber))
elif operationQuestion == "3":
    print("Anwser: " + str(firstNumber * secondNumber))
elif operationQuestion == "4":
    print("Anwser: " + str(firstNumber / secondNumber))
elif operationQuestion == "5":
    print("Anwser: " + str(firstNumber % secondNumber))
elif operationQuestion == "6":
    print("Anwser: " + str(firstNumber // secondNumber))
else:
    print("Invalid input")
