# factorial.py
def factorial(n):
    """
    Calculate the factorial of a number.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
