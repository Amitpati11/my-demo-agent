def get_prime_numbers(n):
    """Return a list of prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

get_prime_numbers(10)  # Example usage, returns [2, 3, 5, 7]
print(get_prime_numbers(20))  # Example usage, returns [2, 3, 5, 7, 11, 13, 17, 19]