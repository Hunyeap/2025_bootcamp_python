# y = 3
# x = y * 9
# z = list(range(x))
# print(z)
# print(tuple(map(str, z)))

def my_range(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        # number += step
        number = number + step


r = my_range()
print(r, type(r))

for x in r:
    print(x)
for x in r:
    print(x)
for x in my_range(10, 19, 2):
    print(x)