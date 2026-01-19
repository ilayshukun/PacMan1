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
        if self.player == None:
            self.player = Pacman()
            self.player.center_x = self.start_x
            self.player.center_y = self.start_y
            self.player_list.append(self.player)


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

    def on_update(self, delta_time):

        if self.game_over:
            return
        old_x = self.player.center_x
        old_y = self.player.center_y

        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            self.player.center_x = old_x
            self.player.center_y = old_y

        for ghost in self.ghost_list:
            old_x = ghost.center_x
            old_y = ghost.center_y

            ghost.update()

            if arcade.check_for_collision_with_list(ghost, self.wall_list):
                ghost.center_x = old_x
                ghost.center_y = old_y
                ghost.change_x *= -1
                ghost.change_y *= -1

        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.player.score += 1
        ghosts_hit = arcade.check_for_collision_with_list(self.player, self.ghost_list)
        if ghosts_hit:
            self.player.lives -= 1

            self.player.center_x = self.start_x
            self.player.center_y = self.start_y
            self.player.change_x = 0
            self.player.change_y = 0

            if self.player.lives5 <= 0:
                self.game_over = True


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
            if key == arcade.key.SPACE:
                setup()
        if key == arcade.key.UP:
            self.player.center_y = 1
        elif key == arcade.key.DOWN:
            self.player.center_y = -1
        elif key == arcade.key.RIGHT:
            self.player.center_x = 1
        elif key == arcade.key.LEFT:
            self.player.center_x = -1

