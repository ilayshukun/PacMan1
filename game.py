"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""
from turtledemo.clock import setup

import arcade
from typing_extensions import Final
import random
from constants import  WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE, LEVEL_MAP
from characters import Player, Enemy, Apple,Banana, Wall, Teleport,Eggplant,Peach
class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = None
        self.game_over = False
        self.win = False
        self.background_color = arcade.color.BLACK
        self.start_x = 1.5*TILE_SIZE
        self.start_y = 1.5*TILE_SIZE
        self.teleport_list = arcade.SpriteList()
        self.teleport_cooldown = 0

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.game_over = False
        self.win = False

        rows = len(LEVEL_MAP)

        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2

                if cell == "#":
                    wall = Wall(x,y)
                    self.wall_list.append(wall)
                elif cell == ".":

                    fruit_class = random.choice([Apple, Eggplant, Banana, Peach])
                    fruit = fruit_class(x, y)
                    self.coin_list.append(fruit)
                elif cell == "P":
                    self.player = Player(x,y,2,0,3)
                    self.player_list.append(self.player)
                elif cell == "G":
                    ghost = Enemy(x,y,2)
                    self.ghost_list.append(ghost)
                elif cell == "T":
                    teleport = Teleport(x, y)
                    self.teleport_list.append(teleport)
        if self.player is None:
            self.player = Player(self.start_x, self.start_y, 2, 0, 3)
            self.player_list.append(self.player)


    def on_draw(self):
        self.clear()

        self.wall_list.draw()
        self.ghost_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.teleport_list.draw()

        arcade.draw_text(f"Score: {self.player.score}",  10,  WINDOW_HEIGHT - 20,  arcade.color.WHITE,  14  )

        arcade.draw_text(f"Lives: {self.player.lives}", 10, WINDOW_HEIGHT - 40, arcade.color.WHITE,14 )

        if self.game_over:
            arcade.draw_text("GAME OVER", WINDOW_WIDTH / 2 - 80,  WINDOW_HEIGHT / 2, arcade.color.RED,24)
        if self.win:
            arcade.draw_text("YOU WIN!",WINDOW_WIDTH / 2 - 80,WINDOW_HEIGHT / 2,arcade.color.GREEN,24
            )


    def on_update(self, delta_time):

        if self.game_over or self.win:
            return
        old_x = self.player.center_x
        old_y = self.player.center_y
        self.player.move()


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
            self.player.score += coin.value

        if len(self.coin_list) == 0:
            self.win = True

        ghosts_hit = arcade.check_for_collision_with_list(self.player, self.ghost_list)
        if ghosts_hit:
            self.player.lives -= 1

            self.player.center_x = self.start_x
            self.player.center_y = self.start_y

            if self.player.lives <= 0:
                self.game_over = True

        if self.teleport_cooldown > 0:
            self.teleport_cooldown -= delta_time

        if self.teleport_cooldown <= 0:
            teleports_hit = arcade.check_for_collision_with_list(
                self.player, self.teleport_list
            )

            if teleports_hit:
                current = teleports_hit[0]

                for teleport in self.teleport_list:
                    if teleport is not current:
                        self.player.center_x = teleport.center_x
                        self.player.center_y = teleport.center_y
                        self.teleport_cooldown = 0.5
                        break

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 0
        elif key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.LEFT:
            self.player.change_x = 0




    def on_key_press(self, key, modifiers):
        if self.game_over or self.win:
            if key == arcade.key.SPACE:
                self.setup()
            return
        if key == arcade.key.UP:
            self.player.change_y = 1
        elif key == arcade.key.DOWN:
            self.player.change_y = -1
        elif key == arcade.key.RIGHT:
            self.player.change_x = 1
        elif key == arcade.key.LEFT:
            self.player.change_x = -1

