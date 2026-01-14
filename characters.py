import arcade
import random

coin_texture = arcade.make_circle_texture(20, arcade.color.YELLOW)
player_texture = arcade.make_circle_texture(50, arcade.color.YELLOW)
enemy_texture = arcade.make_circle_texture(50, arcade.color.RED)
wall_texture = arcade.make_rectangle_texture(50, 50, arcade.color.BLUE)


class Coin(arcade.Sprite):
    def __init__(self, center_x, center_y, value=10):
        super().__init__()
        self.texture = coin_texture
        self.center_x = center_x
        self.center_y = center_y
        self.value = value


class Character(arcade.Sprite):
    def __init__(self, center_x, center_y, texture, speed=1):
        super().__init__()
        self.texture = texture
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed
        self.change_x = 0
        self.change_y = 0


class Player(Character):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, player_texture, speed=1)
        self.score = 0
        self.lives = 3

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Enemy(Character):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, enemy_texture, speed=1)
        self.time_to_change_direction = 0

    def pick_new_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
        direction = random.choice(directions)
        self.change_x = direction[0]
        self.change_y = direction[1]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self, delta_time=1/60):
        self.time_to_change_direction -= delta_time

        if self.time_to_change_direction <= 0:
            self.pick_new_direction()

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Wall(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.texture = wall_texture
        self.center_x = center_x
        self.center_y = center_y
