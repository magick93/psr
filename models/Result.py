from enum import Enum


class Result(str, Enum):
    WIN = 'Win'
    LOSE = 'Lose'
    TIE = 'Draw'
    INVALID = 'Invalid'