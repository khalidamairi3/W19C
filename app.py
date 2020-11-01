import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")
print("Wall is represented by *")
print("Enemy is represented by #")
print("Coin is represented by $")
print("The game has 15 inner wall, 10 enemies and 10 coins")
print("You can move to empty and coin squares")
print("You can earn one coin when you move to a coin square")
print("You are not allowed to move to wall squares")
print("You will lose the game if you hit an enemy square")
print("Enemies will move randomly everytime you move")
print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
board = gameboard.GameBoard()
player = player.Player(9,7)

# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

while True:
    board.randomEnemies(player.rowPosition, player.columnPosition)
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    if selection=="w":
        if board.checkMove(player.rowPosition-1,player.columnPosition):
            player.moveUp() 
            board.collectCoins(player.rowPosition,player.columnPosition)
    elif selection == "s":
        if board.checkMove(player.rowPosition+1,player.columnPosition):
            player.moveDown()
            board.collectCoins(player.rowPosition,player.columnPosition)
    elif selection == "a":
        if board.checkMove(player.rowPosition,player.columnPosition-1):
            player.moveLeft()
            board.collectCoins(player.rowPosition,player.columnPosition)
    elif selection == "d":
        if board.checkMove(player.rowPosition,player.columnPosition+1):
            player.moveRight()
            board.collectCoins(player.rowPosition,player.columnPosition)
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("Congrrats, you won")
        break
    if board.checkLose(player.rowPosition, player.columnPosition):
        print("you Lost")
        break
    # Check if the player has won, if so print a message and break the loop!

print ("you collected ",board.coins," coins")


  
    