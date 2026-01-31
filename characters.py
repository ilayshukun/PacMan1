import random
import arcade
from pyglet.resource import texture

from constants import TILE_SIZE
radius = TILE_SIZE // 2 - 2
import arcade
from constants import TILE_SIZE

class Fruit(arcade.Sprite):
    def __init__(self, center_x, center_y, image_path, value):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.value = value
        self.texture = arcade.load_texture(image_path)
        self.width = 26
        self.height = 26

class Apple(Fruit):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, "assets/apple.png", value=1)

class Banana(Fruit):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, "assets/banana.png", value=2)

class Eggplant(Fruit):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, "assets/eggplant.png", value=3)

class Peach(Fruit):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, "assets/peach.png", value=4)


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
        self.texture = arcade.load_texture("assets/player.png")
        self.width = 25
        self.height = 32

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

class Enemy(Character):
    def __init__(self, center_x, center_y, speed):
        super().__init__(center_x, center_y, speed)
        self.direction_change_to_time = 0
        self.texture = arcade.load_texture("assets/enemy.png")

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

class Teleport(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture = arcade.load_texture("assets/teleport.png")

