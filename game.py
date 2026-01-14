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

        def on_draw(self):
            arcade.start_render()

            self.list_wall.draw()

            self.list_ghost.draw()

            self.list_coin.draw()

            self.list_player.draw()

        def on_draw(self):
            self.clear()
            arcade.draw_text(
                f"Score: {self.score}",
                10,
                self.window.height - 30,
                arcade.color.WHITE,
                16
            )
            arcade.draw_text(
                f"Lives: {self.lives}",
                10,
                self.window.height - 55,
                arcade.color.WHITE,
                16
            )

            if self.over_game:
                arcade.draw_text(
                    "GAME OVER",
                    self.window.width / 2,
                    self.window.height / 2,
                    arcade.color.RED,
                    40
                )
