class Player(object):
    # Game variables
    name = ""
    health_points = 0
    base_dice = 0
    additional_dice = 0
    status = ""
    rolls_remaining = 0
    actions_available = []

    def __init__(self, name, health_points, base_dice, 
                additional_dice, status, rolls_remaining, actions_available):
        self.name = name
        self.health_points = health_points
        self.base_dice = base_dice
        self.additional_dice = additional_dice
        self.status = status
        self.rolls_remaining = rolls_remaining
        self.actions = actions_available

        
