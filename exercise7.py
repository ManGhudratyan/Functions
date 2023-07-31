# Write a Python function that accepts a string and counts the number of upper and lower case letters.

def findUpperLowerCount(mstr):
    md = {"upper_count" : 0, "lower_count" : 0, "other" : 0}
    
    for el in mstr:
        if (el.isupper()):
            md["upper_count"] += 1;
        elif (el.islower()):
            md["lower_count"] += 1;
        else:
            md["other"] += 1;
    return md
print(findUpperLowerCount('Hello World!'));
