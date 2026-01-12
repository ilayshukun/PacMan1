import arcade
import random

PACMAN_COLOR = arcade.color.YELLOW
GHOST_COLOR = arcade.color.RED
COIN_COLOR = arcade.color.YELLOW
WALL_COLOR = arcade.color.BLUE

pacman_texture = arcade.make_circle_texture(50, PACMAN_COLOR)
ghost_texture = arcade.make_circle_texture(50, GHOST_COLOR)
coin_texture = arcade.make_circle_texture(20, COIN_COLOR)
wall_texture = arcade.make_rectangle_texture(50, 50, WALL_COLOR)


class Character:
    def __init__(self, texture, speed=5):
        self.texture = texture
        self.width = self.texture.width
        self.height = self.texture.height
        self.speed = speed
        self.x = 0
        self.y = 0


class Pacman(Character):
    def __init__(self):
        super().__init__(pacman_texture)


class Ghost(Character):
    def __init__(self):
        super().__init__(ghost_texture)

    def move_random(self):
        self.x += random.choice([-self.speed, 0, self.speed])
        self.y += random.choice([-self.speed, 0, self.speed])


class Coin:
    def __init__(self):
        self.texture = coin_texture
        self.width = self.texture.width
        self.height = self.texture.height
        self.x = 0
        self.y = 0


class Wall:
    def __init__(self):
        self.texture = wall_texture
        self.width = self.texture.width
        self.height = self.texture.height
        self.x = 0
        self.y = 0

