import random
from contextlib import nullcontext
from tokenize import endpats

# d_s_p = {"위스키"

drinks = ["위스키", "와인", "소주", "고량주", "사케"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치", "광어회"]
prices = [50000, 30000, 5000, 7500]
amounts = [0 for i in range(len(drinks))]

drinks.append("사케")
snacks.append("광어회")
prices.append(25000)
amounts.append(0)
snacks[0] = "낙곱새"

total_price = 0

def print_menu_total_price(n):
    global total_price
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]}입니다')
    total_price += prices[n]
    return total_price

menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}'
menu_list = menu_list + f'{len(drinks)+1}) 아무거나 {len(drinks)+2}) 종료 : '

while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        break
    elif menu == len(drinks):
        print_menu_total_price(menu)


