# Odd Primitive Non-deficient Strongly Pseudoperfect Numbers
# A number n is primitive non-deficient, if n is non-deficient and every proper divisor of n is deficient.

check_until = 2000000

def get_proper_factors(number):
   proper_factor_list = []
   if number==1:
       return []
   

   proper_factor_list.append(1)
   for i in range(2, int(number**0.5)+1):
    if number % i == 0:
        pair = number//i
        # perfect square
        if i==pair:
            proper_factor_list.append(i)
        else:
            proper_factor_list.append(i)
            proper_factor_list.append(pair)
   return proper_factor_list

def add_proper_factors(proper_factor_list):
    sum = 0
    for i in range (0, len(proper_factor_list)):
        sum+=proper_factor_list[i]
    return sum

def test_deficient(factor):
#    adds factors of the factor of n 
   total = add_proper_factors(get_proper_factors(factor))
   if total<factor:
      return True
   else:
      return False

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
       return omitted_factors

# too low
    if goal_value<0:
        return False

   # Case 2: No more factors to consider, failed
    elif i == len(lower_factor_list):
       return False


   # Current factor and its corresponding pair
    factor = lower_factor_list[i]
    factor_pair = number//lower_factor_list[i]


   # Choice 1: Omit factor pair
   # Subtract both values from goalValue
   # Add them to omittedFactors
    if factor!=factor_pair:
       omit_factor = check_value(number, lower_factor_list, goal_value-factor -
                           factor_pair, i+1, omitted_factors+[factor, factor_pair])
    else: # Perfect Square
       omit_factor = check_value(number, lower_factor_list, goal_value-factor
                               , i+1, omitted_factors+[factor, factor_pair])


   # Choice 2: Keep factor pair
   # Do not change goalValue or omittedFactors
    keep_factor = check_value(number, lower_factor_list, goal_value, i+1, omitted_factors)


   # If either path succeeds, return list of omitted factors
    if omit_factor != False:
       return omit_factor
    elif keep_factor != False:
       return keep_factor
    else:
       return False # Both paths failed

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


for number in range(3, check_until, 2):
    lower_factor_list = get_lower_factors(number)
    if len(lower_factor_list)!=1: # num is not prime
        prime_factor_list = get_prime_factors(number)
        k=len(prime_factor_list)
        p=prime_factor_list[0]
        if p<=k:
            proper_factor_list = get_proper_factors(number)
            allDeficient = True
            for factor in proper_factor_list:
            #    if any factor is not deficient, changes allDeficient to false
                if test_deficient(factor)==False:
                    allDeficient=False
                    break
            # tests next num if not all factors are deficient
            if allDeficient==False:
                continue
            # at this point, all factors are deficient. now test if n is non-deficient.
            else:
                num_is_deficient = test_deficient(number)
                #    n is non-deficient and all its factors are deficient. now test if n is pseudoperfect.
            if num_is_deficient==False:
                factor_sum = sum_factors(number, lower_factor_list)
                goal_value = factor_sum-(2*number)
                result = check_value(number, lower_factor_list, goal_value, i=0)
                if result != False:
                    omitted_factors = result
                    print("Number:", number)
                    print("Sum of factors:", factor_sum)
                    if (omitted_factors == []):
                        print("Omitted factors: None")
                        print("Perfect number\n")
                    else:
                        print("Omitted factors: ", end="")
                        for i in range(0, len(omitted_factors)-1, 2):
                            print("(", omitted_factors[i], ",", number//(omitted_factors[i]), ")", sep="", end="")
                        print("\n")




# 1. get proper factors of n
# 2. test if each proper factor is deficient
# 3. test if n is non-deficient
# 4. test if n is strongly pseudoperfect