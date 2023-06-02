import pygame
import chess
import chess.svg
from boardimg import Boardimg
from button import Button

def get_board_img(brd):
    svg = chess.svg.board(board=brd, size=600)
    f = open("image.svg", "w")
    f.write(svg)
    f.close()

# set up pygame modules

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Chess")

# for input box
base_font = pygame.font.Font(None, 20)
user_text = ''
input_rect = pygame.Rect(0, 600, 100, 100)
color = pygame.Color('chartreuse4')


# set up variables for the display
SCREEN_HEIGHT = 620
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# text display

display_name = my_font.render("Click to start!", True, (0, 0, 0))

my_font = pygame.font.SysFont('Arial', 50)


run = True 
start_screen = True
game_screen = False
active = False
two_player = False
bot_player = False


board = chess.BaseBoard()
get_board_img(board)

boardimg = Boardimg("image.svg")
boardimg.covert_to_png()
boardimg.set_img("image.png")
bot_bn = Button("bot_button.png", 150, 250, "bot")
player_bn = Button("player_button.png", 350, 250, "bot")

# Chess display

while run:

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if bot_bn.rect.collidepoint(event.pos):
                print("bot")
                bot_player = True
                start_screen = False
                game_screen = True

            if player_bn.rect.collidepoint(event.pos):
                print("2player")
                board = chess.Board()
                two_player = True
                start_screen = False
                game_screen = True

        if event.type == pygame.KEYDOWN:
            # 8 = backspace
            if event.key == 8:
                user_text = user_text[0:len(user_text) - 1]

            elif event.key == 13:
                # 13 = enter
                if two_player is True:
                    try:
                        move = chess.Move.from_uci(user_text)
                        board.push(move)
                        get_board_img(board)
                        boardimg.set_img("image.svg")
                        boardimg.covert_to_png()

                    except chess.InvalidMoveError:
                        pass

                # if bot_player is True:
                    #TODO

                    user_text = ""

            # Unicode standard is used for string
            # formation
                else:
                    try:
                        print(chr(event.key))
                        print(event.key)
                        user_text += chr(event.key)
                    except:
                        pass

    screen.fill("white")
    if start_screen:
        screen.blit(display_name, (0,0))
        screen.blit(bot_bn.img_file, bot_bn.rect)
        screen.blit(player_bn.img_file, player_bn.rect)

    if game_screen:
        screen.blit(boardimg.img_file, boardimg.rect)

        # blit input box
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.update()
pygame.quit()
