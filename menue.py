import pygame
import numpy as np


class Menue:

    def __init__(self, screen):
        self.screen = screen
        self.rec_level = 1
        self.run_ = True
        self.no_exit = True
        self.current_level = None
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 23)
        self.buttons = []

    def run(self):
        self.clock.tick(60)
        self.screen.fill([255, 255, 255])
        self.draw_stuff()
        pygame.display.flip()
        self.input()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.no_exit = False

        for button in self.buttons:
            if button.get_clicked():
                self.current_level = button.level_handler
                self.run_ = False

    def draw_stuff(self):
        self.buttons.clear()
        level = 0
        for y in range(7):
            y_sum = 40 + y * 50
            for x in range(15):
                x_sum = 30 + x * 50
                self.buttons.append(Button(self.screen, x_sum, y_sum, level,
                                           level < self.rec_level))
                level += 1

        for button in self.buttons:
            button.draw()
            text = self.myfont.render('Jump and Run', True, (0, 0, 0))
            self.screen.blit(text, (300, -5))


class Button:

    def __init__(self, screen, xp, yp, level, unlocked):
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 15)
        self.pos = np.array([xp, yp])
        self.level_handler = level
        self.screen = screen
        if level < 1:
            self.unlocked = True
        else:
            self.unlocked = unlocked

    def get_clicked(self):
        click = pygame.mouse.get_pressed()[0]
        m_x, m_y = pygame.mouse.get_pos()
        clicked = False
        if click:
            if m_x <= self.pos[0] + 30:
                if m_x >= self.pos[0]:
                    if m_y <= self.pos[1] + 30:
                        if m_y >= self.pos[1]:
                            if self.unlocked:
                                clicked = True

        return clicked

    def draw(self):
        if self.unlocked:
            pygame.draw.rect(self.screen, pygame.Color(255, 162, 0), (self.pos[0], self.pos[1], 30, 30))
        else:
            pygame.draw.rect(self.screen, pygame.Color(135, 133, 128), (self.pos[0], self.pos[1], 30, 30))
        text = self.myfont.render(str(self.level_handler+1), True, (255, 255, 255))
        text_y = 3
        if len(str(self.level_handler)) == 1:
            self.screen.blit(text, (self.pos[0]+11, self.pos[1]+text_y))
        elif len(str(self.level_handler)) == 2:
            self.screen.blit(text, (self.pos[0]+7, self.pos[1]+text_y))
        elif len(str(self.level_handler)) == 3 and self.level_handler != 100:
            self.screen.blit(text, (self.pos[0] + 3, self.pos[1] + text_y))
        elif len(str(self.level_handler)) == 3 and self.level_handler == 100:
            self.screen.blit(text, (self.pos[0], self.pos[1] + text_y))
