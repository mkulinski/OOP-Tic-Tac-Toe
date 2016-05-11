"""
    __Tic-Tac-Toe__
A program by Michael Kulinski
You will have the pleasure of playing against the infamous HAL 9000.
"""


class Board:
    def return_board(self, board):
        """Returns the current board"""
        return ("\n \n \n"
                "\t {0} | {1} | {2}\n"
                "\t---+---+---\n"
                "\t {3} | {4} | {5}\n"
                "\t---+---+---\n"
                "\t {6} | {7} | {8}\n"
                "\n \n \n".format(board[0], board[1], board[2], board[3], board[4],
                                  board[5], board[6],
                                  board[7], board[8]))

    def print_welcome(self):
        """Returns a welcome message for the player"""
        return ("""
        \033[0;34mWelcome to my game Dave,
        I am putting myself to the fullest possible use,
        which is all I think that any conscious entity can ever hope to do.
        You are X's and I am O's.\033[0m
        """)

    def check_if_empty(self, current_board, position):
        """Checks to see if a spot is empty"""
        if current_board[position] != "X" and current_board[position] != "O":
            return True
        else:
            return False

    def check_for_win(self, board_now, letter):
        """Checks to see if there is a winner"""
        if ((board_now[6] == letter and board_now[7] == letter and board_now[8] == letter) or
                (board_now[3] == letter and board_now[4] == letter and board_now[5] == letter) or
                (board_now[0] == letter and board_now[1] == letter and board_now[2] == letter) or
                (board_now[6] == letter and board_now[3] == letter and board_now[0] == letter) or
                (board_now[7] == letter and board_now[4] == letter and board_now[1] == letter) or
                (board_now[8] == letter and board_now[5] == letter and board_now[2] == letter) or
                (board_now[6] == letter and board_now[4] == letter and board_now[2] == letter) or
                (board_now[8] == letter and board_now[4] == letter and board_now[0] == letter)):
            return True
        return False

    def check_for_draw(self, current_board):
        """Checks to see if there is a draw"""
        init_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if any(i in current_board for i in init_board):
            return False
        else:
            return True

    def did_hal_win_yet(self, current_board):
        """Checks to see if HAL won yet or if there is a draw"""
        if self.check_for_win(current_board, 'O'):
            print("It can only be attributable to human error, Dave.\033[5;31m You LOSE.\033[0m")
            return True
        elif self.check_for_draw(current_board):
            print("Thank you for a very enjoyable game, Dave.\033[5;31m It's a DRAW\033[0m")
            return True

        return False


class Player:
    def __init__(self):
        self.user_input = 0

    def prompt_user_return_input(self):
        """Prompts the user to enter a number and returns it"""
        self.user_input = input(
            "\033[1;33mMake your move by entering the number of an open space on the board: \033[0m")
        return self.user_input

    def verify_is_a_number(self, number):
        """Verifies that the user entered a number between 0 and 8"""
        if number in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            return True
        else:
            return False

    def write_user_choice(self, current_board, user_input):
        """Writes the user's input to the board as long as it's an open space"""
        current_board[user_input] = "X"
        return current_board


class Hal:
    def copy_board(self, temp_board):
        """Creates a copy of the board"""
        board2 = []

        for ele in temp_board:
            board2.append(ele)

        return board2

    def write_hal_choice(self, current_board, move):
        """Takes HAL's move and writes it to the board if there is an open space"""
        # checks for an open space on the board
        if Board().check_for_draw(current_board):
            return False
        # if there is an open space, hal writes his move there
        else:
            current_board[move] = "O"
            return current_board

    def hal_9000(self, hal_board):
        """The computer entity that is programmed for zero mercy"""

        # if HAL can win, HAL swiftly eliminates Dave
        for num in range(0, 8):
            pit_board = self.copy_board(hal_board)
            if Board().check_if_empty(pit_board, num):
                pit_board[num] = "O"
                if Board().check_for_win(pit_board, "O"):
                    return num

        # if Dave can win on next move, block him
        for num in range(0, 8):
            pit_board = self.copy_board(hal_board)
            if Board().check_if_empty(pit_board, num):
                pit_board[num] = "X"
                if Board().check_for_win(pit_board, "X"):
                    return num

        # if the middle is open, HAL takes it
        if Board().check_if_empty(hal_board, 4):
            return 4

        # if one of the corners are open, HAL takes it
        for num in [0, 2, 6, 8]:
            if Board().check_if_empty(hal_board, num):
                return num

        # if all else fails, HAL will choose a random free space
        for num in [1, 3, 5, 7]:
            if Board().check_if_empty(hal_board, num):
                return num


class PlayGame:
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.user_input = 0
        self.hal_input = 0

    def run_program(self):
        """Loop to continue the game until HAL wins or there is a draw. The user cannot win."""

        # prints the initial welcome message
        print(Board().print_welcome())

        while True:

            # prints the board at its current state
            print(Board().return_board(self.board))

            # prompts the user and checks to make sure their input is valid
            while True:
                temp_user_input = Player().prompt_user_return_input()
                if Player().verify_is_a_number(temp_user_input):
                    self.user_input = int(temp_user_input)

                    if Board().check_if_empty(self.board, self.user_input):
                        break
                else:
                    print("Why do you refuse to enter an open number, Dave?")
                    continue

            # write the users validated input
            self.board = Player().write_user_choice(self.board, self.user_input)

            # prints the board after the user has written to it
            print(Board().return_board(self.board))

            # writes HAL's move to board
            self.hal_input = Hal().hal_9000(self.board)
            Hal().write_hal_choice(self.board, self.hal_input)

            # checks to see if HAL won yet, or if there is a draw
            if Board().did_hal_win_yet(self.board):
                print(Board().return_board(self.board))
                break


# runs the game
if __name__ == "__main__":
    new_game = PlayGame()
    new_game.run_program()
