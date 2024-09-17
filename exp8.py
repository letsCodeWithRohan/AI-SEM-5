def print_board():
    """Prints the current state of the game board."""
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    """Handles a player's move, ensuring valid input and preventing invalid moves."""
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))

    while True:
        choice = int(input("Enter your move (1-9): ").strip())
        if 1 <= choice <= 9 and board[choice - 1] == " ":
            board[choice - 1] = icon
            break
        else:
            print("Invalid move. Please enter a number between 1 and 9.")

def is_victory(icon):
    """Checks if a player has won the game."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)            # Diagonals
    ]

    for combination in winning_combinations:
        if all(board[index] == icon for index in combination):
            return True
    return False

def is_draw():
    """Checks if the game is a draw."""
    return " " not in board

board = [" " for x in range(9)]

while True:
    print_board()
    player_move("X")
    print_board()

    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

    player_move("O")
    print_board()

    if is_victory("O"):
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
