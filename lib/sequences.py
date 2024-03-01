def print_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    while len(fibonacci_sequence) < n:  # Modify condition to check length of sequence
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print(fibonacci_sequence)

print_fibonacci(88)
