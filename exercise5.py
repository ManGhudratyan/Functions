# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def calcFact(number):
    if (type(number) != int):
        print('Write only integer.')
        return None;
    if (number < 1):
        return 1;
    fact = 1;
    for i in range(1, number + 1):
        fact *= i;
    return fact

print(calcFact(5));
print(calcFact(6));