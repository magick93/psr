from enum import Enum
import time
import colorama
from colorama import Fore, Style
import random
from pydantic import BaseModel, validator, root_validator, create_model

import typer

app = typer.Typer()

class Move(str, Enum):
    PAPER = 'P'
    SCISSORS = 'S'
    ROCK = 'R'
    

GameRuleEngine = create_model(
    'GameRuleEngine',
    human_player=(Move, ...),
    computer_player=(Move, ...),
    validate_moves=True
)

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
        elif (self.human_player, self.computer_player) in [(Move.PAPER, Move.ROCK), (Move.SCISSORS, Move.PAPER), (Move.ROCK, Move.SCISSORS)]:
            return "You win!"
        else:
            return "Computer wins!"


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



def begin_game():

    # Get user input for the game
    user_choice = input("Choose your move: (P)aper, (S)cissors, or (R)ock? ").lower()

    match user_choice:
        case 'p':
            print("You chose Paper.")
            play_game(Move.PAPER)
        case 's':
            print("You chose Scissors.")
            play_game(Move.SCISSORS)
        case 'r':
            print("You chose Rock.")
            play_game(Move.ROCK)

        case 'e':
            easter_egg()
        case _:
            print("Invalid choice. Try again.")
            begin_game()

    







def easter_egg():
    # Initialize colorama
    colorama.init()

    # Read the contents of the ANSI-encoded text file
    with open('./models/DNNRL_auto_encoder.txt', 'r',  encoding='cp1252') as f:
        contents = f.read()
    # Display the contents of the file in the terminal
    # print(Fore.RED + contents + Style.RESET_ALL)
    typer.echo(contents, color=True)



@app.command()
def rules():
    rule_1 = "🪨  Rock wins against scissors."
    rule_2 = "✂️  Scissors win against paper."
    rule_3 = "📃  Paper wins against rock."

    text = f"""Although the game has a lot of complexity to it, the rules to play it are pretty simple.
    The game is played where players deliver hand signals that will represent the elements of the game; rock, paper and scissors. The outcome of the game is determined by 3 simple rules:

        {rule_1}

        {rule_2}

        {rule_3}
    """
    typer.echo(text)




@app.command()
def play(with_timer: bool = typer.Argument(True, help="A flag to indicate whether to use a timer or not")):
    print("Welcome to Paper, Scissors, Rock!\n")
    if with_timer:
        for i in range(3, 0, -1):
            print(f"Starting game in {i}...")
            time.sleep(1)

        print("GO!\n")
        begin_game()
    else:
        begin_game()


if __name__ == "__main__":
    app()


