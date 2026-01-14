"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""

TILE_SIZE = 32

LEVEL_MAP = [
    "###########",
    "#P....G...#",
    "#.........#",
    "###########",
]

import arcade

class PackmanGame (arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.BLACK
        self.start_x=0
        self.start_y=0
        self.game_over=False
        self.wall_list=arcade.SpriteList()
        self.coin_list=arcade.SpriteList()
        self.ghost_list=arcade.SpriteList()
        self.player_list=arcade.SpriteList()


def setup(self):
    self.wall_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    self.ghost_list = arcade.SpriteList()
    self.player_list = arcade.SpriteList()

    self.game_over = False

    rows = len(LEVEL_MAP)

    for row_idx, row in enumerate(LEVEL_MAP):
        for col_idx, cell in enumerate(row):

            x = col_idx * TILE_SIZE + TILE_SIZE / 2
            y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2

            if cell == "#":
                wall = arcade.Sprite()
                wall.texture = arcade.make_rectangle_texture( TILE_SIZE, TILE_SIZE, arcade.color.BLUE )
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

            elif cell == ".":
                coin = arcade.Sprite()
                coin.texture = arcade.make_circle_texture(
                    TILE_SIZE // 2, arcade.color.YELLOW
                )
                coin.center_x = x
                coin.center_y = y
                self.coin_list.append(coin)

            elif cell == "P":
                player = arcade.Sprite()
                player.texture = arcade.make_circle_texture(
                    TILE_SIZE, arcade.color.YELLOW
                )
                player.center_x = x
                player.center_y = y
                self.player_list.append(player)

            elif cell == "G":
                ghost = arcade.Sprite()
                ghost.texture = arcade.make_circle_texture(
                    TILE_SIZE, arcade.color.RED
                )
                ghost.center_x = x
                ghost.center_y = y
                self.ghost_list.append(ghost)
