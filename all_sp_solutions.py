# All Strongly Pseudoperfect Numbers - Solutions

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


def find_solutions(number, lower_divisor_list, goal_value):
    # Each entry has the form: [omitted total, omitted divisors]
    possible_totals = [[0, []]]

    for divisor in lower_divisor_list:
        paired_divisor = number // divisor

        # Symmetric divisor pair
        if divisor == paired_divisor:  # Perfect square
            pair_sum = divisor
            pair = [divisor]
        else:
            pair_sum = divisor + paired_divisor
            pair = [divisor, paired_divisor]

        # New omission totals by omitting the current pair
        new_totals = []

        for (
            old_total,
            old_omitted_divisors,
        ) in (
            possible_totals
        ):  # adds current pair to each old total to get all possible totals
            new_total = old_total + pair_sum

            # Keep totals that haven't exceeded the target
            if new_total <= goal_value:
                new_omitted_divisors = (
                    old_omitted_divisors + pair
                )  # adds current pair to old_omitted_divisors
                new_totals.append(
                    [new_total, new_omitted_divisors]
                )  # adds solution to new_totals

        possible_totals.extend(new_totals)

    all_solutions = []

    for total, omitted_divisors in possible_totals:
        if total == goal_value:
            all_solutions.append(omitted_divisors)

    return all_solutions


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

    solutions = find_solutions(num, lower_divisors, omission_target)

    if len(solutions) > 0:
        print("Number:", num)

        if [] in solutions:
            print("Number of solutions: 1")
            print("Omitted divisors: None")
            print("Perfect number")
        else:
            print("Number of solutions:", len(solutions))
            for solution in solutions:
                print("Omitted divisors:", solution)

        print("\n")
