class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Player {self.type}"