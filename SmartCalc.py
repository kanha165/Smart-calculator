operation = (
    'add', 'subtract', 'multiply', 'devide', 'modulus', 'power',
    'floordivision', 'and', 'or',
    'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal',
    'table', 'data_analysis', 'see history', 'exit'
)

history = [] #to store history of calculations
#make functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        print("Divide by zero gives infinite value!")
        return None
    return a / b    

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floordivision(a, b):
    return a // b

def And(a, b):
    return bool(a) and bool(b)

def Or(a, b):
    return bool(a) or bool(b)

def equal(a, b):
    return a == b

def notequal(a, b):
    return a != b

def greater(a, b):
    return a > b

def less(a, b):
    return a < b

def greaterequal(a, b):
    return a >= b

def lessequal(a, b):
    return a <= b

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    history.append(f"table({n})")

def data_analysis():
    a = float(input("Enter the first value: "))        
    b = float(input("Enter the second value: "))
    avg = (a + b) / 2
    print(f"Minimum number is: {min(a, b)}")
    print(f"Maximum number is: {max(a, b)}")
    print(f"Average number is: {avg}")
    history.append(f"data_analysis({a}, {b}) min={min(a,b)}, max={max(a,b)}, avg={avg}")
#main program loop
print("======================================")    
print("     Welcome to Smart Calculator      ")
print("======================================") 
#always run until user wants to exit the program
while True:
    print("\nAvailable operations are:")
    for op in operation:
        print(op)
    perform = input("\nWhat operation do you want to perform? : ").strip().lower()#rember to strip any extra spaces and convert to lowercase
#give conditions for every operation
    if perform == 'exit':
        print("Exiting... Bye Bye ")
        break

    elif perform == 'see history':
        print("\n===== Calculation History =====")
        if not history:  
            print("No operations performed yet.")
        else:
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
        print("===============================")
        continue

    elif perform == 'table':
        n = int(input("Enter the number for multiplication table: "))
        table(n)

    elif perform == 'data_analysis':
        data_analysis()

    elif perform in (
        'add', 'subtract', 'multiply', 'devide', 'modulus', 'power', 'floordivision',
        'and', 'or',
        'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal'
    ):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        result = None
        match perform:
            case 'add':
                result = add(a, b)
            case 'subtract':
                result = subtract(a, b)
            case 'multiply':
                result = multiply(a, b)
            case 'devide':
                result = devide(a, b)
            case 'modulus':
                result = modulus(a, b)
            case 'power':
                result = power(a, b)
            case 'floordivision':
                result = floordivision(a, b)
            case 'and':
                result = And(a, b)
            case 'or':
                result = Or(a, b)
            case 'equal':
                result = equal(a, b)
            case 'notequal':
                result = notequal(a, b)
            case 'greater':
                result = greater(a, b)
            case 'less':
                result = less(a, b)
            case 'greaterequal':
                result = greaterequal(a, b)
            case 'lessequal':
                result = lessequal(a, b)

        if result is not None:
            print(f"The result of {perform} between {a} and {b} is: {result}")
            history.append(f"{perform}({a}, {b}) = {result}")

    else:
        print("Please write a valid operation")
        continue
