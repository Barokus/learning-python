import random

def generation_number():
    return random.randint(1.100)

def play_game():
    number_to_guess = generation_number()
    attempts = []

    while True:
        guess = int(input("Введите число от 1 до 100: "))
        attempts.append(guess)

        if guess < number_to_guess:
            print("Больше!")

        elif guess > number_to_guess:
            print("Меньше!")

        else:
            print(
                f"Вы угадали число {number_to_guess} "
                f"за {len(attempts)} попыток."
            )
            print ("Ваши попытки:", attempts)
            break

        def main():
            play_game()

        main()