from board import Board
from enums import Type, Side


# sets needs to be rotated because blue is at the opposite side of the gameboard
def boardRotateX(board: Board, input: int) -> int:
    return board.width-1-input
def boardRotateY(board: Board, input: int) -> int:
    return abs(input-3)


def setup(blueChoice: list, redChoice: list) -> Board:
    board = Board()

    index: int = 0

    for y in range(4):
        for x in range(board.width):
            value = blueChoice[index]
            match value:
                case 1:
                    board.addPiece(Type.Spy, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 2:
                    board.addPiece(Type.Scout, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 3:
                    board.addPiece(Type.Miner, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 4:
                    board.addPiece(Type.Sergeant, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 5:
                    board.addPiece(Type.Lieutenant, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 6:
                    board.addPiece(Type.Captain, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 7:
                    board.addPiece(Type.Major, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 8:
                    board.addPiece(Type.Colonel, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 9:
                    board.addPiece(Type.General, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 10:
                    board.addPiece(Type.Marshal, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 'B':
                    board.addPiece(Type.Bomb, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
                case 'F':
                    board.addPiece(Type.Flag, boardRotateX(board, x), boardRotateY(board, y), Side.Blue)
            index += 1

    index = 0
    for y in range(5, 9):
        for x in range(board.width):
            value = redChoice[index]
            match value:
                case 1:
                    board.addPiece(Type.Spy, x, y+1, Side.Red)
                case 2:
                    board.addPiece(Type.Scout, x, y+1, Side.Red)
                case 3:
                    board.addPiece(Type.Miner, x, y+1, Side.Red)
                case 4:
                    board.addPiece(Type.Sergeant, x, y+1, Side.Red)
                case 5:
                    board.addPiece(Type.Lieutenant, x, y+1, Side.Red)
                case 6:
                    board.addPiece(Type.Captain, x, y+1, Side.Red)
                case 7:
                    board.addPiece(Type.Major, x, y+1, Side.Red)
                case 8:
                    board.addPiece(Type.Colonel, x, y+1, Side.Red)
                case 9:
                    board.addPiece(Type.General, x, y+1, Side.Red)
                case 10:
                    board.addPiece(Type.Marshal, x, y+1, Side.Red)
                case 'B':
                    board.addPiece(Type.Bomb, x, y+1, Side.Red)
                case 'F':
                    board.addPiece(Type.Flag, x, y+1, Side.Red)
            index += 1

    return board
