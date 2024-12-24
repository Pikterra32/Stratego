from enum import Enum

# classing pieces by their original ranks
class Type(Enum):
    Flag = 'F'
    Spy = 0
    Scout = 1
    Miner = 2
    Sergeant = 3
    Lieutenant = 4
    Captain = 5
    Major = 6
    Colonel = 7
    General = 8
    Marshal = 9
    Bomb = 'B'

class Dir(Enum):
    Up = (0,-1)
    Down = (0,1)
    Left = (-1,0)
    Right = (1,0)

class Side(Enum):
    Red = 0
    Blue = 1

class Content(Enum):
    Free = 0
    Piece = 1
    Lake = 2
    Boundaries = 3
