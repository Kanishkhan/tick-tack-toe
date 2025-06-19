import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\n")
    print("    1   2   3")
    print("  -------------")
    for i in range(3):
        print(f"{i+1} |", end=" ")
        for j in range(3):
            print(board[i][j] if board[i][j] != " " else " ", end=" | ")
        print("\n  -------------")
    print("\n")

def check_win(board, player):
    # Rows, Columns, Diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2-i] == player for i in range(3)]): return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(board, player):
    while True:
        try:
            row = int(input(f"{player}'s Turn - Enter row (1-3): ")) - 1
            col = int(input(f"{player}'s Turn - Enter column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That cell is already taken. Try again.")
            else:
                print("Invalid input! Enter numbers between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    clear_screen()
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        clear_screen()
        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!\n")
            return current_player
        elif check_draw(board):
            print("It's a draw!\n")
            return "Draw"

        current_player = "O" if current_player == "X" else "X"

def show_scoreboard(scoreboard):
    print("==== Scoreboard ====")
    print(f"Player X: {scoreboard['X']} Wins")
    print(f"Player O: {scoreboard['O']} Wins")
    print(f"Draws: {scoreboard['Draw']}\n")

def main():
    scoreboard = {"X": 0, "O": 0, "Draw": 0}
    while True:
        result = play_game()
        scoreboard[result] += 1
        show_scoreboard(scoreboard)
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing Tic-Tac-Toe!")
            break

if __name__ == "__main__":
    main()
