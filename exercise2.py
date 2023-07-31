# Write a Python function to sum all the numbers in a list.

def calcSum(numbers):
    msum = 0;
    for i in numbers:
        msum += i;
    return msum;
    
msum = calcSum((8, 2, 3, 0, 7));
print("Sum all the numbers in a list are :", msum);