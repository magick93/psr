import io
import unittest
from unittest.mock import patch
from psr import begin_game


class TestBeginGame(unittest.TestCase):
    @patch('builtins.input', return_value='p')
    def test_paper(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            begin_game()
            self.assertIn("Your move: PAPER", fake_output.getvalue())

    @patch('builtins.input', return_value='s')
    def test_scissors(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            begin_game()
            self.assertIn("Your move: SCISSORS", fake_output.getvalue())

    @patch('builtins.input', return_value='r')
    def test_rock(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            begin_game()
            self.assertIn("Your move: ROCK", fake_output.getvalue())



    @patch('sys.stdin', io.StringIO('i\n'))
    @patch('builtins.input', return_value='e')
    def test_invalid(self, mock_stdout):
        begin_game()
        print(mock_stdout.getvalue())
        # self.assertEqual(mock_stdout.getvalue(), "Welcome to Paper, Scissors, Rock!\n\nStarting game in 3...\nStarting game in 2...\nStarting game in 1...\nGO!\n\nChoose your move: (P)aper, (S)cissors, or (R)ock? Invalid choice. Try again.\n\nStarting game in 3...\nStarting game in 2...\nStarting game in 1...\nGO!\n\nChoose your move: (P)aper, (S)cissors, or (R)ock? ")
        # sys.stdin = sys.__stdin__ # Restore default stdin to stop the CLI

if __name__ == '__main__':
    unittest.main()
