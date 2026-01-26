import random
import arcade
from pyglet.resource import texture

from constants import TILE_SIZE
radius = TILE_SIZE // 2 - 2
class Coin(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.value = 0
        self.texture = arcade.make_circle_texture(TILE_SIZE // 2 -6, color=arcade.color.GOLD)
        self.width = self.texture.width
        self.height = self.texture.height
class Character(arcade.Sprite):
    def __init__(self, center_x, center_y, speed):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed
        self.change_x = 0
        self.change_y = 0

class Player(Character):
    def __init__(self, center_x, center_y, speed, score, lives):
        super().__init__(center_x, center_y, speed)
        self.score = score
        self.lives = lives
        self.texture = arcade.make_circle_texture(TILE_SIZE // 2, arcade.color.YELLOW)
        self.width = self.texture.width
        self.height = self.texture.height


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

class Enemy(Character):
    def __init__(self, center_x, center_y, speed):
        super().__init__(center_x, center_y, speed)
        self.direction_change_to_time = 0
        self.texture = arcade.make_circle_texture(TILE_SIZE // 2, color=arcade.color.RED)
        self.width = self.texture.width
        self.height = self.texture.height
    def pick_new_direction(self):
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (0, 0)
        ]
        self.change_x, self.change_y = random.choice(directions)
        self.direction_change_to_time = random.uniform(0.3, 1.0)

    def update(self, delta_time=1/60):
        self.direction_change_to_time -= delta_time

        if self.direction_change_to_time <= 0:
            self.pick_new_direction()

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Wall(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture = arcade.make_soft_square_texture(
            TILE_SIZE,
            arcade.color.BLUE,
            outer_alpha=255
        )
        self.width = self.texture.width
        self.height = self.texture.height