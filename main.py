from classes import Player
from utils import pre_roll_phase_input, roll_phase_input, spell_building_phase_input, spell_casting_phase_input
import keyboard

# Game variables
number_of_players = int(input("How many players?: "))

player_health_points = 30
base_dice = 5
additional_dice = 0
status = "No status" # "No status", "Burned", "Shocked", "Frozen", "Vulnerable", "Poinsoned", "Pacified"
rolls_remaining = 3
locked_dice = []
actions_available = []
current_rolls = []
current_game_phase = "rolling" # pre_roll, rolling, spell_building, spell_casting

player_names = {}
for _ in range(number_of_players):
    print(f"Player {_ + 1} name:")
    player_name = input()
    player_names[f"player {_ + 1}"] = player_name

game_is_running = True
while game_is_running:

    # Game loop
    for player in player_names:
        player = Player(
            player_names[player], 
            player_health_points, 
            base_dice, 
            additional_dice,
            status, 
            rolls_remaining, 
            actions_available, 
            locked_dice, 
            current_rolls, 
            current_game_phase
        )

        if player.player_health_points <= 0:
            print(f"{player_names[player]} has lost the game")
            del player_names[player]

        if len(player_names) == 1:
            print(f"{player_names[player]} has won the game")
            game_is_running = False
            break

        while current_game_phase == "pre_roll":
            pre_roll_phase_input(player)
        while current_game_phase == "rolling":
            roll_phase_input(player)
        while current_game_phase == "spell_building":
            spell_building_phase_input(player)
        while current_game_phase == "spell_casting":
            spell_casting_phase_input(player)    
        