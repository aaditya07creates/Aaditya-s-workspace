import os
import time
import psutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_prime(n, known_primes):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 10 in (0, 5):
        return False

    for prime in known_primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

def find_primes():
    largest_prime = 0
    prime_count = 0
    checked_count = 0
    number = 3  # Start checking from the first odd prime
    known_primes = [2]  # Start with known prime 2
    process = psutil.Process()  # Create process instance to monitor its memory usage

    while True:
        if is_prime(number, known_primes):
            largest_prime = number
            prime_count += 1
            known_primes.append(number)  # Store the found prime

        checked_count += 1

        # Print results every 10,000 checks
        if checked_count % 10000 == 0:
            ram_usage_gb = process.memory_info().rss / (1024 ** 3)  # RAM used by this program in GB
            clear_screen()
            #print(f"Highest Prime Found: {largest_prime}")
            print(f"Prime Count: {prime_count}")
            print(f"Checked Numbers: {checked_count}")
            #print(f"Prime Count: {prime_count}")
            print(f"Program RAM Usage: {ram_usage_gb:.2f} GB")

        number += 2  # Only check odd numbers

if __name__ == "__main__":
    start_time = time.time()
    find_primes()
