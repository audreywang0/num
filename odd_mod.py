# Odd Strongly Pseudoperfect Numbers - Modular 3-25

import re

file = open("odd_output.txt", "r")
text = file.read()
for num in re.findall(r"Number:\s*(\d+)", text):
    num = int(num)
    for i in range (3,26):
        print(num, "mod", i, "=", num%i)
    print("\n")
# numbers = [int(x) for x in re.findall(r"Number:\s*(\d+)", text)]
# /s=whitespace, *=zero or more, parentheses=returns whats inside the parentheses (d+), /d=digit, +=one or more

file.close()
