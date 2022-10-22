import pygame
import numpy as np
import stages


class Game:

    def __init__(self, screen):
        self.run_ = False
        self.stages = stages.Stages()
        self.level = 1
        self.rec_level = 1
        self.no_exit = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.button = Button(self.screen, 3, 3, 30)
        self.touch_move = False
        self.screen.fill([255, 255, 255])
        self.gravity = 0
        self.player = Player(50, 200)
        self.rects = []
        self.spikes = []
        self.player_touch_ground = False
        self.create_level()

    def run(self):
        self.clock.tick(60)
        self.screen.fill([255, 255, 255])
        self.player_action()
        self.test_level_completion()
        self.reset_screen()  # incl. respawn by death or level-completion
        self.create_level()

    def create_level(self):  # resets level by completion to next level
        if self.level != self.stages.level:
            self.rects.clear()
            self.spikes.clear()
        self.spikes, self.rects = self.stages.create_stage(self.level)

    def test_level_completion(self):  # incl. death by falling out of map
        if self.player.position[0] >= 800:
            if self.level == self.rec_level:
                self.rec_level += 1
            self.level += 1
            self.respawn(death=False)

        if self.player.position[1] >= 400:
            self.respawn(death=True)

    def respawn(self, death=True):
        if death:
            self.player.position = np.array([50, 100])
        else:
            self.player.position = np.array([50, 100])

    def reset_screen(self):
        self.player.reset(self.screen)
        for rect in self.rects:
            rect.reset(self.screen)
        for spike in self.spikes:
            spike.reset(self.screen)
        self.player_touch_ground = False
        if not self.player_touch_ground:

            # with death
            for rect in self.rects:
                if rect.death_var is True:
                    if self.player.position[1] + 14 >= rect.position[1]:
                        if self.player.position[1] - 10 <= rect.position[1] + rect.size[1]:
                            if rect.position[0] <= self.player.position[0] + 5:
                                if self.player.position[0] - 5 <= rect.position[0] + rect.size[0]:
                                    self.player_touch_ground = True
                                    if self.player_touch_ground:
                                        if rect.death_var is False:
                                            break
                                        else:
                                            self.respawn(death=True)

            # without death
            for rect in self.rects:
                if self.player.position[1] + 14 >= rect.position[1]:
                    if self.player.position[1] - 10 <= rect.position[1] + rect.size[1]:
                        if rect.position[0] <= self.player.position[0] + 5:
                            if self.player.position[0] - 5 <= rect.position[0] + rect.size[0]:
                                self.player_touch_ground = True

        # test for spike-death
        for spike in self.spikes:
            if self.player.position[1] + 14 >= spike.position[1] - 15:
                if self.player.position[1] - 20 <= spike.position[1]:
                    if spike.position[0] <= self.player.position[0] + 5:
                        if self.player.position[0] - 5 <= spike.position[0] + 15:
                            self.respawn(death=True)

        self.button.draw()

        pygame.display.flip()

    def player_action(self):  # test player moving-action (moving left, right AND jumping)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.no_exit = False

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.move_is_available(direction='right'):
                self.player.move(5, 0)

        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.move_is_available(direction='left'):
                self.player.move(-5, 0)

        self.test_moving()
        if self.gravity < 0 and self.player_touch_ground:
            self.player.fall(20)
            self.gravity = 0
        else:
            self.player_jump(pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_SPACE]
                             or pygame.key.get_pressed()[pygame.K_UP])

        if pygame.key.get_pressed()[pygame.K_r]:
            self.respawn(death=True)

        if self.button.get_clicked():
            self.run_ = False

    def move_is_available(self, direction='right'):
        possible = True

        # false if touched Rectangle
        for rect in self.rects:

            # if went to right direction
            if direction == 'right':
                if self.player.position[1] >= rect.position[1]:
                    if self.player.position[1] <= rect.position[1] + rect.size[1]:
                        if self.player.position[0] + 10 >= rect.position[0]:
                            if self.player.position[0] + 10 <= rect.position[0] + rect.size[0]:
                                if rect.death_var is False:
                                    possible = False
                                else:
                                    self.respawn(death=True)

            # if went to left direction
            if direction == 'left':
                if self.player.position[1] >= rect.position[1]:
                    if self.player.position[1] <= rect.position[1] + rect.size[1]:
                        if self.player.position[0] - 10 >= rect.position[0]:
                            if self.player.position[0] - 10 <= rect.position[0] + rect.size[0]:
                                if rect.death_var is False:
                                    possible = False
                                else:
                                    self.respawn(death=True)

            if self.player.position[0] - 10 < 1 and direction == 'left':
                # player can not go out of map on the left side
                possible = False

        return possible

    def player_jump(self, jump_bool):

        if self.player_touch_ground:
            self.gravity = 0
            if jump_bool:
                self.gravity = -15
        else:
            if not self.gravity > 9:
                self.gravity += 1
        self.player.fall(self.gravity)

    def test_moving(self):
        self.mpv = False
        for rect in self.rects:
            rect.move()
            if self.player.position[1] + 14 >= rect.position[1]:
                if self.player.position[1] - 10 <= rect.position[1] + rect.size[1]:
                    if rect.position[0] <= self.player.position[0] + 5:
                        if self.player.position[0] - 5 <= rect.position[0] + rect.size[0]:
                            if rect.death_var is False:
                                if rect.move_var:
                                    if not rect.arrived_h:
                                        self.player.move(rect.step_x, 0)
                                    else:
                                        self.player.move(-rect.step_x, 0)

                                    if not rect.arrived_v:
                                        self.player.move(0, rect.step_y)
                                        if rect.bdv == 'DOWN':
                                            pass
                                    else:
                                        self.player.move(0, -rect.step_y)
                                        if rect.bdv == 'UP':
                                            pass
                            else:
                                self.respawn(death=True)


class Player:

    def __init__(self, xp, yp):
        self.position = np.array([xp, yp])

    def move(self, x, y):
        self.position += np.array([x, y])

    def fall(self, gravity):
        self.position[1] += gravity

    def respawn(self):
        self.position = np.array([50, 200])

    def reset(self, screen):
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), (self.position[0], self.position[1]), 10)


class Button:

    def __init__(self, screen, xp, yp, w):
        self.pos = np.array([xp, yp])
        self.w = w
        self.screen = screen

    def get_clicked(self):
        click = pygame.mouse.get_pressed()[0]
        m_x, m_y = pygame.mouse.get_pos()
        clicked = False

        if click:
            if m_x <= self.pos[0] + self.w:
                if m_x >= self.pos[0]:
                    if m_y <= self.pos[1] + self.w:
                        if m_y >= self.pos[1]:
                            clicked = True

        return clicked

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), (self.pos[0], self.pos[1], self.w, self.w))
        pygame.draw.line(self.screen, pygame.Color(0, 0, 0), (self.pos[0]+5, self.pos[1]+5),
                                                              (self.pos[0]+self.w-5, self.pos[1]+self.w-5), 5)
        pygame.draw.line(self.screen, pygame.Color(0, 0, 0), (self.pos[0] + 5, self.pos[1]+self.w-5),
                         (self.pos[0] + self.w - 5, self.pos[1] + 5), 5)
