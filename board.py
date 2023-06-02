import chess

class Board:
    def __init__(self):
        self.state = [
            ["R_w", "N_w", "B_w", "K_w", "Q_w", "B_w", "N_w", "R_w"],
            ["P_w", "P_w", "P_w", "P_w", "P_w", "P_w", "P_w", "P_w"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P_b", "P_b", "P_b", "P_b", "P_b", "P_b", "P_b", "P_b"],
            ["R_b", "N_b", "B_b", "K_b", "Q_b", "B_b", "N_b", "R_b"]
        ]
        self.turn = "white"

    def move_piece(self, current, new):

        # gets index from notation

        current_x = ord(current[0]) - 64
        current_y = int(current[1])
        current_y -= 1
        current_x -= 1

        new_x = ord(new[0]) - 64
        new_y = int(new[1])
        new_x -= 1
        new_y -= 1

        board = self.state
        board[new_y][new_x] = board[current_y][current_x]
        board[current_y][current_x] = ""

        return board

    def is_legal(self, current, new):

        checked = False

        # is king checked in both
        for row in range(self.state):
            for col in range(i):

                # Straight

                if self.state[row][col] == "K_w":
                    for i in range(self.state):
                        if self.state[i][col] == "Q_b" or self.state[i][col] == "R_b":
                            checked = True
                    for i in range(self.state):
                        if self.state[row][i] == "Q_b" or self.state[i][col] == "R_b":
                            checked = True

                # diagonals

                    for i in range(self.state):
                        if row + i <= 8 and col + i <= 8:
                            if self.state[row + i][col + i] == "Q_b" or self.state[i][col] == "B_b":
                                checked = True
                    for i in range(self.state):
                        if row - i <= 0:
                            if self.state[row - i][col - i] == "Q_b" or self.state[i][col] == "B_b":
                                checked = True

                    # TODO finish diagonals
                    # TODO finish L


    def set_board(self, new_board):
        self.state = new_board

    def get_board(self):
        return self.state








b = Board()
b.move_piece("A2", "A3")
board = b.get_board()
for col in board:
    print(col)

