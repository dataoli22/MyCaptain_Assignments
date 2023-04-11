#Write a Python Program for Fibonacci numbers.

def fibonacci(n):
    # Initialize the first two terms
    a, b = 0, 1

    # Check if the number of terms is valid
    if n <= 0:
        print("Invalid input")
    elif n == 1:
        print(a)
    else:
        # Print the first two terms
        print(a, b, end=" ")

        # Generate the sequence
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c

# Test the function
fibonacci(10)  # Generate the first 10 Fibonacci numbers
