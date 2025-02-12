import math
# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) ** 대신 pow 함수 사용하기
# v1.4) pow 대신 함수 만들어 사용하기
def my_sqrt(a) -> float:
    epsilon = 1e-10
    guess = a
    while abs(guess * guess - a) > epsilon:
        guess = 0.5 * (guess + a / guess)  # 뉴턴-랩슨 공식 적용

    return guess

def my_pow(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    if e < 0:
        b = 1 / b
        e = e * -1

    result = 1

    i = int(e)
    f = e - i

    for _ in range(i):  # for k in range(e):
        result = result * b

    if f > 0:
        result = result * math.exp(f * math.log(b))

    return result


# def my_pow(a, b) -> float:
#     """
#     This function returns a^b
#     :param a: base number
#     :param b: exponent
#     """
#     result = 1
#     for k in range(b):
#         result *= a


def is_prime(num):
    """
    This function checks if a number is prime.
    If a number is prime, it returns True.
    """
    if num == 1:
        return False

    i = 2
    while i <= int(my_pow(num, 0.5)):
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