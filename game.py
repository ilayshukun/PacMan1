"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""
from turtledemo.clock import setup

import arcade

from constants import  WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE, LEVEL_MAP
from characters import Pacman, Ghost, Coin, Wall

class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = None
        self.game_over = False
        self.background_color = arcade.color.BLACK
        self.start_x = 0
        self.start_y = 0

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
                    wall = Wall()
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

                elif cell == ".":
                    coin = Coin()
                    coin.center_x = x
                    coin.center_y = y
                    self.coin_list.append(coin)

                elif cell == "P":
                    self.player = Pacman()
                    self.player.center_x = x
                    self.player.center_y = y
                    self.player_list.append(self.player)

                elif cell == "G":
                    ghost = Ghost()
                    ghost.center_x = x
                    ghost.center_y = y
                    self.ghost_list.append(ghost)

    def on_draw(self):
        self.clear()

        self.wall_list.draw()
        self.ghost_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        arcade.draw_text("Score: 0",  10,  WINDOW_HEIGHT - 20,  arcade.color.WHITE,  14  )

        arcade.draw_text("Lives: 3", 10, WINDOW_HEIGHT - 40, arcade.color.WHITE,14 )

        if self.game_over:
            arcade.draw_text("GAME OVER", WINDOW_WIDTH / 2 - 80,  WINDOW_HEIGHT / 2, arcade.color.RED,24)

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP:
            self.player.center_y = 0
        elif key == arcade.key.DOWN:
            self.player.center_y = 0
        elif key == arcade.key.RIGHT:
            self.player.center_x = 0
        elif key == arcade.key.LEFT:
            self.player.center_x = 0




    def on_key_press(self, key, modifers):
        if self.game_over == True:
            if key == arcade.key.Space:
                setup()
        if key == arcade.key.Up:
            self.player.center_y = 1
        elif key == arcade.key.Down:
            self.player.center_y = -1
        elif key == arcade.key.Right:
            self.player.center_x = 1
        elif key == arcade.key.Left:
            self.player.center_x = -1

