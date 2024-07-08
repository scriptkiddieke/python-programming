# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for odd factors from 3 to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

# Finding all prime numbers between 1 to 250
prime_numbers = [num for num in range(1, 251) if is_prime(num)]

# Writing results to a file
file_path = 'results.txt'
with open(file_path, 'w') as file:
    for prime in prime_numbers:
        file.write(str(prime) + '\n')

print(f"Prime numbers between 1 to 250 saved to {file_path}")
