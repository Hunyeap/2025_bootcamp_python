import math

def is_prime(num):
    """
    This function checks if a number is prime.
    if a number is prime, it returns True.
    """
    if num >= 2:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    else:
        return False
    return True


n = int(input("input n: "))

if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
