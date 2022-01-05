from classes import Player

def pre_roll_phase_input():
    pass

def roll_phase_input(player):
    user_input = input("What do you want to do? ")
        
    match user_input:
        case "action":
            player.action_menu(
                player.actions_available
        )
        case "roll":
            player.roll(
                player.base_dice, 
                player.additional_dice, 
                player.rolls_remaining, 
                player.status, 
                player.locked_dice, 
                player.current_rolls
        )
        case "lock":
                player.lock(
                player.current_rolls, 
                player.locked_dice
        )

def spell_building_phase_input():
    pass

def spell_casting_phase_input():
    pass

