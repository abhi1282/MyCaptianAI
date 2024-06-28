def fibonacci_sequence(limit):
    fib_sequence = [0, 1]
    
    for i in range(2, limit):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_fib)
    
    return fib_sequence


limit = 20
fibonacci_numbers = fibonacci_sequence(limit)
print("Fibonacci numbers up to limit", limit, ":", fibonacci_numbers)
