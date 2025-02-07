def filter_prime(numbers):
    
    primes = []

    for num in numbers:
        if num < 2:
            continue
        
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)

    return primes


numbers = list(map(int, input().split()))

print(filter_prime(numbers))