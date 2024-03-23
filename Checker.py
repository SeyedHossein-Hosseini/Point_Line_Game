class Checker:
    def __init__(self) -> None:
        pass

    # it has player_lines (Hossein) 
    def square_complete(self, player_lines):
        # returns [('a1', 'a2', 'b1', 'b2'), ...] or None
        pass

    # @ checks the lines vertically and horizontally, plus whether the line is empty (Hossein)
    def choose_line_checker(self, board):
        # returns the selected correct line to player class
        pass

    # checks the correctness of selected points using points of board class ['a1', 'a2', 'a3', ..., ] (Hossein)
    def point_checker(self, points):
        pass

    def choose_first(self):
        pass

    def full_board_check(self, board):
        pass

    def win_check(self, player1, player2):
        pass


    def replay(self):
        pass
