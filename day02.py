import math
# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) ** 대신 pow 함수 사용하기
def is_prime(num):
    """
    This function checks if a number is prime.
    If a number is prime, it returns True.
    """
    if num ==1 :
        return False

    i = 2
    while i <= int(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1

    return True


n = int(input("input n: "))

if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
