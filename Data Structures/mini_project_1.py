import random as rnd

player_health = 100
enemy_health = 100
#Dictionary with text key and Tuples value
moves = {"normal": (0, -20),
         "special": (5, -10),
         "heal": (15,0),
         "last stand": (-15,-30)}

def report(player_health, enemy_health):
    print(f"""Player health: {player_health}\nEnemy health: {enemy_health}""")

def check_game_over(player_health, enemy_health):
    if player_health <= 0 < enemy_health:
        print("Game Over! Enemy Wins!")
        return False
    elif player_health > 0 >= enemy_health:
        print("Game Over! Player Wins!")
        return False
    elif player_health <= 0 >= enemy_health:
        print("Game Over! Tie!")
        return False
    else:
        return True


report(player_health, enemy_health)

current_turn = 1

running = True
while running:
    #Player Turn
    if current_turn == 1:
        print("PLAYER TURN")

        valid_input = False
        while not valid_input:
            player_input = input("Select move...\n")
            valid_input = player_input.lower() in list(moves.keys()) or player_input.lower() == 'quit'
            if not valid_input:
                print("Invalid input. Try again...")
            # Quit Game
            if player_input.lower() == 'quit':
                running = False
                print("Goodbye!")
                break

            selected = moves[player_input.lower()]
            print("You selected:", player_input)
            player_health += selected[0]
            enemy_health += selected[1]

    elif current_turn == -1:
        print("Enemy TURN")
        enemy_input = rnd.randint(0, 3)
        selected = moves[list(moves.keys())[enemy_input]]
        print("Enemy selected: ", list(moves.keys())[enemy_input])

        enemy_health += selected[0]
        player_health += selected[1]

    report(player_health, enemy_health)
    running = check_game_over(player_health, enemy_health)
    current_turn *= -1
