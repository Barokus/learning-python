import json
import random

def play_game():
    number_to_guess = random.randint(1,100)
    attempts = []

    while True:
        guess = int(input("Введите число от 1 до 100: "))
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

def save_result_to_file(result):
    with open("game_result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

def load_result_from_file():
    with open("game_result.json", "r", encoding="utf-8") as file:
        result = json.load(file)
    return result

def main():
    game_result = play_game()
    save_result_to_file(game_result)    

    print("Текущий результат: ")
    print(game_result)

    print("\nРезультат из файла: ")
    loaded_result = load_result_from_file()
    print(loaded_result)

    save_result_to_file(game_result)
    
main()