import random

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
print("Первый, кто наберёт 3 победы, выигрывает!")

player_wins = 0
computer_wins = 0
choices = ["камень", "ножницы", "бумага"]

while player_wins < 3 and computer_wins < 3:
    print("\n--- Новый раунд ---")
    player_choice = input("Выберите: камень, ножницы или бумага (или 'выход' для завершения): ").lower()

    if player_choice == 'выход':
        print("Вы вышли из игры.")
        break

    if player_choice not in choices:
        print("Некорректный ввод. Попробуйте снова.")
        continue

    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья в этом раунде!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        player_wins += 1
        print("Вы выиграли этот раунд!")
    else:
        computer_wins += 1
        print("Компьютер выиграл этот раунд!")

    print(f"Счёт: Вы {player_wins} — {computer_wins} Компьютер")

if player_wins == 3:
    print("Поздравляем! Вы выиграли игру!")
elif computer_wins == 3:
    print("Компьютер выиграл игру! Попробуйте ещё раз.")