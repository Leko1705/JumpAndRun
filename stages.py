import pygame
import numpy as np


class Stages:

    def __init__(self):
        self.level = None
        self.current_level = None
        self.rects = []
        self.spikes = []

    def create_stage(self, level):
        self.level = level
        if self.current_level != self.level:
            self.rects.clear()
            if self.level == 1:
                self.rects.append(Rectangle(0, 300, 800, 100))
            elif self.level == 2:
                self.rects.append(Rectangle(0, 300, 800, 100))
                self.spikes.append(Spike(395, 300))
            elif self.level == 3:
                self.rects.append(Rectangle(0, 300, 100, 100))
                self.rects.append((Rectangle(200, 300, 100, 100)))
                self.rects.append((Rectangle(400, 300, 100, 100)))
                self.rects.append((Rectangle(600, 300, 100, 100)))
            elif self.level == 4:
                self.rects.append((Rectangle(0, 300, 100, 100)))
                self.rects.append((Rectangle(200, 250, 100, 150)))
                self.rects.append((Rectangle(400, 200, 100, 200)))
                self.rects.append((Rectangle(600, 150, 100, 250)))
            elif self.level == 5:
                self.rects.append((Rectangle(0, 300, 100, 100)))
                self.rects.append((Rectangle(200, 250, 100, 150)))
                self.rects.append((Rectangle(400, 200, 100, 50)))
                self.spikes.append(Spike(445, 200))
                self.rects.append((Rectangle(600, 300, 200, 100)))
            elif self.level == 6:
                self.rects.append(Rectangle(0, 300, 800, 100))
                self.rects.append(Rectangle(350, 100, 450, 200))
                self.rects.append(Rectangle(130, 250, 30, 10))
                self.rects.append(Rectangle(180, 200, 30, 10))
                self.rects.append(Rectangle(230, 150, 30, 10))
                self.spikes.append((Spike(600, 100)))
            elif self.level == 7:
                self.rects.append(Rectangle(0, 300, 650, 100))
                self.rects.append(Rectangle(390, 100, 20, 200, death=True))
                self.rects.append(Rectangle(360, 200, 30, 10))
            elif self.level == 8:
                self.rects.append(Rectangle(0, 300, 375, 100))
                self.rects.append(Rectangle(435, 300, 575, 100))
                self.rects.append(Rectangle(100, 200, 600, 20))
                self.rects.append(Rectangle(0, 50, 100, 20))
                self.rects.append(Rectangle(100, 50, 20, 150))
                self.rects.append(Rectangle(200, 100, 600, 20))
                self.rects.append(Rectangle(770, 100, 30, 200))
                self.spikes.append((Spike(395, 200)))
                self.spikes.append((Spike(650, 200)))
                self.spikes.append((Spike(530, 100)))
            elif self.level == 9:
                self.rects.append(Rectangle(0, 300, 100, 100))
                self.rects.append(Rectangle(230, 250, 30, 10))
                self.rects.append(Rectangle(330, 200, 30, 10))
                self.rects.append(Rectangle(260, 170, 30, 10, death=True))
                self.rects.append(Rectangle(290, 300, 30, 10, death=True))
                self.rects.append(Rectangle(450, 130, 30, 10, death=True))
                self.rects.append(Rectangle(400, 180, 30, 10, death=True))
                self.rects.append(Rectangle(230, 100, 30, 10))
                self.rects.append(Rectangle(480, 250, 30, 10))
                self.rects.append(Rectangle(330, 70, 30, 10))
                self.rects.append(Rectangle(580, 150, 30, 10))
                self.rects.append(Rectangle(580, 320, 30, 10, death=True))
                self.rects.append(Rectangle(770, 390, 30, 10))
                self.spikes.append((Spike(790, 390)))
                self.spikes.append((Spike(780, 390)))
            elif self.level == 10:
                self.rects.append(Rectangle(0, 300, 100, 100))
                self.rects.append(Rectangle(700, 300, 100, 100))
                self.rects.append(Rectangle(600, 270, 50, 10, move=True, to_x=150, step_x=2, step_y=0))
            elif self.level == 11:
                self.rects.append(Rectangle(0, 300, 100, 100))
                self.rects.append(Rectangle(150, 100, 50, 10, move=True, to_y=350, step_x=0, step_y=2))
                self.rects.append(Rectangle(300, 350, 50, 10, move=True, to_y=100, step_x=0, step_y=2))
                self.rects.append(Rectangle(450, 100, 50, 10, move=True, to_y=350, step_x=0, step_y=2))
                self.rects.append(Rectangle(600, 350, 50, 10, move=True, to_y=100, step_x=0, step_y=2))
            elif self.level == 12:
                self.rects.append(Rectangle(0, 300, 100, 100))
                self.rects.append(Rectangle(750, 300, 50, 100))
                self.rects.append(Rectangle(150, 100, 50, 10, move=True, to_y=350, step_x=0, step_y=2))
                self.rects.append(Rectangle(200, 100, 50, 10, move=True, to_x=450, step_x=2, step_y=0))
                self.rects.append(Rectangle(700, 300, 50, 10, move=True, to_x=450, step_x=2, step_y=0))
                self.rects.append(Rectangle(500, 200, 50, 10, death=True, move=True, to_x=750, step_x=2, step_y=0))

            self.current_level = self.level

        return self.spikes, self.rects


class Rectangle:

    def __init__(self, xp, yp, xw, yw, death=False, move=False, to_x=False, to_y=False, step_x=0, step_y=0):
        self.position_s = np.array([xp, yp])
        self.position = np.array([xp, yp])
        self.size = np.array([xw, yw])
        self.death_var = death
        self.move_var = move
        self.to_x = to_x
        self.to_y = to_y
        self.step_x = abs(step_x)
        self.step_y = abs(step_y)
        self.arrived_h = False
        self.arrived_v = False
        self.color = (0, 0, 0)
        if self.death_var:
            self.color = (255, 0, 0)

        # bdh = beginning direction horizontal
        self.bdh = None
        if self.position_s[0] < self.to_x:
            self.bdh = 'RIGHT'
        else:
            self.bdh = 'LEFT'
            self.step_x *= -1
        if self.position_s[0] == self.to_x and step_x > 0:
            raise ValueError

        # bdv = beginning direction vertical
        self.bdv = None
        if self.position_s[1] < self.to_y:
            self.bdv = 'UP'
        else:
            self.bdv = 'DOWN'
            self.step_y *= -1
        if self.position_s[1] == self.to_y and step_y > 0:
            raise ValueError

    def move(self):
        if self.move_var:
            if self.bdh == 'RIGHT':
                if not self.arrived_h:
                    self.position[0] += self.step_x
                    if self.position[0] >= self.to_x:
                        self.arrived_h = True
                elif self.arrived_h:
                    self.position[0] -= self.step_x
                    if self.position[0] <= self.position_s[0]:
                        self.arrived_h = False

            if self.bdh == 'LEFT':
                if not self.arrived_h:
                    self.position[0] += self.step_x
                    if self.position[0] <= self.to_x:
                        self.arrived_h = True
                elif self.arrived_h:
                    self.position[0] -= self.step_x
                    if self.position[0] >= self.position_s[0]:
                        self.arrived_h = False

            if self.bdv == 'UP':
                if not self.arrived_v:
                    self.position[1] += self.step_y
                    if self.position[1] >= self.to_y:
                        self.arrived_v = True
                elif self.arrived_v:
                    self.position[1] -= self.step_y
                    if self.position[1] <= self.position_s[1]:
                        self.arrived_v = False

            if self.bdv == 'DOWN':
                if not self.arrived_v:
                    self.position[1] += self.step_y
                    if self.position[1] <= self.to_y:
                        self.arrived_v = True
                elif self.arrived_v:
                    self.position[1] -= self.step_y
                    if self.position[1] >= self.position_s[1]:
                        self.arrived_v = False

    def touch_player(self, x, y):
        z = False
        if x+10 <= self.position[0] + self.size[0]:
            if x-10 >= self.position[0]:
                if y+14 <= self.position[1] + self.size[1]:
                    if y+14 >= self.position[1]:
                        z = True
        return z

    def reset(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size[0],
                         self.size[1]))

    def death_var_(self):
        self.death_var = not self.death_var


class Spike:

    def __init__(self, xp, yp):
        self.position = np.array([xp, yp])
        self.ground_size = 1

    def reset(self, screen):
        pygame.draw.polygon(screen,
                            pygame.Color(0, 0, 0), ((self.position[0], self.position[1]),
                                                    (self.position[0] + 10, self.position[1]),
                                                    (self.position[0] + 5, self.position[1] - 15)))
