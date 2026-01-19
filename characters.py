import arcade

class Pacman(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_circle_texture(32, arcade.color.YELLOW)
        self.width = 32
        self.height = 32

class Ghost(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_circle_texture(32, arcade.color.RED)
        self.width = 32
        self.height = 32

class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_circle_texture(8, arcade.color.YELLOW)
        self.width = 16
        self.height = 16

class Wall(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(32, arcade.color.BLUE )
        self.width = 32
        self.height = 32