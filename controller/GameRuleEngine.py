from pydantic import BaseModel, root_validator, validator
from models.Move import Move
import sqlite3 as sl


class GameRuleEngine(BaseModel):
    human_player: Move
    computer_player: Move
    validate_moves: bool = True

    @root_validator(pre=True)
    def validate_not_same_move(cls, values):
        if values['human_player'] == values['computer_player']:
            raise ValueError("It's a tie!")
        return values

    @validator('human_player', 'computer_player', pre=True)
    def validate_moves(cls, value):
        if value not in Move:
            raise ValueError(f"Invalid move: {value}")
        return value


    def determine_winner(self):
        if self.human_player == self.computer_player:
            return "It's a tie!"

        rules = {
            Move.PAPER: {Move.ROCK: "You win!", Move.SCISSORS: "Computer wins!"},
            Move.SCISSORS: {Move.PAPER: "You win!", Move.ROCK: "Computer wins!"},
            Move.ROCK: {Move.SCISSORS: "You win!", Move.PAPER: "Computer wins!"},
        }

        # Extensbility
        # rules = {
        #     Move.PAPER: {Move.ROCK: "You win!", Move.SCISSORS: "Computer wins!", Move.LIZARD: "You win!"},
        #     Move.SCISSORS: {Move.PAPER: "You win!", Move.ROCK: "Computer wins!", Move.SPOCK: "Computer wins!"},
        #     Move.ROCK: {Move.SCISSORS: "You win!", Move.PAPER: "Computer wins!", Move.SPOCK: "You win!"},
        #     Move.LIZARD: {Move.PAPER: "Computer wins!", Move.SPOCK: "You win!"},
        #     Move.SPOCK: {Move.SCISSORS: "You win!", Move.ROCK: "You win!"},
        # }


        if rules[self.human_player].get(self.computer_player):
            return rules[self.human_player][self.computer_player]
        else:
            return "Invalid moves"