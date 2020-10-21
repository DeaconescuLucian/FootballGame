import pygame
import sys
import os
import numpy as np
from pygame import mixer



# import ctypes


class game:
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """

        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    pygame.init()
    clock = pygame.time.Clock()
    # user32 = ctypes.windll.user32
    # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode((800, 611))
    game_running = False
    game_time = 120
    start_ticks = 0
    current_time = 0
    game_pause_time = 0
    goal_time = 0
    impact_volume=1
    stadium_volume=0.5
    impact = mixer.Sound(resource_path('impact.wav'))
    impact.set_volume(1)
    stadium = mixer.music.load(resource_path('stadium.wav'))
    mixer.music.set_volume(1)
    def update_music_volume(self):
        mixer.music.set_volume(self.stadium_volume)

    def update_impact_volume(self):
        self.impact.set_volume(self.impact_volume)

    mixer.music.play(-1)
    # Menu
    menu_running = True
    buton_PlayIMG = pygame.image.load(resource_path("PLAY.png"))
    buton_PlayIMG.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    buton_PlayIMG_hover = pygame.image.load(resource_path("PLAY.png"))
    buton_OptionsIMG = pygame.image.load(resource_path("OPTIONS.png"))
    buton_OptionsIMG.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    buton_OptionsIMG_hover = pygame.image.load(resource_path("OPTIONS.png"))
    buton_InstructionsIMG = pygame.image.load(resource_path("INSTRUCTIONS.png"))
    buton_InstructionsIMG.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    buton_InstructionsIMG_hover = pygame.image.load(resource_path("INSTRUCTIONS.png"))
    buton_YesIMG = pygame.image.load(resource_path("YES.png"))
    buton_YesIMG.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    buton_YesIMG_hover = pygame.image.load(resource_path("YES.png"))
    buton_NoIMG = pygame.image.load(resource_path("NO.png"))
    buton_NoIMG.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    buton_NoIMG_hover = pygame.image.load(resource_path("NO.png"))
    pygame.display.set_caption(resource_path("First Game"))
    icon = pygame.image.load(resource_path("covid.png"))
    volume = pygame.image.load(resource_path("speaker.png"))
    volume_hover = pygame.image.load(resource_path("speaker.png"))
    volume_hover.fill((0, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    mute=pygame.image.load(resource_path("mute.png"))
    mute_hover = pygame.image.load(resource_path("mute.png"))
    mute_hover.fill((0, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    dot=pygame.image.load(resource_path("dot.png"))
    high_volume=pygame.image.load(resource_path("high-volume.png"))
    high_volume_hover = pygame.image.load(resource_path("high-volume.png"))
    high_volume_hover.fill((0, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    volume_bar=pygame.image.load(resource_path("VOLUME_BAR.png"))
    bot = pygame.image.load(resource_path("bot.png"))
    pygame.display.set_icon(icon)
    # Player
    playerImg = pygame.image.load(resource_path("panda.png"))
    playerName = "MARGARETH"
    # player2
    player2Img = pygame.image.load(resource_path("panda.png"))
    player2Name = "MARGARETH"
    # Ball
    ballImg = pygame.image.load(resource_path("ball.png"))
    # characters
    panda = pygame.image.load(resource_path("panda.png"))
    owl = pygame.image.load(resource_path("owl.png"))
    monkey = pygame.image.load(resource_path("monkey.png"))
    lion = pygame.image.load(resource_path("lion.png"))
    dragon = pygame.image.load(resource_path("dragon.png"))
    dog = pygame.image.load(resource_path("dog.png"))
    crocodile = pygame.image.load(resource_path("crocodile.png"))
    cat = pygame.image.load(resource_path("cat.png"))
    characters = [panda, owl, monkey, lion, dragon, dog, crocodile, cat]
    character_names = ["MARGARETH", "ARTHUR", "CHAMP", "SIMBA", "FINN", "STAN", "BOBBY", "FIGARO"]
    # Arrows
    previous = pygame.image.load(resource_path("previous.png"))
    previous_hover = pygame.image.load(resource_path("previous.png"))
    previous_hover.fill((0, 128, 51), special_flags=pygame.BLEND_RGB_ADD)
    next = pygame.image.load(resource_path("next.png"))
    next_hover = pygame.image.load(resource_path("next.png"))
    next_hover.fill((0, 128, 51), special_flags=pygame.BLEND_RGB_ADD)
    up = pygame.image.load(resource_path("UP.png"))
    up.fill((0, 51, 51), special_flags=pygame.BLEND_RGB_ADD)
    up_hover = pygame.image.load(resource_path("UP.png"))
    up_hover.fill((0, 128, 128), special_flags=pygame.BLEND_RGB_ADD)
    down = pygame.image.load(resource_path("DOWN.png"))
    down.fill((0, 51, 51), special_flags=pygame.BLEND_RGB_ADD)
    down_hover = pygame.image.load(resource_path("DOWN.png"))
    down_hover.fill((0, 128, 128), special_flags=pygame.BLEND_RGB_ADD)

    # Bari
    bara1 = pygame.image.load(resource_path("bara.png"))
    bara2 = pygame.image.load(resource_path("bara.png"))
    bara3 = pygame.image.load(resource_path("bara.png"))
    bara4 = pygame.image.load(resource_path("bara.png"))
    score_player = 0
    score_player2 = 0
    # Boosts
    speed = pygame.image.load(resource_path("speed.png"))
    speed01 = pygame.image.load(resource_path("speed(1).png"))
    slow = pygame.image.load(resource_path("slow.png"))
    slow1 = pygame.image.load(resource_path("slow(1).png"))
    freeze = pygame.image.load(resource_path("snowflake.png"))
    freeze1 = pygame.image.load(resource_path("snowflake(1).png"))
    boosts = [speed, slow, freeze]
    boosts1 = [speed, slow, freeze]
    boosts2 = [speed, slow, freeze]
    boost1X = [0, 0, 0]
    boost2X = [0, 0, 0]
    collect1 = [0, 0, 0]
    collect2 = [0, 0, 0]
    collect_time1 = [0, 0, 0]
    collect_time2 = [0, 0, 0]

    font = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 12)
    font3 = pygame.font.Font('freesansbold.ttf', 18)
    textX = 10
    textY = 10
    goal_textY = 280
    goal_textX = 300

    def text(self, text, x, y):
        text_display = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_display, (x, y))

    def text2(self, text, x, y):
        text_display = self.font2.render(text, True, (255, 255, 255))
        self.screen.blit(text_display, (x, y))

    def text3(self, text, x, y):
        text_display = self.font3.render(text, True, (255, 255, 255))
        self.screen.blit(text_display, (x, y))

    posesie = 0
    playerX = 370
    playerY = 480
    speed1 = 0.25
    speed2 = 0.25
    playerX_speed = 0
    player2X = 370
    player2Y = 94
    player2X_speed = 0
    ballX = 768
    ballY = 512
    ballY_speed = -0.15
    ballX_speed = 0
    ball_state = 1
    win_score = 10
    game_state = 1
    bot_range=200

    def bari(self):
        self.screen.blit(self.bara1, (0, 544))
        self.screen.blit(self.bara2, (600, 544))
        self.screen.blit(self.bara1, (0, 56))
        self.screen.blit(self.bara1, (600, 56))

    def img_load(self, img, x, y):
        self.screen.blit(img, (x, y))

    def player(self):
        self.screen.blit(self.playerImg, (self.playerX, self.playerY))

    def player2(self):
        self.screen.blit(self.player2Img, (self.player2X, self.player2Y))

    def ball(self):
        self.screen.blit(self.ballImg, (self.ballX, self.ballY))

    def character(self, no, x, y):
        self.screen.blit(self.characters[no], (x, y))

    def arrow(self, arrow, x, y):
        self.screen.blit(arrow, (x, y))

    options_running = False
    instructions_running = False

    def menu(self):
        while self.menu_running:
            self.screen.fill((0, 128, 128))
            self.screen.fill((0, 51, 51), (0, 0, 800, 50))
            self.screen.fill((0, 51, 51), (0, 561, 800, 50))
            self.text("MENU", 325, 100)
            mx, my = pygame.mouse.get_pos()
            if (mx > 275 and mx < 475 and my > 200 and my < 235):
                self.img_load(self.buton_PlayIMG_hover, 275, 200)
            else:
                self.img_load(self.buton_PlayIMG, 275, 200)
            if (mx > 275 and mx < 475 and my > 300 and my < 335):
                self.img_load(self.buton_OptionsIMG_hover, 275, 300)
            else:
                self.img_load(self.buton_OptionsIMG, 275, 300)
            if (mx > 275 and mx < 475 and my > 400 and my < 435):
                self.img_load(self.buton_InstructionsIMG_hover, 275, 400)
            else:
                self.img_load(self.buton_InstructionsIMG, 275, 400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.instructions_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (mx > 275 and mx < 475 and my > 200 and my < 235):
                            self.game_running = True
                            self.menu_running = False
                            if self.game_mode == "PVP":
                                self.game()
                            elif self.game_mode == "PVC":
                                self.game_PVC()
                            else:
                                self.game_CVC()

                        elif (mx > 275 and mx < 475 and my > 300 and my < 335):
                            self.options_running = True
                            self.menu_running = False
                            self.options()

                        elif (mx > 275 and mx < 475 and my > 400 and my < 435):
                            self.instructions_running = True
                            self.menu_running = False
                            self.instructions()

            pygame.display.update()

    def instructions(self):
        while self.instructions_running:
            self.screen.fill((0, 51, 51))
            mx, my = pygame.mouse.get_pos()
            self.text("INSTRUCTIONS", 300, 100)
            self.text3("CONTROLS:", 25, 150)
            self.text3("        PLAYER 1 : ", 25, 180)
            self.text3("                MOVE LEFT :  <", 25, 210)
            self.text3("                MOVE RIGHT : >", 25, 240)
            self.text3("                HIT / LAUNCH THE BALL : SPACE", 25, 270)
            self.text3("        PLAYER 2 : ", 25, 300)
            self.text3("                MOVE LEFT :  A", 25, 330)
            self.text3("                MOVE RIGHT : D", 25, 360)
            self.text3("                HIT / LAUNCH THE BALL : TAB", 25, 390)
            self.text3("NAVIGATION:", 25, 420)
            self.text3("        USE ESC TO EXIT THE GAME OR OTHER MENUS ", 25, 450)
            if mx > 368 and mx < 432 and my > 545 and my < 609:
                self.img_load(self.down_hover, 368, 545)
            else:
                self.img_load(self.down, 368, 545)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.instructions_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_running = True
                        self.instructions_running = False
                        self.menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mx > 368 and mx < 432 and my > 545 and my < 609:
                            self.instructions2_running = True
                            self.instructions_running = False
                            self.instructions2()
            pygame.display.update()

    instructions2_running = False

    def instructions2(self):
        while self.instructions2_running:
            self.screen.fill((0, 51, 51))
            mx, my = pygame.mouse.get_pos()
            self.text3("BOOSTS: ", 25, 100)
            self.img_load(self.speed, 75, 130)
            self.text3("INCREASE YOUR CHARACTER MOVEMENT SPEED FOR 5 SECONDS.", 75, 160)
            self.img_load(self.slow, 75, 190)
            self.text3("DECREASE OPPONENT'S CHARACTER MOVEMENT SPEED FOR 5 SECONDS.", 75, 220)
            self.img_load(self.freeze, 75, 240)
            self.text3("STUNS YOU OPPONENT FOR 1.5 SECONDS.", 75, 280)
            self.text3("DURING THIS TIME HE CAN HIT THE BALL BUT HE CAN NOT MOVE AT ALL.", 75, 310)
            self.text3("CHARACTER SELECTION :", 25, 340)
            self.text3("        IN OPTIONS MENU YOU CHOOSE YOR FAVORITE CHARACTER :", 25, 370)
            self.img_load(self.panda, 50, 400)
            self.img_load(self.monkey, 120, 400)
            self.img_load(self.lion, 190, 400)
            self.img_load(self.crocodile, 260, 400)
            self.img_load(self.owl, 330, 400)
            self.img_load(self.dog, 400, 400)
            self.img_load(self.cat, 470, 400)
            self.img_load(self.dragon, 540, 400)
            if mx > 368 and mx < 432 and my > 0 and my < 64:
                self.img_load(self.up_hover, 368, 0)
            else:
                self.img_load(self.up, 368, 0)

            if mx > 368 and mx < 432 and my > 545 and my < 609:
                self.img_load(self.down_hover, 368, 545)
            else:
                self.img_load(self.down, 368, 545)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.instructions2_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_running = True
                        self.instructions_running2 = False
                        self.menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mx > 368 and mx < 432 and my > 0 and my < 64:
                            self.instructions2_running = False
                            self.instructions_running = True
                            self.instructions()
                        if mx > 368 and mx < 432 and my > 545 and my < 609:
                            self.instructions3_running = True
                            self.instructions2_running = False
                            self.instructions3()
            pygame.display.update()

    instructions3_running = False

    def instructions3(self):
        while self.instructions3_running:
            self.screen.fill((0, 51, 51))
            mx, my = pygame.mouse.get_pos()
            self.text3("GAME MODES: ", 25, 100)
            self.text3("    PVP ( PLAYER VERSUS PLAYER ) : ", 25, 130)
            self.text3("        HAVE FUN WITH YOUR FRIENDS IN THIS GAME MODE.  ", 25, 160)
            self.text3("    PVC ( PLAYER VERSUS COMPUTER ) : ", 25, 190)
            self.text3("        ONE HUMAN VERSUS ONE COMPUTER...WHO WILL WIN?  ", 25, 220)
            self.text3("    CVC ( COMPUTER VERSUS COMPUTER ) : ", 25, 250)
            self.text3("        YOU ARE TO LAZY TO PLAY THE GAME?  ", 25, 280)
            self.text3("        SEAT BACK,RELAX AND LET THE COMPUTER PLAY AGAINST HIMSELF.  ", 25, 310)
            self.text3(" !!! IF ONE OF THE PLAYERS REFUSES TO LAUNCH THE BALL AFTER TAKING A GOAL,", 25, 380)
            self.text3(" THE BALL WILL BE AUTOMATICALLY THROWN AFTER 4 SECONDS.  ", 25, 410)
            if mx > 368 and mx < 432 and my > 0 and my < 64:
                self.img_load(self.up_hover, 368, 0)
            else:
                self.img_load(self.up, 368, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.instructions3_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_running = True
                        self.instructions_running3 = False
                        self.menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mx > 368 and mx < 432 and my > 0 and my < 64:
                            self.instructions3_running = False
                            self.instructions2_running = True
                            self.instructions2()

            pygame.display.update()

    character_no1 = 0
    character_no2 = 0
    game_mode = "PVP"
    game_modes = ["PVP", "PVC", "CVC"]
    game_mode_poz = 0

    def options(self):
        while self.options_running:
            self.screen.fill((0, 51, 51))
            mx, my = pygame.mouse.get_pos()
            self.text("OPTIONS", 325, 100)
            self.text2("Player1", 380, 182)
            self.character(self.character_no1, 368, 200)
            if (mx > 450 and mx < 514 and my > 200 and my < 264):
                self.arrow(self.next_hover, 450, 200)
            else:
                self.arrow(self.next, 450, 200)
            if (mx > 286 and mx < 350 and my > 200 and my < 264):
                self.arrow(self.previous_hover, 286, 200)
            else:
                self.arrow(self.previous, 286, 200)
            self.text2(self.character_names[self.character_no1], 368, 270)
            self.text2("Player2", 380, 382)
            self.character(self.character_no2, 368, 400)
            if (mx > 450 and mx < 514 and my > 400 and my < 464):
                self.arrow(self.next_hover, 450, 400)
            else:
                self.arrow(self.next, 450, 400)
            if (mx > 286 and mx < 350 and my > 400 and my < 464):
                self.arrow(self.previous_hover, 286, 400)
            else:
                self.arrow(self.previous, 286, 400)
            self.text2(self.character_names[self.character_no2], 368, 470)
            self.text2(self.character_names[self.character_no2], 368, 470)

            if mx > 368 and mx < 432 and my > 545 and my < 609:
                self.img_load(self.down_hover, 368, 545)
            else:
                self.img_load(self.down, 368, 545)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.options_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_running = True
                        self.menu()
                        self.options_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (mx > 286 and mx < 350 and my > 200 and my < 264):
                            if (self.character_no1 - 1 >= 0):
                                self.character_no1 = self.character_no1 - 1
                                self.playerImg = self.characters[self.character_no1]
                                self.playerName = self.character_names[self.character_no1]
                        if (mx > 450 and mx < 514 and my > 200 and my < 264):
                            if (self.character_no1 + 1 <= len(self.characters) - 1):
                                self.character_no1 = self.character_no1 + 1
                                self.playerImg = self.characters[self.character_no1]
                                self.playerName = self.character_names[self.character_no1]
                        if (mx > 286 and mx < 350 and my > 400 and my < 464):
                            if (self.character_no2 - 1 >= 0):
                                self.character_no2 = self.character_no2 - 1
                                self.player2Img = self.characters[self.character_no2]
                                self.player2Name = self.character_names[self.character_no2]
                        if (mx > 450 and mx < 514 and my > 400 and my < 464):
                            if (self.character_no2 + 1 <= len(self.characters) - 1):
                                self.character_no2 = self.character_no2 + 1
                                self.player2Img = self.characters[self.character_no2]
                                self.player2Name = self.character_names[self.character_no2]
                        if mx > 368 and mx < 432 and my > 545 and my < 609:
                            self.options2_running = True
                            self.options_running = False
                            self.options2()

            pygame.display.update()

    options2_running=False
    mouse_pressed = 0
    def options2(self):
        while self.options2_running:
            self.screen.fill((0, 51, 51))
            mx, my = pygame.mouse.get_pos()
            if mx > 368 and mx < 432 and my > 0 and my < 64:
                self.img_load(self.up_hover, 368, 0)
            else:
                self.img_load(self.up, 368, 0)
            self.text3("MUSIC VOLUME:", 25, 128)

            if self.mouse_pressed==1 and mx > 100 and mx < 500 and my > 160 and my < 224:
                self.stadium_volume = (mx - 100) / 400
                self.update_music_volume()
            self.volume_settings(mx,my,25,160,self.stadium_volume)

            self.text3("SOUND VOLUME:", 25, 275)

            if self.mouse_pressed==1 and mx > 100 and mx < 500 and my > 297 and my < 361:
                self.impact_volume = (mx - 100) / 400
                self.update_impact_volume()
            self.volume_settings(mx,my,25,297,self.impact_volume)

            self.text3("GAME MODE:", 25, 391)

            if (mx > 25 and mx < 89 and my > 421 and my < 485):
                self.arrow(self.previous_hover, 25, 421)
            else:
                self.arrow(self.previous, 25, 421)
            if self.game_mode == "PVP":
                self.text3("PVP", 95, 444)
            elif self.game_mode == "PVC":
                self.text3("PVC", 95, 444)
            else:
                self.text3("CVC", 95, 444)
            if (mx > 135 and mx < 199 and my > 421 and my < 485):
                self.arrow(self.next_hover, 135, 421)
            else:
                self.arrow(self.next, 135, 421)
            self.text3("BOT DIFFICULTY:", 25, 515)
            if self.mouse_pressed==1 and mx > 100 and mx < 500 and my > 545 and my < 609:
                self.bot_range = mx - 100
            self.difficulty_settings(25,545,self.bot_range)
            if self.bot_range<100:
                self.text3("EASY", 550, 568)
            elif self.bot_range>=100 and self.bot_range<200:
                self.text3("MEDIUM", 550, 568)
            elif self.bot_range>=200 and self.bot_range<300:
                self.text3("HARD", 550, 568)
            elif self.bot_range>=300:
                self.text3("EXTREME", 550, 568)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.options2_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_running = True
                        self.menu()
                        self.options2_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mx > 368 and mx < 432 and my > 0 and my < 64:
                            self.options2_running = False
                            self.options_running = True
                            self.options()
                        if mx > 25 and mx < 89 and my > 160 and my < 244 and self.stadium_volume>0:
                            self.stadium_volume=0
                            self.update_music_volume()
                        elif mx > 25 and mx < 89 and my > 160 and my < 244 and self.stadium_volume==0:
                            self.stadium_volume=0.5
                            self.update_music_volume()
                        if mx > 100 and mx < 500 and my > 160 and my < 224:
                            self.mouse_pressed = 1
                            self.stadium_volume = (mx - 100) / 400
                            self.update_music_volume()
                        if mx > 25 and mx < 89 and my > 297 and my < 361 and self.impact_volume>0:
                            self.impact_volume=0
                            self.update_impact_volume()
                        elif mx > 25 and mx < 89 and my > 297 and my < 361 and self.impact_volume==0:
                            self.impact_volume=0.5
                            self.update_impact_volume()
                        if mx > 100 and mx < 500 and my > 297 and my < 361:
                            self.mouse_pressed = 1
                            self.impact_volume = (mx - 100) / 400
                            self.update_impact_volume()
                        if (mx > 25 and mx < 89 and my > 421 and my < 485):
                            if(self.game_mode_poz-1>=0):
                                self.game_mode_poz=self.game_mode_poz-1
                                self.game_mode=self.game_modes[self.game_mode_poz]
                        if (mx > 135 and mx < 199 and my > 421 and my < 485):
                            if (self.game_mode_poz + 1 <= len(self.game_modes)-1):
                                self.game_mode_poz = self.game_mode_poz + 1
                                self.game_mode = self.game_modes[self.game_mode_poz]
                        if mx > 100 and mx < 500 and my > 545 and my < 609:
                            self.bot_range = mx - 100
                            self.mouse_pressed = 1
                if event.type==pygame.MOUSEBUTTONUP:
                            self.mouse_pressed=0


            pygame.display.update()

    leave_game_running = False

    def leave_game(self):
        while self.leave_game_running:
            self.text("You want to go back to MENU?", 150, 100)
            mx, my = pygame.mouse.get_pos()
            if (mx > 125 and mx < 325 and my > 275 and my < 310):
                self.img_load(self.buton_YesIMG_hover, 125, 275)
            else:
                self.img_load(self.buton_YesIMG, 125, 275)
            if (mx > 425 and mx < 625 and my > 275 and my < 310):
                self.img_load(self.buton_NoIMG_hover, 425, 275)
            else:
                self.img_load(self.buton_NoIMG, 425, 275)

            self.game_pause_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                    self.leave_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (mx > 125 and mx < 325 and my > 275 and my < 310):
                            self.score_player = 0
                            self.score_player2 = 0
                            self.ball_state = 1
                            self.ballY_speed = 0
                            self.ballX_speed = 0
                            self.ballX = self.playerX + 16
                            self.ballY = self.playerY + 32
                            self.posesie = 0
                            self.menu_running = True
                            self.game_pause_time = 0
                            self.current_time = 0
                            self.goal_time = 0
                            self.start_ticks = 0
                            self.speed1 = 0.25
                            self.speed2 = 0.25
                            self.menu()
                            self.leave_game_running = False

                        elif (mx > 425 and mx < 625 and my > 275 and my < 310):
                            self.game_running = True
                            self.leave_game_running = False
                            self.start_ticks = self.start_ticks + self.game_pause_time - self.current_time
                            if (self.game_mode == "PVP"):
                                self.game()
                            elif (self.game_mode == "PVC"):
                                self.game_PVC()
                            else:
                                self.game_CVC()
            pygame.display.update()

    # PLAYER VERSUS PLAYER FUNCTION
    def game(self):
        while self.game_running:
            self.screen.fill((0, 128, 128))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.leave_game_running = True
                        self.current_time = pygame.time.get_ticks()
                        self.leave_game()
                        self.game_running = False
                    if event.key == pygame.K_LEFT:
                        self.playerX_speed = -self.speed1
                    if event.key == pygame.K_RIGHT:
                        self.playerX_speed = self.speed1
                    if event.key == pygame.K_SPACE:
                        self.player1_hit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_speed = 0
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player2X_speed = 0
                # player2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player2X_speed = -self.speed2
                    if event.key == pygame.K_d:
                        self.player2X_speed = self.speed2
                    if event.key == pygame.K_TAB:
                        self.player2_hit()
            if (self.posesie == 1 and self.ball_state == 1):
                self.ballX = self.player2X + 16
                self.ballY = self.player2Y + 48
            if (self.posesie == 0):
                if (self.ball_state == 1):
                    self.ballX = self.playerX + 16
                    self.ballY = self.playerY - 16
            self.playerX += self.playerX_speed
            self.player2X += self.player2X_speed
            seconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)
            self.chestii(seconds)
            self.alte_chestii(seconds)

            pygame.display.update()

    # PLAYER VERSUS COMPUTER FUNCTION
    def game_PVC(self):
        while self.game_running:
            self.screen.fill((0, 128, 128))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.leave_game_running = True
                        self.current_time = pygame.time.get_ticks()
                        self.leave_game()
                        self.game_running = False
                    if event.key == pygame.K_LEFT:
                        self.playerX_speed = -self.speed1
                    if event.key == pygame.K_RIGHT:
                        self.playerX_speed = self.speed1
                    if event.key == pygame.K_SPACE:
                        self.player1_hit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_speed = 0
            if (self.ballY_speed > 2):
                self.ballY_speed = 0.15
            if (self.ballY_speed < -2):
                self.ballY_speed = -0.15
            self.playerX += self.playerX_speed
            if (self.ballX > self.player2X + 16 and self.ballY-self.player2Y<self.bot_range):
                self.player2X_speed = self.speed2
            elif (self.ballX < self.player2X - 16 and self.ballY-self.player2Y<self.bot_range):
                self.player2X_speed = -self.speed2
            else:
                self.player2X_speed = 0
            self.player2_hit()
            if (self.posesie == 1 and self.ball_state == 1):
                self.ballX = self.player2X + 16
                self.ballY = self.player2Y + 48
            if (self.posesie == 0):
                if (self.ball_state == 1):
                    self.ballX = self.playerX + 16
                    self.ballY = self.playerY - 16
            self.player2X += self.player2X_speed
            seconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)
            self.chestii(seconds)
            self.alte_chestii(seconds)

            pygame.display.update()

    # Functie COMPUTER vs COMPUTER
    def game_CVC(self):
        while self.game_running:
            self.screen.fill((0, 128, 128))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.menu_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.leave_game_running = True
                        self.current_time = pygame.time.get_ticks()
                        self.leave_game()
                        self.game_running = False
            if (self.ballY_speed > 2):
                self.ballY_speed = 0.15
            if (self.ballY_speed < -2):
                self.ballY_speed = -0.15
            # player
            if (self.ball_state == 1):
                self.playerX = np.random.randint(17, 734)
            if (self.ballX > self.playerX + 16 and -self.ballY + self.playerY < 300):
                self.playerX_speed = self.speed1
            elif (self.ballX < self.playerX - 16 and -self.ballY + self.playerY < 300):
                self.playerX_speed = -self.speed1
            else:
                self.playerX_speed = 0

            if (abs(self.ballX - self.playerX) <= 32 and self.ball_state == 1):
                self.playerX_speed = -self.speed1
            if abs(self.ballX - self.playerX) <= 30 and abs(self.player2X - self.playerX) <= 30:
                self.playerX_speed = self.speed1
            self.player1_hit()
            # player2
            if (self.ball_state == 1):
                self.player2X = np.random.randint(1, 734)
                if (abs(self.player2X - self.playerX) < 15):
                    self.player2X = np.random.randint(1, 767)
            if (self.ballX > self.player2X + 16 and self.ballY - self.player2Y < 300):
                self.player2X_speed = self.speed2
            elif (self.ballX < self.player2X - 16 and self.ballY - self.player2Y < 300):
                self.player2X_speed = -self.speed2
            else:
                self.player2X_speed = 0
            if (abs(self.ballX - self.player2X) <= 32 and self.ball_state == 1):
                self.player2X_speed = self.speed2
            self.player2_hit()

            seconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)
            self.chestii(seconds)
            self.alte_chestii(seconds)

            pygame.display.update()

    def chestii(self, seconds):
        if (self.start_ticks > 0):
            if (seconds < self.game_time):
                if (int(self.game_time - seconds) > 60):
                    if (int(int(self.game_time - seconds) % 60) >= 10):
                        self.text("TIME:" + str(int(int(self.game_time - seconds) / 60)) + ":" + str(
                            int(int(self.game_time - seconds) % 60)), 600, 10)
                    if (int(int(self.game_time - seconds) % 60) < 10):
                        self.text("TIME:" + str(int(int(self.game_time - seconds) / 60)) + ":0" + str(
                            int(int(self.game_time - seconds) % 60)), 600, 10)
                elif (int(int(self.game_time - seconds) % 60) >= 10):
                    self.text("TIME:0:" + str(int(self.game_time - seconds)), 600, 10)
                elif (int(int(self.game_time - seconds) % 60) < 10 and int(self.game_time - seconds) != 60):
                    self.text("TIME:0:0" + str(int(self.game_time - seconds)), 600, 10)
                elif (int(self.game_time - seconds) == 60):
                    self.text("TIME:1:00", 600, 10)
            else:
                self.text("TIME:0:00", 600, 10)
        else:
            self.text("TIME:2:00", 600, 10)
        if int(self.game_time - seconds) >= 85 and int(self.game_time - seconds) <= 90:
            if (self.playerX > self.boost1X[0] - 60 and self.playerX < self.boost1X[0] + 30):
                self.collect1[0] = 1
                self.collect_time1[0] = pygame.time.get_ticks()
            if (self.collect1[0] == 0):
                self.img_load(self.boosts1[0], self.boost1X[0], self.playerY)
            if (self.player2X > self.boost2X[0] - 60 and self.player2X < self.boost2X[0] + 30):
                self.collect2[0] = 1
                self.collect_time2[0] = pygame.time.get_ticks()
            if (self.collect2[0] == 0):
                self.img_load(self.boosts2[0], self.boost2X[0], self.player2Y)
        if int(self.game_time - seconds) >= 55 and int(self.game_time - seconds) <= 60:
            if (self.playerX > self.boost1X[1] - 60 and self.playerX < self.boost1X[1] + 30):
                self.collect1[1] = 1
                self.collect_time1[1] = pygame.time.get_ticks()
            if (self.collect1[1] == 0):
                self.img_load(self.boosts1[1], self.boost1X[1], self.playerY)
            if (self.player2X > self.boost2X[1] - 60 and self.player2X < self.boost2X[1] + 30):
                self.collect2[1] = 1
                self.collect_time2[1] = pygame.time.get_ticks()
            if (self.collect2[1] == 0):
                self.img_load(self.boosts2[1], self.boost2X[1], self.player2Y)
        if int(self.game_time - seconds) >= 25 and int(self.game_time - seconds) <= 30:
            if (self.playerX > self.boost1X[2] - 60 and self.playerX < self.boost1X[2] + 30):
                self.collect1[2] = 1
                self.collect_time1[2] = pygame.time.get_ticks()
            if (self.collect1[2] == 0):
                self.img_load(self.boosts1[2], self.boost1X[2], self.playerY)
            if (self.player2X > self.boost2X[2] - 60 and self.player2X < self.boost2X[2] + 30):
                self.collect2[2] = 1
                self.collect_time2[2] = pygame.time.get_ticks()
            if (self.collect2[2] == 0):
                self.img_load(self.boosts2[2], self.boost2X[2], self.player2Y)

        # BOOSTS:slow and speed
        if (pygame.time.get_ticks() < self.collect_time1[0] + 5000 and self.collect_time1[0] > 0):
            if (self.boosts1[0] == self.speed):
                self.boosts1[0] = self.previous
                self.speed1 = self.speed1 + 0.1
            if (self.boosts1[0] == self.slow):
                self.boosts1[0] = self.next
                self.speed2 = self.speed2 - 0.1
            if (self.boosts1[0] == self.previous):
                self.img_load(self.speed01, self.playerX, self.playerY - 16)
            if (self.boosts1[0] == self.next):
                self.img_load(self.slow1, self.player2X + 64, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[0] + 5000 and self.collect_time1[0] > 0):
            if (self.boosts1[0] == self.previous):
                self.boosts1[0] = self.cat
                if self.boosts2[0] != self.lion:
                    self.speed1 = self.speed1 - 0.1
            if (self.boosts1[0] == self.next):
                self.boosts1[0] = self.cat
                self.speed2 = self.speed2 + 0.1
        if (pygame.time.get_ticks() < self.collect_time1[1] + 5000 and self.collect_time1[1] > 0):
            if (self.boosts1[1] == self.speed):
                self.boosts1[1] = self.previous
                self.speed1 = self.speed1 + 0.1
            if (self.boosts1[1] == self.slow):
                self.boosts1[1] = self.next
                self.speed2 = self.speed2 - 0.1
            if (self.boosts1[1] == self.previous):
                self.img_load(self.speed01, self.playerX, self.playerY - 16)
            if (self.boosts1[1] == self.next):
                self.img_load(self.slow1, self.player2X + 64, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[1] + 5000 and self.collect_time1[1] > 0):
            if (self.boosts1[1] == self.previous):
                self.boosts1[1] = self.cat
                if self.boosts2[1] != self.lion:
                    self.speed1 = self.speed1 - 0.1
            if (self.boosts1[1] == self.next):
                self.boosts1[1] = self.cat
                self.speed2 = self.speed2 + 0.1
        if (pygame.time.get_ticks() < self.collect_time1[2] + 5000 and self.collect_time1[2] > 0):
            if (self.boosts1[2] == self.speed):
                self.boosts1[2] = self.previous
                self.speed1 = self.speed1 + 0.1
            if (self.boosts1[2] == self.slow):
                self.boosts1[2] = self.next
                self.speed2 = self.speed2 - 0.1
            if (self.boosts1[2] == self.previous):
                self.img_load(self.speed01, self.playerX, self.playerY - 16)
            if (self.boosts1[2] == self.next):
                self.img_load(self.slow1, self.player2X + 64, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[2] + 5000 and self.collect_time1[2] > 0):
            if (self.boosts1[2] == self.previous):
                self.boosts1[2] = self.cat
                if self.boosts2[2] != self.lion:
                    self.speed1 = self.speed1 - 0.1
            if (self.boosts1[2] == self.next):
                self.boosts1[2] = self.cat
                self.speed2 = self.speed2 + 0.1
        if (pygame.time.get_ticks() < self.collect_time2[0] + 5000 and self.collect_time2[0] > 0):
            if (self.boosts2[0] == self.speed):
                self.boosts2[0] = self.previous
                self.speed2 = self.speed2 + 0.1
            if (self.boosts2[0] == self.slow):
                self.boosts2[0] = self.next
                self.speed1 = self.speed1 - 0.1
            if (self.boosts2[0] == self.previous):
                self.img_load(self.speed01, self.player2X, self.player2Y + 64)
            if (self.boosts2[0] == self.next):
                self.img_load(self.slow1, self.playerX + 64, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[0] + 5000 and self.collect_time2[0] > 0):
            if (self.boosts2[0] == self.previous):
                self.boosts2[0] = self.cat
                if self.boosts1[0] != self.lion:
                    self.speed2 = self.speed2 - 0.1
            if (self.boosts2[0] == self.next):
                self.boosts2[0] = self.cat
                self.speed1 = self.speed1 + 0.1
        if (pygame.time.get_ticks() < self.collect_time2[1] + 5000 and self.collect_time2[1] > 0):
            if (self.boosts2[1] == self.speed):
                self.boosts2[1] = self.previous
                self.speed2 = self.speed2 + 0.1
            if (self.boosts2[1] == self.slow):
                self.boosts2[1] = self.next
                self.speed1 = self.speed1 - 0.1
            if (self.boosts2[1] == self.previous):
                self.img_load(self.speed01, self.player2X, self.player2Y + 64)
            if (self.boosts2[1] == self.next):
                self.img_load(self.slow1, self.playerX + 64, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[1] + 5000 and self.collect_time2[1] > 0):
            if (self.boosts2[1] == self.previous):
                self.boosts2[1] = self.cat
                if self.boosts1[1] != self.lion:
                    self.speed2 = self.speed2 - 0.1
            if (self.boosts2[1] == self.next):
                self.boosts2[1] = self.cat
                self.speed1 = self.speed1 + 0.1
        if (pygame.time.get_ticks() < self.collect_time2[2] + 5000 and self.collect_time2[2] > 0):
            if (self.boosts2[2] == self.speed):
                self.boosts2[2] = self.previous
                self.speed2 = self.speed2 + 0.1
            if (self.boosts2[2] == self.slow):
                self.boosts2[2] = self.next
                self.speed1 = self.speed1 - 0.1
            if (self.boosts2[2] == self.previous):
                self.img_load(self.speed01, self.player2X, self.player2Y + 64)
            if (self.boosts2[2] == self.next):
                self.img_load(self.slow1, self.playerX + 64, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[2] + 5000 and self.collect_time2[2] > 0):
            if (self.boosts2[2] == self.previous):
                self.boosts2[2] = self.cat
                if self.boosts1[2] != self.lion:
                    self.speed2 = self.speed2 - 0.1
            if (self.boosts2[2] == self.next):
                self.boosts2[2] = self.cat
                self.speed1 = self.speed1 + 0.1

        # BOOSTS: freeze
        if (pygame.time.get_ticks() < self.collect_time1[0] + 1500 and self.collect_time1[0] > 0):
            if (self.boosts1[0] == self.freeze):
                self.boosts1[0] = self.lion
                self.speed2 = 0
            if (self.boosts1[0] == self.lion):
                self.img_load(self.freeze1, self.player2X + 32, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[0] + 1500 and self.collect_time1[0] > 0):
            if (self.boosts1[0] == self.lion):
                self.boosts1[0] = self.cat
                self.speed2 = self.speed2 + 0.25
        if (pygame.time.get_ticks() < self.collect_time1[1] + 1500 and self.collect_time1[1] > 0):
            if (self.boosts1[1] == self.freeze):
                self.boosts1[1] = self.lion
                self.speed2 = 0
            if (self.boosts1[1] == self.lion):
                self.img_load(self.freeze1, self.player2X + 32, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[1] + 1500 and self.collect_time1[1] > 0):
            if (self.boosts1[1] == self.lion):
                self.boosts1[1] = self.cat
                self.speed2 = self.speed2 + 0.25
        if (pygame.time.get_ticks() < self.collect_time1[2] + 1500 and self.collect_time1[2] > 0):
            if (self.boosts1[2] == self.freeze):
                self.boosts1[2] = self.lion
                self.speed2 = 0
            if (self.boosts1[2] == self.lion):
                self.img_load(self.freeze1, self.player2X + 32, self.player2Y + 64)
        elif (pygame.time.get_ticks() > self.collect_time1[2] + 1500 and self.collect_time1[2] > 0):
            if (self.boosts1[2] == self.lion):
                self.boosts1[2] = self.cat
                self.speed2 = self.speed2 + 0.25
        if (pygame.time.get_ticks() < self.collect_time2[0] + 1500 and self.collect_time2[0] > 0):
            if (self.boosts2[0] == self.freeze):
                self.boosts2[0] = self.lion
                self.speed1 = 0
            if (self.boosts2[0] == self.lion):
                self.img_load(self.freeze1, self.playerX + 32, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[0] + 1500 and self.collect_time2[0] > 0):
            if (self.boosts2[0] == self.lion):
                self.boosts2[0] = self.cat
                self.speed1 = self.speed1 + 0.25
        if (pygame.time.get_ticks() < self.collect_time2[1] + 1500 and self.collect_time2[1] > 0):
            if (self.boosts2[1] == self.freeze):
                self.boosts2[1] = self.lion
                self.speed1 = 0
            if (self.boosts2[1] == self.lion):
                self.img_load(self.freeze1, self.playerX + 32, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[1] + 1500 and self.collect_time2[1] > 0):
            if (self.boosts2[1] == self.lion):
                self.boosts2[1] = self.cat
                self.speed1 = self.speed1 + 0.25
        if (pygame.time.get_ticks() < self.collect_time2[2] + 1500 and self.collect_time2[2] > 0):
            if (self.boosts2[2] == self.freeze):
                self.boosts2[2] = self.lion
                self.speed1 = 0
            if (self.boosts2[2] == self.lion):
                self.img_load(self.freeze1, self.playerX + 32, self.playerY - 16)
        elif (pygame.time.get_ticks() > self.collect_time2[2] + 1500 and self.collect_time2[2] > 0):
            if (self.boosts2[2] == self.lion):
                self.boosts2[2] = self.cat
                self.speed1 = self.speed1 + 0.25

    def alte_chestii(self, seconds):
        self.player2X += self.player2X_speed
        self.playerX += self.playerX_speed
        if self.playerX <= 16:
            self.playerX = 16
        elif self.playerX > 736:
            self.playerX = 736
        if self.player2X <= 16:
            self.player2X = 16
        elif self.player2X > 736:
            self.player2X = 736
        self.player()
        self.player2()
        self.ball()
        self.bari()
        self.text(
            self.playerName + "  " + str(self.score_player) + " - " + str(self.score_player2) + "  " + self.player2Name,
            self.textX, self.textY)
        if self.ball_state == 0:
            self.ball()
            self.ballY += self.ballY_speed
            self.ballX += self.ballX_speed
        if (self.ballY < 0 or self.ballY > 555):
            self.ballX_speed = 0
        if self.ballY < 0:
            if self.ball_state != 2:
                self.goal_time = pygame.time.get_ticks()
            self.ball_state = 2
            self.posesie = 1
            if (pygame.time.get_ticks() - self.goal_time > 1000):
                self.score_player = self.score_player + 1
                self.ball_state = 1
                self.ballY = self.player2Y + 32
                self.ballX = self.player2X + 16
        if self.ballY > 555:
            if self.ball_state != 2:
                self.goal_time = pygame.time.get_ticks()
            self.ball_state = 2
            self.posesie = 0
            if (pygame.time.get_ticks() - self.goal_time > 1000):
                self.ball_state = 1
                self.score_player2 = self.score_player2 + 1
                self.ballY = self.playerY + 32
                self.ballX = self.playerX + 16
        if self.ballX <= 0:
            self.ballX = 0
        if self.ballX >= 768:
            self.ballX = 768
        if (self.ballX <= 0 or self.ballX >= 768):
            self.impact.play()
            self.ballX_speed = -self.ballX_speed
        if (self.ballX > 0 and self.ballX < 198) and self.ballY < 94:
            self.impact.play()
            self.ballY = 94
            self.ballY_speed = -self.ballY_speed
        elif self.ballX > 198 and self.ballX < 201 and self.ballY < 94:
            self.impact.play()
            self.ballX_speed = -self.ballX_speed
        if (self.ballX > 0 and self.ballX < 198) and self.ballY > 513:
            self.impact.play()
            self.ballY = 513
            self.ballY_speed = -self.ballY_speed
        elif self.ballX > 198 and self.ballX < 201 and self.ballY > 513:
            self.impact.play()
            self.ballX_speed = -self.ballX_speed
        if (self.ballX > 565 and self.ballX < 768) and self.ballY < 94:
            self.impact.play()
            self.ballY = 94
            self.ballY_speed = -self.ballY_speed
        elif self.ballX < 565 and self.ballX > 563 and self.ballY < 94:
            self.impact.play()
            self.ballX_speed = -self.ballX_speed
        if (self.ballX > 565 and self.ballX < 768) and self.ballY > 513:
            self.impact.play()
            self.ballY = 513
            self.ballY_speed = -self.ballY_speed
        elif self.ballX < 565 and self.ballX > 563 and self.ballY > 513:
            self.impact.play()
            self.ballX_speed = -self.ballX_speed
        if (self.posesie == 0 and self.ball_state == 2):
            self.text("GOAL " + self.player2Name, self.goal_textX, self.goal_textY)
        if (self.posesie == 1 and self.ball_state == 2):
            self.text("GOAL " + self.playerName, self.goal_textX, self.goal_textY)
        if (seconds > self.game_time and self.score_player > self.score_player2):
            self.text(self.playerName + " WINS!", self.goal_textX, self.goal_textY)
            self.goal_time = 0
            self.ballX_speed = 0
            self.ballY_speed = 0
            self.playerX_speed = 0
            self.player2X_speed = 0
            if (seconds - self.game_time > 5):
                self.posesie = 0
                self.ball_state = 1
                self.score_player2 = 0
                self.score_player = 0
        if (seconds > self.game_time and self.score_player2 > self.score_player):
            self.text(self.player2Name + " WINS!", self.goal_textX, self.goal_textY)
            self.goal_time = 0
            self.ballX_speed = 0
            self.ballY_speed = 0
            self.playerX_speed = 0
            self.player2X_speed = 0
            if (seconds - self.game_time > 5):
                self.posesie = 0
                self.ball_state = 1
                self.score_player2 = 0
                self.score_player = 0
        if (seconds > self.game_time and self.score_player == self.score_player2 and seconds - self.game_time <= 5):
            self.text("DRAW", self.goal_textX + 20, self.goal_textY)
            self.goal_time = 0
            self.ballX_speed = 0
            self.ballY_speed = 0
            self.playerX_speed = 0
            self.player2X_speed = 0
        elif (seconds - self.game_time > 5):
            self.posesie = 0
            self.ball_state = 1
            self.score_player2 = 0
            self.score_player = 0
        if (
                self.posesie == 0 and self.ball_state == 1 and pygame.time.get_ticks() > self.goal_time + 4000 and self.goal_time > 0 and self.start_ticks > 0):
            self.ballY_speed = -0.15
            self.ball_state = 0
        if (
                self.posesie == 1 and self.ball_state == 1 and pygame.time.get_ticks() > self.goal_time + 4000 and self.goal_time > 0 and self.start_ticks > 0):
            self.ballY_speed = 0.15
            self.ball_state = 0

    def selectie_random(self):
        if self.score_player == 0 and self.score_player2 == 0:
            self.start_ticks = pygame.time.get_ticks()
            for i in range(3):
                self.boost1X[i] = np.random.randint(17, 736)
                self.boost2X[i] = np.random.randint(17, 736)
                self.boosts1[i] = self.boosts[np.random.randint(3)]
                self.boosts2[i] = self.boosts[np.random.randint(3)]
                self.collect1[i] = 0
                self.collect2[i] = 0
                self.collect_time1[i] = 0
                self.collect2[i] = 0

    def player1_hit(self):
        if (self.ball_state == 0 and self.ballY > self.playerY-32 and self.ballY < self.playerY + 64):
            if (self.ballX > self.playerX - 31 and self.ballX < (self.playerX + 95)):
                self.impact.play()
                old_speed = abs(self.ballX_speed) + abs(self.ballY_speed)
                self.ballX_speed = 0.0075 * (self.ballX - self.playerX - 16)
                self.ballY_speed = -0.15
                if abs(self.ballX_speed) + abs(self.ballY_speed) < old_speed:
                    self.ballY_speed = -old_speed
        if (self.posesie == 0):
            if (self.ball_state == 1):
                self.ballX = self.playerX + 16
                self.ballY = self.playerY - 16
                self.ball_state = 0
                self.ballY_speed = -0.15
                self.selectie_random()

    def player2_hit(self):
        if (self.ballY > self.player2Y and self.ballY < self.player2Y + 64 and self.ball_state == 0):
            if (self.ballX > self.player2X - 31 and self.ballX < self.player2X + 95):
                self.impact.play()
                old_speed = abs(self.ballX_speed) + abs(self.ballY_speed)
                self.ballX_speed = 0.0075 * (self.ballX - self.player2X - 16)
                self.ballY_speed = 0.15
                if abs(self.ballX_speed) + abs(self.ballY_speed) < old_speed:
                    self.ballY_speed = old_speed
        if (self.posesie == 1 and self.ball_state == 1):
            self.ballX = self.player2X + 16
            self.ballY = self.player2Y + 16
            self.ball_state = 0
            self.ballY_speed = 0.3

    def volume_settings(self,mx,my,x,y,volume):
        if (volume > 0 and volume < 0.75):
            if mx > x and mx < x+64 and my > y and my < y+64:
                self.img_load(self.volume_hover, x,y)
            else:
                self.img_load(self.volume, x,y)

        if (volume == 0):
            if mx > x and mx < x+64 and my > y and my < y+64:
                self.img_load(self.mute_hover, x, y)
            else:
                self.img_load(self.mute, x, y)
        if (volume > 0.75):
            if mx > x and mx < x+64 and my > y and my < y+64:
                self.img_load(self.high_volume_hover, x, y)
            else:
                self.img_load(self.high_volume, x, y)
        self.img_load(self.volume_bar, x+75, y+31)
        self.img_load(self.dot, 100 + volume * 400, y)

    def difficulty_settings(self,x,y,range):
        self.img_load(self.bot,x,y)
        self.img_load(self.volume_bar, x+75, y+31)
        self.img_load(self.dot, 100 + range, y)

Game = game()
Game.menu()
