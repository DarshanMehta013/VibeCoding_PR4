def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Sum: {add_two_numbers(x, y)}")
    except ValueError:
        print("Please enter valid numeric values.")
