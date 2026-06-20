# All Strongly Pseudoperfect Numbers

check_until = 2000000


def get_lower_divisors(number):
    # Returns one lower divisor from each divisor pair
    lower_divisors = []

    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            lower_divisors.append(i)

    return lower_divisors


def sigma(number, lower_divisors):
    # Compute sum of all positive divisors of number
    total = 0
    for divisor in lower_divisors:
        pair = number // divisor
        if divisor == pair:
            total += divisor
        else:
            total += divisor + pair
    return total


def find_strongly_pseudo(number, lower_divisors, omission_target):
    # Stores omitted divisor totals that are reachable so far
    possible_totals = {0}

    for divisor in lower_divisors:
        paired_divisor = number // divisor

        # Sum contributed by omitting the divisor pair
        if divisor == paired_divisor:  # Perfect square
            pair_sum = divisor
        else:
            pair_sum = divisor + paired_divisor

        # Stores new totals made by omitting the current pair
        new_totals = set()

        for old_total in possible_totals:
            new_total = old_total + pair_sum

            # Valid total found
            if new_total == omission_target:
                return True

            # Keep partial totals that have not passed the target
            if new_total < omission_target:
                new_totals.add(new_total)

        # Add totals made using the current pair
        possible_totals = possible_totals | new_totals

    # Check whether the target omission total was reachable
    if omission_target in possible_totals:
        return True
    else:
        return False


for num in range(2, check_until + 1):
    lower_divisors = get_lower_divisors(num)

    # Skip primes
    if len(lower_divisors) == 1:
        continue

    # Never 2 (mod 3), 3 (mod 4)
    if num % 3 == 2 or num % 4 == 3:
        continue

    sigma_value = sigma(num, lower_divisors)

    # Omitted pairs must sum to sigma(n)-2n
    omission_target = sigma_value - (2 * num)

    if find_strongly_pseudo(num, lower_divisors, omission_target):
        print("Number:", num)
