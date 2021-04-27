import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def generate_cells(widht_screen, height_screen, widht_cell, height_cell):
    columns = list()

    for pos_x in range(0, widht_screen // widht_cell):

        rows = list()
        for pos_y in range(0, height_screen // height_cell):
            rows.append(Cell(widht_cell, height_cell, pos_x, pos_y))
        
        columns.append(rows)

    return columns

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, widht, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.widht = widht
        self.height = height

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.check = False
        self.ant = None

        self.update_rect()

    def update_rect(self):
        self.rect = self.get_rect()

        self.rect.x = self.pos_x * self.widht
        self.rect.y = self.pos_y * self.height

    def get_rect(self):
        self.image = pygame.Surface( (self.widht - 1, self.height - 1) )

        if self.ant:
            self.image.fill(self.ant.color)
        else:
            if self.check:
                self.image.fill(WHITE)
            else:
                self.image.fill(BLACK)

        return self.image.get_rect()

    def set_ant(self, ant):
        self.ant = ant
        self.get_rect()

    def unset_ant(self):
        self.ant = None
        self.get_rect()

    def select(self):
        self.check = not self.check
        self.update_rect()
