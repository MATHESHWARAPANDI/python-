class cal():  # PEP 8 standard for class name
    def __init__(self, a, b):  # PEP 8 standard for argument name
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b  # handle error (exception)

    def sub(self):
        return self.a-self.b


a = int(input("Enter first number: "))  # Pep 8 standard for variable name
b = int(input("Enter second number: "))  # Error handle
obj = cal(a, b)
# Don't hardcode any value in the code. Have it in separate file. (like constants, configurations etc)
choice = 1
while choice != 0:
    print("0. Exit")  # Don't hardcode any value
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    # Error handle. If I give a string, it will throw error.
    choice = int(input("Enter choice: "))
    # If you have multiple if, elif, else, Use Dictionary instead of nested if elif.
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        try:
            # Always add error handling in the source. (starting place)
            print("Result: ", round(obj.div()))
        except ZeroDivisionError:
            print("we cannot divided by Zero")
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
