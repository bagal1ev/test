import random

# Начальное приветствие и создание игроков
def create_player():
    name = input("Введите имя участника: ")
    while True:
        try:
            start_balance = int(input("Введите начальный баланс в $: "))
            if start_balance > 0:
                break
            else:
                print("Баланс должен быть больше 0.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")
    return {"name": name, "balance": start_balance, "target": start_balance * 5}

# Функция для игры "Монетка".
def play_coin_toss(player):
    bet = int(input("Введите ставку на игру 'Монетка': $"))
    if bet > player["balance"]:
        print("Недостаточно средств.")
        return
    outcome = random.choice(["Орел", "Решка"])
    choice = input("Выберите 'Орел' или 'Решка': ").capitalize()
    if choice == outcome:
        player["balance"] += bet
        print(f"Вы угадали! Выпал {outcome}. Ваш баланс: ${player['balance']}")
    else:
        player["balance"] -= bet
        print(f"Вы не угадали. Выпал {outcome}. Ваш баланс: ${player['balance']}")

# Функция для игры "Кубик"
def play_dice(player):
    bet = int(input("Введите ставку на игру 'Кубик': $"))
    if bet > player["balance"]:
        print("Недостаточно средств.")
        return
    roll = random.randint(1, 6)
    guess = int(input("Угадайте число (от 1 до 6): "))
    if guess == roll:
        player["balance"] += bet * 5
        print(f"Вы угадали! Выпало {roll}. Ваш баланс: ${player['balance']}")
    else:
        player["balance"] -= bet
        print(f"Вы не угадали. Выпало {roll}. Ваш баланс: ${player['balance']}")

# Проверка на победу
def check_winner(players):
    for player in players:
        if player["balance"] >= player["target"]:
            print(f"\nПоздравляем, {player['name']} достиг баланса в {player['target']}$ и выиграл!")
            return player
    return None

# Основная функция игры
def main():
    players = [create_player() for _ in range(2)]
    
    while True:
        for player in players:
            print(f"\nХод игрока {player['name']} (Баланс: ${player['balance']})")
            print("Меню:")
            print("1. Играть в Монетку")
            print("2. Играть в Кубик")
            print("3. Выйти из игры")
            
            choice = input("Выберите действие: ")
            
            if choice == "1":
                play_coin_toss(player)
            elif choice == "2":
                play_dice(player)
            elif choice == "3":
                print(f"{player['name']} вышел из игры.")
                return
            else:
                print("Неверный выбор. Попробуйте снова.")
            
            # Проверка победителя
            if check_winner(players):
                return

# Запуск программы
if __name__ == "__main__":
    main()
