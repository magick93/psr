
import typer
from controller.PlayGame import Play
from models.Move import Move
import colorama



class ChoiceAction:

    def choose():
        user_choice = input("Choose your move: (P)aper, (S)cissors, or (R)ock? ").lower()

        match user_choice:
            case 'p':
                Play.play_game(Move.PAPER)
            case 's':
                Play.play_game(Move.SCISSORS)
            case 'r':
                Play.play_game(Move.ROCK)

            case 'e':
                easter_egg()
            case _:
                print("Invalid choice. Try again.")
                # begin_game()


def easter_egg():
    # Initialize colorama
    colorama.init()

    # Read the contents of the ANSI-encoded text file
    with open('./models/DNNRL_auto_encoder.txt', 'r',  encoding='cp1252') as f:
        contents = f.read()
    # Display the contents of the file in the terminal
    # print(Fore.RED + contents + Style.RESET_ALL)
    typer.echo(contents, color=True)