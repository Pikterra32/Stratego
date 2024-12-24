from enums import Type, Dir, Side

class Piece:
    type: Type
    pos: list[int]

    def __init__(self, type: Type, posX: int, posY: int, side: Side, id: int):
        self.type = type

        self.pos = [posX, posY]

        self.side = side
        self.id = id


    def __repr__(self):
        return f"{str(self.side)[5::]} {str(self.type)[5::]} at x:{self.pos[0]} - y:{self.pos[1]} id:{self.id}"


    def move(self, direction: Dir):
        self.pos[0] += direction.value[0]
        self.pos[1] += direction.value[1]

    def moveTo(self, posX: int, posY: int):
        self.pos[0] = posX
        self.pos[1] = posY
