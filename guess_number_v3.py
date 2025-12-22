import random

def play_game():
    number_to_guess = random.randit(1,100)
    attempts = []

    while True:
        guess = int(input("Введите число от 1 до 100"))
        attempts.append(guess)

        if guess < number_to_guess:
            print ("Больше!")

        elif guess > number_to_guess:
            print("Меньше!")

        else:
            print("Угадал!")
            break

    result = {
        "number": number_to_guess,
        "attempts_count": len(attempts),
        "attempts": attempts
    }

    return result

def main():
    game_result = play_game()

    print("Результат игры:")
    print(game_result)
    
main()