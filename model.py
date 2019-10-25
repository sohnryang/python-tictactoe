DRAW = 'draw'
UNDEFINED = 'undef'

class Board:
    def __init__(self):
        self.clear()

    def place(self, player, x, y):
        if self.board_data[x][y] is not None:
            raise ValueError('Cannot place on position (%d, %d)' % (x, y))
        self.board_data[x][y] = player

    def clear(self):
        self.board_data = []
        for _ in range(3):
            self.board_data.append([None] * 3)

    def check_winner(self):
        check_pos = (((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                     ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                     ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                     ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)))

        for pos_list in check_pos:
            s = set()
            for pos in pos_list:
                stone = self.board_data[pos[0]][pos[1]]
                if stone is None:
                    return UNDEFINED
                s.add(stone)
            if len(s) == 1:
                return s.pop()

        return DRAW
