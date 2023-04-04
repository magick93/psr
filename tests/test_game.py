import unittest
from pydantic import ValidationError

from controller.GameRuleEngine import GameRuleEngine
from models.Move import Move
from models.Result import Result
# from psr import GameRuleEngine, Move

class TestGameRuleEngine(unittest.TestCase):

    def test_valid_moves(self):
        # Test that the GameRuleEngine validates valid moves
        game = GameRuleEngine(human_player=Move.PAPER, computer_player=Move.SCISSORS)
        self.assertEqual(game.human_player, Move.PAPER)
        self.assertEqual(game.computer_player, Move.SCISSORS)

    def test_invalid_moves(self):
        # Test that the GameRuleEngine raises a ValueError for invalid moves
        with self.assertRaises(ValidationError):
            GameRuleEngine(human_player='invalid', computer_player=Move.SCISSORS)

    def test_same_moves(self):
        # Test that the GameRuleEngine raises a ValueError for the same moves
        with self.assertRaises(ValueError):
            GameRuleEngine(human_player=Move.PAPER, computer_player=Move.PAPER)
        

    def test_human_player_wins(self):
        # Test that the GameRuleEngine correctly identifies a human player win
        game = GameRuleEngine(human_player=Move.PAPER, computer_player=Move.ROCK)
        self.assertEqual(game.determine_winner(), Result.WIN)

    def test_computer_player_wins(self):
        # Test that the GameRuleEngine correctly identifies a computer player win
        game = GameRuleEngine(human_player=Move.SCISSORS, computer_player=Move.ROCK)
        self.assertEqual(game.determine_winner(), Result.LOSE)





if __name__ == '__main__':
    unittest.main()
