# Write a Python function to check whether a number falls within a given range.

def checkRangeNum(n):
    if n in range(10, 50):
        return ('Number is in the range.');
    else:
        return ('Number is not in the range.');
        
print(checkRangeNum(12));
print(checkRangeNum(60))