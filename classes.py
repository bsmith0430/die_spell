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

    def __init__(self, name, health_points, base_dice,
                additional_dice, status, rolls_remaining, actions_available,
                locked_dice, current_rolls):
        self.name = name
        self.health_points = health_points
        self.base_dice = base_dice
        self.additional_dice = additional_dice
        self.status = status
        self.rolls_remaining = rolls_remaining
        self.actions = actions_available
        self.locked_dice = locked_dice
        self.current_rolls = current_rolls

    def roll(self, base_dice, additional_dice,
            rolls_remaining, status, locked_dice, current_rolls):


        total_rolls = base_dice + additional_dice - len(locked_dice)

        if self.rolls_remaining > 0:
            # Rolls the dice
            for _ in range(total_rolls):
                dice_roll = random.randint(1, 6)
                current_rolls.append(dice_roll)
                self.rolls_remaining -= 1
            current_rolls.sort()
            print(f"{self.name} rolled {current_rolls}")
