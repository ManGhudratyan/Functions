# Write a Python program to print the even numbers from a given list.

def evenNums(numbers):
    evenNumbers = [];
    for el in numbers:
        if (el % 2 == 0):
            evenNumbers.append(el);
    return evenNumbers;
    
ml = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print("Even numbers are:", evenNums(ml));