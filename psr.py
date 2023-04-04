import time


import typer
from controller.Choices import ChoiceAction


app = typer.Typer()


    

# GameRuleEngine = create_model(
#     'GameRuleEngine',
#     human_player=(Move, ...),
#     computer_player=(Move, ...),
#     validate_moves=True
# )




# def play_game(player_move: Move) -> str:
#     """
#     Play a game of Paper, Scissors, Rock against the computer.

#     Args:
#         player_move (Move): The move chosen by the human player.

#     Returns:
#         str: A string indicating the winner of the game.
#     """
    
#     # Generate a random move for the computer
#     computer_move = random.choice(list(Move))

#     # Print the moves chosen by the player and computer
#     print(f"Your move: {player_move.name}")
#     print(f"HAL 9000's move: {computer_move.name}")

#     # Determine the winner of the game using the GameRuleEngine
#     try:
#         game = GameRuleEngine(human_player=player_move, computer_player=computer_move)
#         winner = game.determine_winner()
#     except ValueError as e:
#         print(f"Error: {e}")
#         winner = None

#     # Print the winner of the game and return it as a string
#     if winner:
#         print(winner)
#     return winner



def begin_game(iterations: int = 1):
    """
    Starts the game and prompts the user to choose their move.

    Args:
        iterations (int): Number of iterations to play the game. Default is 1.

    Returns:
        None
    """

    for i in range(iterations):
        ChoiceAction.choose()
   
    








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
def play(
    games: int = typer.Option("", help="The number of games to play."),

    with_timer: bool = typer.Argument(True, help="A flag to indicate whether to use a timer or not")):
    print("Welcome to Paper, Scissors, Rock!\n")

    if games <= 0:
        print("Invalid number of games. Try again with a number greater than 0.")
        return
    
    if with_timer:
        for i in range(3, 0, -1):
            print(f"Starting game in {i}...")
            time.sleep(1)

        print("GO!\n")
        begin_game(games)
    else:
        begin_game(games)


if __name__ == "__main__":
    app()


