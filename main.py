from classes import Player
import keyboard

# Game variables
number_of_players = int(input("How many players?: "))

player_health_points = 30
base_dice = 5
additional_dice = 0
status = "No status"
rolls_remaining = 3
locked_dice = []
actions_available = []
current_rolls = []
current_game_phase = "Upkeep"

player_names = {}
for _ in range(number_of_players):
    print(f"Player {_ + 1} name:")
    player_name = input()
    player_names[f"player {_ + 1}"] = player_name

game_is_running = True
while game_is_running:

    for player in player_names:
        player = Player(player_names[player], player_health_points, base_dice, additional_dice,
                        status, rolls_remaining, actions_available, locked_dice, current_rolls, current_game_phase)

        if player_health_points <= 0:
            print(f"{player_names[player]} has lost the game")
            game_is_running = False
            break

        user_input = input("What do you want to do? ")
        # if user_input == "quit" or user_input == "q":
        #     game_is_running = False
        #     print('Thanks for playing!')
        #     break

        # if user_input == "roll":
        #     player.roll(player.base_dice, player.additional_dice, player.rolls_remaining, player.status, player.locked_dice, player.current_rolls)

        # if user_input == "action":
        #     player.action_menu(player.actions_available)

        match user_input:
            case "quit":
                game_is_running = False
                print('Thanks for playing!')
                break
            case "roll":
                player.roll(player.base_dice, player.additional_dice, player.rolls_remaining, player.status, player.locked_dice, player.current_rolls)
            case "action":
                player.action_menu(player.actions_available)
            case "lock":
                player.lock(player.current_rolls, player.locked_dice)