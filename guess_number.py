import random
number_to_guess = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("Введите число от 1 до 100: "))
    attempts += 1

    if guess < number_to_guess:
        print("Больше!")

    elif guess > number_to_guess:
        print("Меньше!")

    else:
        print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
        break