def display_board(board):
    print("---------")
    print("|", board[0], board[1], board[2], "|")
    print("|", board[3], board[4], board[5], "|")
    print("|", board[6], board[7], board[8], "|")
    print("---------")

def check_win(board):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return board[pos[0]]
    return None

def check_draw(board):
    return " " not in board

def make_move(board, player):
    while True:
        move = input("Enter the coordinates: ")
        if not move.replace(" ", "").isdigit():
            print("You should enter numbers!")
        else:
            x, y = map(int, move.split())
            index = (x - 1) * 3 + y - 1
            if not 0 <= index <= 8:
                print("Coordinates should be from 1 to 3!")
            elif board[index] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                board[index] = player
                return

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = 0
    winner = None
    
    display_board(board)
    
    while not winner and not check_draw(board):
        make_move(board, players[current_player])
        display_board(board)
        winner = check_win(board)
        current_player = (current_player + 1) % 2
    
    if winner:
        print(f"{winner} wins")
    else:
        print("Draw")
    
play_game()
