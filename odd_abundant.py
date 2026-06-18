# Odd Abundant Numbers

check_until = 2000

def addFactors(num):
    add = 0
    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            pair = num//i
            if pair==i:
                add+=i
            else:
                add+=i+pair
    return ad

for num in range (1, check_until, 2):
    sum = addFactors(num)
    if sum>2*num:
        print(f"Number:", num)
        print(f"Sum:   ", sum, "\n")