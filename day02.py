import math
# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) ** 대신 pow 함수 사용하기
# v1.4) pow 대신 함수 만들어 사용하기
def my_pow(a):
    epsilon = 1e-10
    guess = a
    while abs(guess * guess - a) > epsilon:
        guess = 0.5 * (guess + a / guess)  # 뉴턴-랩슨 공식 적용

    return guess

def is_prime(num):
    """
    This function checks if a number is prime.
    If a number is prime, it returns True.
    """
    if num == 1:
        return False

    i = 2
    while i <= int(my_pow(num)):
        if num % i == 0:
            return False
        i += 1

    return True


numbers = input("input n: ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

current = n1
while current <= n2:
    if is_prime(current):
        print(current, end=" ")  # 한 줄에 출력
    current += 1