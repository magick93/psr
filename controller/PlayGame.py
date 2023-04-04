

import random
from controller.GameRuleEngine import GameRuleEngine
from models.Move import Move


class Play:

    def play_game(player_move: Move) -> str:
        """
        Play a game of Paper, Scissors, Rock against the computer.

        Args:
            player_move (Move): The move chosen by the human player.

        Returns:
            str: A string indicating the winner of the game.
        """
        
        # Generate a random move for the computer
        computer_move = random.choice(list(Move))

        # Print the moves chosen by the player and computer
        print(f"Your move: {player_move.name}")
        print(f"HAL 9000's move: {computer_move.name}")

        # Determine the winner of the game using the GameRuleEngine
        try:
            game = GameRuleEngine(human_player=player_move, computer_player=computer_move)
            winner = game.determine_winner()
        except ValueError as e:
            print(f"Error: {e}")
            winner = None

        # Print the winner of the game and return it as a string
        if winner:
            print(winner)
        return winner