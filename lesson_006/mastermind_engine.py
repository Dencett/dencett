from random import randint

total_number = []


def guess_number():
    global total_number
    total_number.append(randint(1, 9))
    i = 0
    while True:
        number = randint(0, 9)
        if number not in total_number:
            total_number.append(number)
            i += 1
        if i == 3:
            break
    print(total_number)  # NOTE а это здесь нужно для отладочных целей ;)


def check_number(user_number):
    return total_number == user_number


def fun_bulls_and_cows(user_number):
    bull, cow = 0, 0
    for x in range(4):
        if user_number[x] == total_number[x]:
            bull += 1
        elif user_number[x] in total_number:
            cow += 1
    return bull, cow


def end_game():
    total_number.clear()
    guess_number()

