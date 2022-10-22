import game
import pygame
import menue


class BaseGame:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Jump and Run')
        self.game_ = game.Game(self.screen)
        self.menue_ = menue.Menue(self.screen)
        self.in_progress = True

    def run_game(self):

        self.game_.level = self.menue_.current_level
        self.game_.level += 1
        self.game_.run_ = True
        #  self.game_.stages.level = self.game_.level
        self.game_.respawn()
        while self.game_.run_ and self.game_.no_exit and self.menue_.no_exit:
            self.game_.run()
        self.game_.rects.clear()
        self.game_.spikes.clear()
        self.game_.stages.current_level = -1  # Dieser level exisitert nicht

    def run_menue(self):
        self.menue_.run_ = True
        while self.menue_.run_ and self.game_.no_exit and self.menue_.no_exit:
            self.menue_.rec_level = self.game_.rec_level
            self.menue_.run()

    def run_all(self):
        while self.game_.no_exit and self.menue_.no_exit:
            self.run_menue()

            self.run_game()


if __name__ == '__main__':
    mainGame = BaseGame()
    mainGame.run_all()
