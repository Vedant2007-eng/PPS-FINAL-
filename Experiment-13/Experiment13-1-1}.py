# # Write your code here......

# n = int(input())

# if n > 0:
# 	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
# 	print(' '.join(map(str, fib_series)))
# else:
# 	print("Please enter a positive integer")

# Main program

import fibonacci_module

n = int(input())

if n > 0:
    fib_series = fibonacci_module.generate_fibonacci_sequence(n)
    print(' '.join(map(str, fib_series)))
else:
    print("Please enter a positive integer")

# Module to generate Fibonacci sequence

def generate_fibonacci_sequence(max_value):
    sequence = []
    
    a, b = 0, 1
    while a <= max_value:
        sequence.append(a)
        a, b = b, a + b
    
    return sequence
