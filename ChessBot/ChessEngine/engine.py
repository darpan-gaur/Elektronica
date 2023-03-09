from stockfish import Stockfish
class board:
    def __init__(self):
        self.Board = Stockfish()

    def move_piece(self, move):
        """
        Moves chess piece(s)

        Args:
            move: string
            Eg. move = "e2e4"
            => Move piece at e2 to e4
        """
        self.Board.make_moves_from_current_position([move])

    def get_best(display = True):
        best_move = self.Board.get_best_move()
        self.Board.make_moves_from_current_position([best_move])
        if (display):
            print(self.Board.get_board_visual())
        return best_move