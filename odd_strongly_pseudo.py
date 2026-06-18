# // Odd Strongly Pseudoperfect Numbers

check_until = 2000000

def get_lower_factors(number):
   lower_factor_list = []
   for i in range(1, int(number**0.5)+1):
       if number % i == 0:
           lower_factor_list.append(i)
   return lower_factor_list



def sum_factors(number, lower_factor_list):
    total = 0
    for factor in lower_factor_list:
        pair = number // factor
        if factor==pair:
            total += factor
        else:
           total += factor + pair
    return total



def check_value(number, lower_factor_list, goal_value, i=0, omitted_factors=None):
    if omitted_factors == None:
       omitted_factors = [] # Initialize omittedFactors the first time the function runs (aka once for each number)


   # Case 1: Goal reached
    if goal_value == 0:
       return [omitted_factors]
   
   # Case 2: Too low
    if goal_value<0:
        return []

   # Case 3: No more factors to consider, failed
    if i == len(lower_factor_list):
       return []


   # Current factor and its corresponding pair
    factor = lower_factor_list[i]
    factor_pair = number//factor

    all_solutions=[]

   # Choice 1: Omit factor pair
   # Subtract both values from goalValue
   # Add them to omittedFactors
    if factor!=factor_pair:
       all_solutions += check_value(number, lower_factor_list, goal_value - factor - factor_pair, 
                                    i+1, omitted_factors+[factor, factor_pair])
    else: # Perfect Square
       all_solutions += check_value(number, lower_factor_list, goal_value-factor
                               , i+1, omitted_factors+[factor])


   # Choice 2: Keep factor pair
   # Do not change goalValue or omittedFactors
    all_solutions += check_value(number, lower_factor_list, goal_value, i+1, omitted_factors)

    return all_solutions


def get_prime_factors(number):
    p=2
    prime_factor_list = []
    while p<=number**0.5:
        if number%p==0:
            prime_factor_list.append(p)
            while number%p==0:
                number=number//p
        p+=1
        # adds last prime factor (remaining "number")
    if number>1:
        prime_factor_list.append(number)
    return prime_factor_list


for num in range(1, check_until, 2):
    lower_factor_list = get_lower_factors(num)
    if len(lower_factor_list)!=1: # num is not prime
        prime_factor_list = get_prime_factors(num)
        k=len(prime_factor_list)
        p=prime_factor_list[0]
        if p<=k:
            factor_sum = sum_factors(num, lower_factor_list)
            goal_value = factor_sum-(2*num)
            results = check_value(num, lower_factor_list, goal_value, i=0)
            if results:
                print("Number:", num)
                print("Sum of factors:", factor_sum)
                print("Number of solutions:", len(results))
                for solution in results:
                    if solution==[]:
                        print("Omitted factors: None")
                        print("Perfect number")
                    else:
                        print("Omitted factors:", solution)
                print("\n")