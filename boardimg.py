import pygame
import aspose.words as aw

class Boardimg:

    def __init__(self, img):
        self.img = img
        self.img_file = pygame.image.load(img)
        self.x = 0
        self.y = 0
        self.img_size = self.img_file.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.img_size[0], self.img_size[1])

    def set_img(self, img):
        self.img = img
        self.img_file = pygame.image.load(img)
        self.img_size = self.img_file.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.img_size[0], self.img_size[1])

    def get_img(self):
        return self.img

    def covert_to_png(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_image(self.img)
        pageSetup = builder.page_setup
        pageSetup.page_width = shape.width
        pageSetup.page_height = shape.height
        pageSetup.top_margin = 0
        pageSetup.left_margin = 0
        pageSetup.bottom_margin = 0
        pageSetup.right_margin = 0
        doc.save("image.png")
        self.set_img("image.png")




a = Boardimg("image.svg")
a.covert_to_png()


