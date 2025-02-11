import math

# for dan in range(2, 10, 1):
#     for i in range(1, 10, 1):
#         print(f"{dan} x {i} = {dan * i}")
#
# dan = int(input("input dan: "))
# for i in range(1, 10, 1):
#     print(f"{dan} x {i} = {dan * i}")

n = int(input("input n: "))
is_prime = True

if n == 1:
    is_prime = False
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        is_prime = False
        print(f"{i} ")
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")





# if n >= 2:
#     count = 0
#     for i in range(2, n):
#         if n % i == 0:
#             # count += 1
#             is_prime = False
#             break
#         print(i, end=' ')
# else: is_prime = False

# if is_prime:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")
