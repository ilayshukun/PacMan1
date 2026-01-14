"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""
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

