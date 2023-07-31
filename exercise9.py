# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def checkPrime(number):
    isPrime = True;
    if (number == 1):
        return False;
    elif (number == 2):
        return True;
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i == 0):
                isPrime = False;
                break;
    if (isPrime):
        return True;
    else:
        return False

print(checkPrime(11));
print(checkPrime(15));
