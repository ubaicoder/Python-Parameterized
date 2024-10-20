import sys

# Check if enough arguments are passed
if len(sys.argv) != 3:
    print("Please provide two numbers as command-line arguments.")
else:
    # Parse command-line arguments
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    # Perform addition and print the result
    print(f"Addition of {num1} & {num2} is {num1 + num2}")
