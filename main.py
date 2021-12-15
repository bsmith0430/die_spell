from classes import Player
import keyboard

# Game variables
number_of_players = int(input("How many players?: "))

player_health_points = number_of_players * 10
base_dice = 5
additional_dice = 0
status = "No status"
rolls_remaining = 3
actions_available = []

game_is_running = True

player_names = {}
for _ in range(number_of_players):
    print(f"Player {_ + 1} name:")
    player_name = input()
    player_names[f"player {_ + 1}"] = player_name

while game_is_running:
    if keyboard.is_pressed('q'):
        game_is_running = False
        print('Thanks for playing!')
        break
    