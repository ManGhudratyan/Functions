# Write a Python function to multiply all the numbers in a list.

def calcMult(numbers):
    mult = 1;
    for i in numbers:
        mult *= i;
    return mult
    
multNums = calcMult((8, 2, 3, -1, 7));
print('Multiply all the numbers in a list are :', multNums);