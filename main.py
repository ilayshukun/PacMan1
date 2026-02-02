"""
נקודת הכניסה למשחק פקמן.

אחראית על:
- יצירת חלון Arcade
- יצירת אובייקט PacmanGame
- אתחול המשחק
- הרצת לולאת המשחק
"""
import arcade
from constants import WINDOW_WIDTH, WINDOW_HEIGHT,WINDOW_TITLE
from game import PacmanGame

def main():
    """פונקציית main שמריצה את המשחק."""
    window = arcade.Window(
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        WINDOW_TITLE,
    )
    game = PacmanGame()
    game.setup()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
