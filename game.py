
class Game:
    def __init__(self, board_size, win_length):
        self.win_length = win_length
        self.board_size = board_size
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

    def running(self, row, col, piece):
        '''
        given the placement of the most recent piece, check to see if that player has won
        '''
        r = row
        c = col

        direction_pairs = [
            [(0, 1), (0, -1)],
            [(1, 0), (-1, 0)], 
            [(1, 1), (-1, -1)], 
            [(1, -1), (-1, 1)]
        ]

        for dir_pair in direction_pairs:
            count = 1 # count starts at 1 becuase the starting place is the right piece
            first_dir = dir_pair[0]
            second_dir = dir_pair[1]

            r = row
            c = col
            while count < self.win_length: # check first dir
                r += first_dir[0]
                c += first_dir[1]
                if r in range(self.board_size) and c in range(self.board_size) and self.board[r][c] == piece:
                    count += 1
                else:
                    break
            r = row
            c = col
            while count < self.win_length: # check second dir

                r += second_dir[0]
                c += second_dir[1]
                # print(r, c)
                if r in range(self.board_size) and c in range(self.board_size) and self.board[r][c] == piece:
                    count += 1
                else:
                    break
            
            if count >= self.win_length:
                if piece == "O":
                    winner = "Player 1"
                else:
                    winner = "Player 2"
                return winner, False
        return None, True



    def dump(self):
        '''
        Displays the current game board state
        '''
        for i in range(self.board_size):
            row = ""
            for j in range(self.board_size - 1):
                if self.board[i][j] is None:
                    row += "   |"
                else:
                    row += " " + self.board[i][j] + " |"
            if self.board[i][-1] is None:
                row += "   "
            else:
                row += " " + self.board[i][-1] + " "

            print(row)

            if i < self.board_size - 1:
                separator = ["----" for _ in range(self.board_size)]
                print(''.join(separator))

if __name__ == "__main__":
    player1 = True

    # users will be able to define these parameters
    board_size = 3
    win_length = 3
    pieces = {
        True: "O", 
        False: "X"
    }
    
    game = Game(board_size, win_length)
    print(game.board)

    print("WELCOME TO TIC TAC TOE!!")
    print("_______________________\n")

    print("Current Game Board: \n")
    game.dump()

    if player1: # if player 1's turn
        player = "Player 1"
    else:
        player = "Player 2"
    piece = pieces[player1]
    
    while True: # check for valid move
        row = int(input(f"{player} select the row in which you would like to place a piece: "))
        col = int(input(f"{player} select the column in which you would like to place a piece: "))

        if row in range(game.board_size) and col in range(game.board_size) and game.board[row][col] is None:
            break
        else:
            print("Invalid Piece Placement, try again")

    game.board[row][col] = piece
    game.dump()

    player1 = not player1

    winner, game_in_progress = game.running(row, col, piece)

    while game_in_progress: # if game is still going
        if player1: # if player 1's turn
            player = "Player 1"
        else:
            player = "Player 2"
        piece = pieces[player1]
        
        while True:
            row = int(input(f"{player} select the row in which you would like to place a piece: "))
            col = int(input(f"{player} select the column in which you would like to place a piece: "))
            if row in range(game.board_size) and col in range(game.board_size) and game.board[row][col] is None:
                break
            else:
                print("Invalid Piece Placement, try again")

        game.board[row][col] = piece
        game.dump()

        player1 = not player1

        winner, game_in_progress = game.running(row, col, piece)

    print("Game Over")
    print(f"{winner} WINS!")


    




    


