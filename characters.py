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

class Character(arcade.Sprite):
    def __init__(self, texture, speed=5):
        super().__init__()
        self.texture = texture
        self.speed = speed

class Pacman(Character):
    def __init__(self):
        super().__init__(pacman_texture)

class Ghost(Character):
    def __init__(self):
        super().__init__(ghost_texture)

    def move_random(self):
        self.center_x += random.choice([-self.speed, 0, self.speed])
        self.center_y += random.choice([-self.speed, 0, self.speed])

class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = coin_texture


class Wall(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = wall_texture
