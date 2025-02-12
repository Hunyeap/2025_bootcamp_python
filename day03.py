import random

# 딕셔너리를 리스트로 변환
drinks = ["위스키", "와인", "소주", "고량주", "사케"]
foods = ["초콜릿", "치즈", "삽겹살", "양꼬치", "광어회"]

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')

    if menu in ['1', '2', '3', '4', '5']:
        index = int(menu) - 1
        print(f'{drinks[index]}에 어울리는 안주는 {foods[index]} 입니다')
    elif menu == '6':
        random_index = random.randint(0, len(drinks) - 1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')
    elif menu == '7':
        print('다음에 또 오세요')
        break