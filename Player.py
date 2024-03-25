from Checker import Checker
class Player:
    def __init__(self):
        self.player_lines = []
        self.turn = False
    # selects the line and stores it in a list as [('a1', 'b1'), ...] (Hossein)
    def player_input(self, checker: Checker):
        player_line = ()
        points_counter = 0
        while True:
            if points_counter == 0:
                first_point = input("Select the first point: ")
                first_point = checker.point_checker(first_point)            
                if first_point == None:
                    continue
                else:
                    player_line[0] = first_point
                    points_counter += 1
            elif points_counter == 1:
                second_point = input("Select the second point: ")
                second_point = checker.point_checker(second_point)            
                if second_point == None:
                    continue
                else:
                    player_line[1] = second_point
                    points_counter += 1
            else:
                break
        
        if checker.choose_line_checker(player_line) and player_line not in self.player_lines:
            self.player_lines.append(player_line)



    def cal_point(self):
        pass

 
    def change_turn(self):
        pass

    def player_turn(self):
        pass