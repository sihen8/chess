import pygame

class Button:
    def __init__(self, img, x, y, purpose):
        self.img_file = pygame.image.load(img)
        self.x = x
        self.y = y
        self.img_size = self.img_file.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.img_size[0], self.img_size[1])
        self.purpose = purpose

    def get_purpose(self):
        return self.purpose

    def get_coord(self):
        return self.x, self.y

