def divide_numbers(a, b):
    """
    Divides two numbers with error handling.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None

# Example usage (can be removed in production)
if __name__ == "__main__":
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
    print(divide_numbers(10, "x"))