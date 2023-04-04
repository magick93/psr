from enum import Enum


class Move(str, Enum):
    PAPER = 'P'
    SCISSORS = 'S'
    ROCK = 'R'