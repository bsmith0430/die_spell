import random
class Player(object):
    # Game variables
    name = ""
    health_points = 0
    base_dice = 0
    additional_dice = 0
    status = ""
    rolls_remaining = 0
    locked_dice = []
    actions_available = []
    current_game_phase = ""

    def __init__(
            self,
            name,
            health_points, 
            base_dice,
            additional_dice,
            status, 
            rolls_remaining, 
            actions_available,
            locked_dice, 
            current_rolls, 
            current_game_phase
    ):

        self.name = name
        self.health_points = health_points
        self.base_dice = base_dice
        self.additional_dice = additional_dice
        self.status = status
        self.rolls_remaining = rolls_remaining
        self.actions = actions_available
        self.locked_dice = locked_dice
        self.current_rolls = current_rolls
        self.current_game_phase = current_game_phase

    def roll(
            self, 
            base_dice, 
            additional_dice,
            rolls_remaining, 
            status, 
            locked_dice, 
            current_rolls
    ):

        total_rolls = base_dice + additional_dice - len(locked_dice)

        if self.rolls_remaining > 0:
            current_rolls.clear()
            # Rolls the dice
            for _ in range(total_rolls):
                dice_roll = random.randint(1, 6)
                current_rolls.append(dice_roll)
            self.rolls_remaining -= 1
            current_rolls.sort()
            print(f"{self.name} rolled {current_rolls}")
            print(f"{self.name} has {self.rolls_remaining} rolls remaining")
            
    
    def build_spell(
            self, 
            locked_dice, 
            state
    ):
        
        spell = {}

        if state == "Build":

            for dice in locked_dice:
                if dice in spell:
                    spell[dice] += 1
                else:
                    spell[dice] = 1
            
            print(spell)


    def lock(
            self, 
            current_rolls, 
            locked_dice
    ):      
        
        is_locking = True

        while is_locking:
            if len(self.current_rolls) > 0:
                try:
                    print(f"Unlocked dice: {self.current_rolls}")
                    print(f"Locked dice: {self.locked_dice}")
                    dice_to_lock = int(input("Which dice do you want to lock? Hint: Use 0 index values to lock dice and -1 to stop locking dice: "))
                    if dice_to_lock == -1:
                        is_locking = False
                    if dice_to_lock in range(len(current_rolls)):
                        locked_dice.append(current_rolls[dice_to_lock])
                        current_rolls.remove(current_rolls[dice_to_lock])
                except ValueError:
                    print("Invalid input")
            if len(self.current_rolls) == 0:
                print(f"{self.name} has no dice to lock")
                is_locking = False

    def action_menu(
            self, 
            actions_available
    ):
                    
        print(f"{self.name}'s actions: {actions_available}")

        if len(actions_available) == 0:
            print(f"{self.name} has no actions available")

        if len(actions_available) > 0:
            action_value = input("What action do you want to use? ")
            if action_value == "back":
                # Needs to move us to the correct menu
                # Need to flesh this out more
                current_game_phase = self.current_game_phase

            try:
                action_value = int(action_value)

                if action_value in actions_available:
                    print(f"{self.name} used {action_value}")
                    self.actions_available.remove(action_value)
            except ValueError:
                print("Invalid input")
