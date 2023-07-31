# Write a Python function to find the maximum of three numbers.

def findMax(a,b,c):
    if (a >= b and a >= c):
        return a;
    elif(b >= a and b >= c):
        return b;
    else:
        return c;

maxNum = findMax(15,30,20);
print("The maximum of the three numbers is:", maxNum);