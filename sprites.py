from timer import Timer
import pygame
from settings import *
from random import randint, choice

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75,)

class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.name = name

class Water(Generic):
    def __init__(self, pos, frames, groups):
        # animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos, 
            self.frames[self.frame_index],
            groups,
            LAYERS['water'])
        
    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)

class WildFlower(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)

class Particle(Generic):
    def __init__(self, pos, surf, groups, z, duration = 200):
        super().__init__(pos, surf, groups, z)
        self.start_time = pygame.time.get_ticks()
        self.duration = duration

        # white surface
        mask_surf = pygame.mask.from_surface(self.image)
        new_surf = mask_surf.to_surface()
        new_surf.set_colorkey((0, 0, 0)) # black
        self.image = new_surf

    def update(self, dt):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > self.duration:
            self.kill()

class Tree(Generic):
    def __init__(self, pos, surf, groups, name, player_add):
        super().__init__(pos, surf, groups)
        
        self.all_sprites = groups[0]

        # tree attributes
        self.health = 5
        self.alive = True
        stump_path = f"../graphics/stumps/{'small' if name == 'Small' else 'large'}.png"
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()

        # apples
        self.apple_surf = pygame.image.load("../graphics/fruit/apple.png").convert_alpha()
        self.apple_pos = APPLE_POS[name]
        self.apple_sprites = pygame.sprite.Group()
        self.create_fruit()

        self.player_add = player_add

        # sounds
        self.axe_sound = pygame.mixer.Sound("../audio/axe.mp3")

    def damage(self):
        # damage tree
        self.health -= 1

        # play sound
        self.axe_sound.play()

        # remove apple
        if len(self.apple_sprites.sprites()) > 0:
            random_apple = choice(self.apple_sprites.sprites())
            Particle(random_apple.rect.topleft, random_apple.image, self.all_sprites, LAYERS['fruit'])
            self.player_add('apple')
            random_apple.kill()

    def check_death(self):
        if self.health <= 0:
            Particle(
                pos = self.rect.topleft,
                surf = self.image,
                groups = self.all_sprites,
                z = LAYERS['fruit'],
                duration = 300
            )
            self.image = self.stump_surf
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            self.hitbox = self.rect.copy().inflate(-10, -self.rect.height * 0.6)
            self.alive = False
            self.player_add('wood')

    def update(self, dt):
        if self.alive:
            self.check_death()

    def create_fruit(self):
        for pos in self.apple_pos:
            if randint(0, 10) < 2:
                x = self.rect.left + pos[0]
                y = self.rect.top + pos[1]
                a = Generic((x, y), self.apple_surf, [self.apple_sprites, self.all_sprites], LAYERS['fruit'])