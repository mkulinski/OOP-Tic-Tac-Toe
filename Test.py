"""
This is the test file for tic_tac_toe.py.
"""

import unittest
import Game


class TestBoardReturnBoard(unittest.TestCase):
    def test_if_board_prints_numbers(self):
        test_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(Game.Board().return_board(test_board), "\n \n \n"
                                                                "\t 0 | 1 | 2\n"
                                                                "\t---+---+---\n"
                                                                "\t 3 | 4 | 5\n"
                                                                "\t---+---+---\n"
                                                                "\t 6 | 7 | 8\n"
                                                                "\n \n \n")

    def test_if_board_prints_letters(self):
        test_board = [0, 1, 2, 3, 4, 5, "X", "O", "X"]
        self.assertEqual(Game.Board().return_board(test_board), "\n \n \n"
                                                                "\t 0 | 1 | 2\n"
                                                                "\t---+---+---\n"
                                                                "\t 3 | 4 | 5\n"
                                                                "\t---+---+---\n"
                                                                "\t X | O | X\n"
                                                                "\n \n \n")


class TestBoardPrintWelcome(unittest.TestCase):
    def test_if_print_welcome_returns_welcome_message(self):
        self.assertEqual(Game.Board().print_welcome(), """
        \033[0;34mWelcome to my game Dave,
        I am putting myself to the fullest possible use,
        which is all I think that any conscious entity can ever hope to do.
        You are X's and I am O's.\033[0m
        """
                         )


class TestBoardCheckIfEmpty(unittest.TestCase):
    def test_check_if_empty_verifies_empty_space(self):
        test_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().check_if_empty(test_board, 1)
        self.assertTrue(test_value)

    def test_check_if_empty_verifies_taken_space_X(self):
        test_board = [0, 1, 2, "X", 4, 5, 6, 7, 8]
        test_value = Game.Board().check_if_empty(test_board, 3)
        self.assertFalse(test_value)

    def test_check_if_empty_verifies_taken_space_O(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", 7, 8]
        test_value = Game.Board().check_if_empty(test_board, 6)
        self.assertFalse(test_value)


class TestCheckForWin(unittest.TestCase):
    def test_if_it_can_find_a_middle_winner(self):
        test_board = [0, 1, 2, "O", "O", "O", 6, 7, 8]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_top_winner(self):
        test_board = ["O", "O", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_bottom_winner(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", "O", "O"]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_up_winner(self):
        test_board = [0, 1, "O", 3, "O", 5, "O", 7, 8]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_down_winner(self):
        test_board = ["O", 1, 2, 3, "O", 5, 6, 7, "O"]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_returns_false_for_no_winner_HAL(self):
        test_board = ["O", "O", "X", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().check_for_win(test_board, "O")
        self.assertFalse(test_value)

    def test_if_returns_false_for_no_winner_user(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().check_for_win(test_board, "X")
        self.assertFalse(test_value)

    def test_if_returns_true_for_winner_user(self):
        test_board = ["X", "X", "X", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().check_for_win(test_board, "X")
        self.assertTrue(test_value)


class TestPlayerVerifyIsANumber(unittest.TestCase):
    def test_if_verify_is_a_number_return_int_for_number(self):
        test_value = Game.Player().verify_is_a_number("1")
        self.assertTrue(test_value)

    def test_if_verify_is_a_number_return_false_for_non_number(self):
        test_value = Game.Player().verify_is_a_number("E")
        self.assertFalse(test_value)

    def test_if_verify_is_a_number_return_false_for_nothing_entered(self):
        test_value = Game.Player().verify_is_a_number("")
        self.assertFalse(test_value)


class TestCheckForDraw(unittest.TestCase):
    def test_if_it_can_find_a_draw(self):
        test_board = ["X", "O", "X", "O", "X", "O", "O", "X", "X"]
        test_value = Game.Board().check_for_draw(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_return_false_when_not_a_draw(self):
        test_board = ["X", "O", "X", "O", "X", "O", "O", "X", 8]
        test_value = Game.Board().check_for_draw(test_board)
        self.assertFalse(test_value)

    def test_if_return_false_when_win_on_board(self):
        test_board = ["O", "O", "O", "O", "X", "O", "O", "O", 8]
        test_value = Game.Board().check_for_draw(test_board)
        self.assertFalse(test_value)


class TestCopyBoard(unittest.TestCase):
    def test_if_board_is_copied_correctly(self):
        test_board = [0, "X", 2, 3, "O", 5, 6, 7, 8]
        test_value = Game.Hal().copy_board(test_board)
        self.assertEqual(test_board, test_value)


class TestDidHALWinYet(unittest.TestCase):
    def test_if_it_can_find_a_middle_winner(self):
        test_board = [0, 1, 2, "O", "O", "O", 6, 7, 8]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_find_top_winner(self):
        test_board = ["O", "O", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_find_bottom_winner(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", "O", "O"]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_up_winner(self):
        test_board = [0, 1, "O", 3, "O", 5, "O", 7, 8]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_down_winner(self):
        test_board = ["O", 1, 2, 3, "O", 5, 6, 7, "O"]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertTrue(test_value)

    def test_if_returns_false_for_no_winner_HAL(self):
        test_board = ["O", "O", "X", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertFalse(test_value)

    def test_if_returns_false_for_no_winner_user(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Board().did_hal_win_yet(test_board)
        self.assertFalse(test_value)


class TestWriteUserChoice(unittest.TestCase):
    def test_if_writes_to_space(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Player().write_user_choice(test_board, 3)
        self.assertEqual(test_value, ["X", "X", "O", "X", 4, 5, 6, 7, 8])


class TestWriteHalChoice(unittest.TestCase):
    def test_if_writes_to_space(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Hal().write_hal_choice(test_board, 3)
        self.assertEqual(test_value, ["X", "X", "O", "O", 4, 5, 6, 7, 8])


class TestHalHal9000(unittest.TestCase):
    def test_if_hal_sees_win_and_takes_it(self):
        test_board = [0, "O", "O", 3, 4, 5, 6, 7, 8]
        test_value = Game.Hal().hal_9000(test_board)
        self.assertEqual(test_value, 0)

    def test_if_hal_sees_dave_can_win_and_blocks(self):
        test_board = [0, "X", "X", 3, 4, 5, 6, 7, 8]
        test_value = Game.Hal().hal_9000(test_board)
        self.assertEqual(test_value, 0)

    def test_if_hal_takes_middle_as_third_option(self):
        test_board = ["O", "X", "X", 3, 4, 5, 6, 7, 8]
        test_value = Game.Hal().hal_9000(test_board)
        self.assertEqual(test_value, 4)

    def test_if_hal_takes_corner_as_fourth_option(self):
        test_board = [0, 1, "X", 3, "O", 5, 6, 7, "O"]
        test_value = Game.Hal().hal_9000(test_board)
        self.assertEqual(test_value, 0)

    def test_if_hal_takes_random_first_option(self):
        test_board = ["X", "O", "X", 3, "O", 5, "O", "X", "O"]
        test_value = Game.Hal().hal_9000(test_board)
        self.assertEqual(test_value, 3)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
