from piece import Piece
from enums import Dir, Type, Side, Content

default_lakes: list[tuple[int, int]] = [
    (2, 4), (3, 4),
    (2, 5), (3, 5),

    (6, 4), (7, 4),
    (6, 5), (7, 5),
]

class Moves():
    id: int
    moves: list[Dir]

    def __init__(self):
        self.id = 0
        self.moves = []

    def __repr__(self):
        return f"\n{self.id} {self.moves}"

class Board():
    availableMoves: list[Moves]
    composition: list[Piece] = []
    id: int = 0

    def __init__(self, width: int = 10, height: int = 10, lakes: list[tuple[int, int]] = default_lakes):
        self.width = width
        self.height = height
        self.lakes = lakes
        self.availableMoves = []


    def __repr__(self):
        format: str = ""

        for y in range(self.height):
            format += '\n'

            for x in range(self.width):
                terrain: str = "\033[32m"+ "." +"\033[0m"

                for piece in self.composition:
                    if piece.pos[0] == x and piece.pos[1] == y:
                        if piece.side == Side.Red:
                            terrain = "\033[31m"+ str(piece.type.value) +"\033[0m"
                        else:
                            terrain = "\033[34m"+ str(piece.type.value) +"\033[0m"

                for lake in self.lakes:
                    if lake[0] == x and lake[1] == y:
                        terrain = "\033[35m"+ "*" +"\033[0m"

                format += terrain
        return format


    def addPiece(self, type: Type, posX: int, posY: int, side: Side):
        availability = self.content(posX, posY)
        if availability == Content.Free:
            newPiece = Piece(type, posX, posY, side, self.id)
            self.composition.append(newPiece)
            self.id += 1

    def movePiece(self, id: int, direction: Dir):
        target = self.getPieceById(id)
        if target.type == Type.Bomb:
            return 0

        targetPos: tuple[int, int] = (target.pos[0]+direction.value[0], target.pos[1]+direction.value[1])

        content = self.content(targetPos[0], targetPos[1])

        if content == Content.Free:
            target.move(direction)
        elif content == Content.Piece:
            ennemy = self.getPieceByPos(targetPos[0], targetPos[1])
            if ennemy.side != target.side:
                result = self.strike(target, ennemy)
                if result == 0:
                    target.move(direction)
                elif result == 1:
                    if ennemy.type != Type.Bomb:
                        ennemy.moveTo(targetPos[0]-direction.value[0], targetPos[1]-direction.value[1])
                elif result == -1:
                    pass

        self.refreshAvailableMoves()

    def content(self, posX: int, posY: int) -> Content :
        for lake in self.lakes:
            if lake[0] == posX and lake[1] == posY:
                return Content.Lake

        for piece in self.composition:
            if piece.pos[0] == posX and piece.pos[1] == posY:
                return Content.Piece

        if ( posX >= 0 and posX <= self.width-1 ) and ( posY >= 0 and posY <= self.height-1 ):
            return Content.Free
        else:
            return Content.Boundaries


    def getPieceById(self, id: int) -> Piece:
        if id >= self.id:
            print("invalid id")
            quit(-1)
        for piece in self.composition:
            if piece.id == id:
                return piece
        return self.composition[0]


    def getPieceByPos(self, posX: int, posY: int):
        for piece in self.composition:
            if piece.pos[0] == posX and piece.pos[1] == posY:
                return piece
        return self.composition[0]


    def strike(self, offense: Piece, defense: Piece) -> int:
        if defense.type == Type.Flag:
            self.win(offense.side)
            return -1

        if defense.type == Type.Bomb:
            if offense.type == Type.Miner:
                self.killPiece(defense)
                return 0
            else:
                self.killPiece(offense)
                return 1

        if offense.type == Type.Spy:
            if defense.type == Type.Marshal:
                self.killPiece(defense)
                return 0
            elif int(offense.type.value) == int(defense.type.value):
                self.killPiece(offense)
                self.killPiece(defense)
                return -1
            else:
                self.killPiece(offense)
                return 1

        if int(offense.type.value) > int(defense.type.value):
            self.killPiece(defense)
            return 0
        elif int(offense.type.value) < int(defense.type.value):
            self.killPiece(offense)
            return 1
        elif int(offense.type.value) == int(defense.type.value):
            self.killPiece(offense)
            self.killPiece(defense)
            return -1
        return -1


    def win(self, side: Side):
        print(f"{side} won")
        self.composition = []


    def killPiece(self, target: Piece):
        self.composition.remove(target)

    def refreshAvailableMoves(self):
        for piece in self.composition:
            moves = Moves()
            moves.id = piece.id

            for direction in Dir:
                targetPos: tuple[int, int] = (piece.pos[0]+direction.value[0], piece.pos[1]+direction.value[1])
                content = self.content(targetPos[0], targetPos[1])

                if content == Content.Free:
                    moves.moves.append(direction)
                elif content == Content.Piece and self.getPieceByPos(targetPos[0], targetPos[1]).side != piece.side:
                    moves.moves.append(direction)

            if len(moves.moves) >= 1:
                self.availableMoves.append(moves)
