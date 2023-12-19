import pygame
from network import Network
import pickle

pygame.font.init()

width = 700
height = 700

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        return self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height
     
def redrawWindow(win, game, p):
    win.fill((128, 128, 128))
    pass

def main():
    pass

if __name__ == "__main__":
    main()
