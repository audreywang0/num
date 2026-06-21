# Mersenne Prime Divisibility

import re

file_name = "even_sp.txt"
file = open(file_name, "r")
text = file.read()


def test_prime(number):
    prime = True
    if number < 2:
        prime = False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
            break
    return prime


mersenne_primes = []
for i in range(1, 50):
    if test_prime(i) == True:
        mersenne_num = (2**i) - 1
        if test_prime(mersenne_num) == True:
            mersenne_primes.append(mersenne_num)

for num in re.findall(r"Number:\s*(\d+)", text):
    num = int(num)
    divisible = False
    for mersenne_prime in mersenne_primes:
        if num % mersenne_prime == 0:
            print(num, "/", mersenne_prime, "=", num // mersenne_prime)
            divisible = True
    if divisible == False:
        print(num, ": None", sep="")
    print()


file.close()
