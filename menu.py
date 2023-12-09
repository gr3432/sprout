import pygame
from settings import *

class Menu:
    def __init__(self, player, toggle_menu):
        # general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("../font/LycheeSoda.ttf", 30)

        # options
        self.width = 400
        self.space = 10
        self.padding = 8

        # entries
        self.options = list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys())
        self.sell_border = len(self.player.item_inventory) - 1
        self.setup()

    def setup(self):
        self.text_surfaces = []
        for item in self.options:
            text_surf = self.font.render(item, False, 'Black')
            self.text_surfaces.append(text_surf)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

    def update(self):
        self.input()
        for text_index, text_surf in enumerate(self.text_surfaces):
            self.display_surface.blit(text_surf, (100, text_index * 50))