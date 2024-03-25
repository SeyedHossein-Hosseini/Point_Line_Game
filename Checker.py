class Checker:
    def __init__(self, board):
        # pass the board object to Checker class
        self.points = board._points # ['a1', 'a2', ..., 'c1', 'c2', ..., 'e1', 'e2', ...] # 
        self.alphabet_list = list(board.alphabet_str) # ['a', 'b', 'c', 'd', ... , 'z'] #


    @staticmethod
    def are_consecutive(list_, ele1, ele2):
        ele1_index = list_.index(ele1)
        ele2_index = list_.index(ele2)

        if ele1_index + 1 < len(list_):
            if list_[ele1_index + 1] == ele2 or list_[ele2_index + 1] == ele1:
                return True
        return False

    # it has player_lines (Hossein) 
    def square_complete(self, player_lines, current_line):
        # returns [('a1', 'a2', 'b1', 'b2'), ...] or None
        pass

    # @ checks the lines vertically and horizontally, plus whether the line is empty (Hossein)
    def choose_line_checker(self, selected_line):
        # example of selected_line: ('a1', 'b1')

        first_char_of_first_ele = list(selected_line[0])[0] # for ('a1', 'b2') it is a #
        second_char_of_first_ele = list(selected_line[0])[1] # for ('a1', 'b2') it is 1 #
        first_char_of_second_ele = list(selected_line[1])[0] # for ('a1', 'b2') it is b #
        second_char_of_second_ele = list(selected_line[1])[1] # for ('a1', 'b2') it is 2 #

        if first_char_of_first_ele == first_char_of_second_ele and second_char_of_first_ele == second_char_of_second_ele:
            print("2 points are the same")
        
        elif first_char_of_first_ele == first_char_of_second_ele and (int(second_char_of_first_ele) + 1 == int(second_char_of_second_ele) or int(second_char_of_first_ele) == int(second_char_of_second_ele) + 1):
            return True

        elif int(second_char_of_first_ele) == int(second_char_of_second_ele) and self.are_consecutive(self.alphabet_list, first_char_of_first_ele, first_char_of_second_ele):
            return True
        # returns the selected correct line to player class
        else:
            print("Try again")


    # checks the correctness of selected points using points of board class ['a1', 'a2', 'a3', ..., ] (Hossein)
    def point_checker(self, selected_point: str):
        if selected_point in self.points:
            return selected_point
        else:
            return None
        
    def choose_first(self):
        pass

    def full_board_check(self, board):
        pass

    def win_check(self, player1, player2):
        pass



    def replay(self):
        pass
