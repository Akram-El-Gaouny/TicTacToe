import enum
class gameState(enum.Enum):
    X_win = "X - wins the game!"
    O_win = "O - wins the game!"
    Draw = "It's a draw"
    Ongoing = "You can still play!"