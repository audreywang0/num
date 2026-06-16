# // Even Strongly Pseudoperfect Numbers

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
       return omitted_factors

#    too low
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


for num in range(2, check_until, 2):
    lower_factor_list = get_lower_factors(num)
    factor_sum = sum_factors(num, lower_factor_list)
    goal_value = factor_sum-(2*num)
    result = check_value(num, lower_factor_list, goal_value, i=0)
    if result != False:
        omitted_factors = result
        print("Number:", num)
        print("Sum of factors:", factor_sum)
        if (omitted_factors == []):
            print("Omitted factors: None")
            print("Perfect number\n")
        else:
            print("Omitted factors: ", end="")
            for i in range(0, len(omitted_factors)-1, 2):
                print("(", omitted_factors[i], ",", num//(omitted_factors[i]), ")", sep="", end="")
            print("\n")