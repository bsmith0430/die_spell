from classes import Player
import keyboard

# Game variables
number_of_players = int(input("How many players?: "))

player_health_points = number_of_players * 10
base_dice = 5
additional_dice = 0
status = "No status"
rolls_remaining = 3
locked_dice = []
actions_available = []


player_names = {}
for _ in range(number_of_players):
    print(f"Player {_ + 1} name:")
    player_name = input()
    player_names[f"player {_ + 1}"] = player_name

game_is_running = True
while game_is_running:
    if keyboard.is_pressed('q'):
        game_is_running = False
        print('Thanks for playing!')
        break

    for player in player_names:
        player = Player(player_names[player], player_health_points, base_dice, additional_dice,
                        status, rolls_remaining, actions_available)

        if player_health_points <= 0:
            print(f"{player_names[player]} has lost the game")
            game_is_running = False
            break

        user_input = input("What do you want to do? ")
        if user_input == "q":
            game_is_running = False
            print('Thanks for playing!')
            break

        if user_input == "roll":
            player.roll(player.base_dice, player.additional_dice, player.rolls_remaining, player.status, player.locked_dice)
