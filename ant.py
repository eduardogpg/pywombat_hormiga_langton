class Ant():

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.color = (170, 56, 150)
        
        self.last_cell = None

        self.position = 12 # 12 == N // 6 == S // 3 == E // 9 == O

    def check(self, cells):
        if self.last_cell:
            self.last_cell.unset_ant()
        
        self.current_cell = cells[self.pos_x][self.pos_y]
        self.current_cell.set_ant(self)

        if self.current_cell.check:
            self.position -= 3
            if self.position <= 0:
                self.position = 12
        else:
            self.position += 3
            if self.position > 12:
                self.position = 3

        self.current_cell.select()

        if self.position == 12:
            self.pos_y -= 1
        elif self.position == 3:
            self.pos_x += 1
        elif self.position == 6:
            self.pos_y += 1
        elif self.position == 9:
            self.pos_x -= 1

        self.last_cell = self.current_cell
