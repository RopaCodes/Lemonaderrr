import pygame, os, sys, time
#import classes
from entities import ExtrasContainer,Grass, Sugar, FruitContainer, BasicLemMenu, DoneBtn
from entities import SpriteSheet, IceBucket, LemonadeStand, WaterJug, MoneySystem
# pygame setup
#find and replace = ctrl + shift + F
clock = pygame.time.Clock()
timer_font = pygame.font.Font("assets/grow_year_regular.ttf", 70)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Lemonaderrr')
        self.screen_width = 960
        self.screen_height = 650
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock =  pygame.time.Clock()
        pygame.display.set_caption('Lemonaderrr')
        self.state = "start"
        self.game_over = False
        pygame.mixer.music.load("assets/soundFx/gameplay_music.wav") #automatically plays the music
        pygame.mixer.music.play(-1) #ensures the bg music loops

        # Timer variables
        self.timer_font = pygame.font.Font("assets/grow_year_regular.ttf", 70)
        self.timer_sec = 60
        self.timer_text = timer_font.render("01:00",True,(34, 36, 49))
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000) # Trigger event every 1000ms

        self.drink_progress = 0
        self.frame_num = 0
        self.lemon_held = False
        self.clicked = False
        
        
        #OBJECT CREATION
        self.basic_lem_menu = BasicLemMenu(self.display, self.screen_width, self.screen_height)
        self.money_status = MoneySystem(self.display,self.screen_width,self.screen_height,0) 
        
        self.grass = Grass(self.display, self.screen_width, self.screen_height)
        self.lemonade_stand = LemonadeStand(self.display, self.screen_width, self.screen_height)
        self.extras_container = ExtrasContainer(self.display, self.screen_width, self.screen_height)
        self.fruit_container = FruitContainer(self.display, self.screen_width, self.screen_height,self.lemon_held,self.basic_lem_menu,self.clicked,self.money_status,self)
        self.ice_bucket = IceBucket(self.display, self.screen_width, self.screen_height,self.basic_lem_menu,self.money_status,self)
        self.sugar_bag = Sugar(self.display, self.screen_width, self.screen_height,self.basic_lem_menu,self.money_status,self)
        self.water_jug = WaterJug(self.display, self.screen_width, self.screen_height,self.basic_lem_menu,self.money_status,self)
        self.done_btn = DoneBtn(self.display, self.screen_width, self.screen_height,self.basic_lem_menu,self)
        

        #SPRITE SHEET
        self.glass_rect = pygame.Rect(0,0,0,0)
        self.sprite_sheet_basic_lem = pygame.image.load("assets/sprite_sheet_basic_lemonade.png")
        self.sprite_sheet_basic = SpriteSheet(self.sprite_sheet_basic_lem)
        self.frame0 = self.sprite_sheet_basic.get_img(self.frame_num,256,256,1)
        self.scaled_drink = pygame.transform.scale(self.frame0,(110,110))

        #start & game over screens
        self.start_screen_img = pygame.image.load('assets/start_screen.PNG')
        self.gameOver_screen_img = pygame.image.load('assets/game_over_screen.PNG')
    
    def check_recipie_complete(self):
        if(
            self.water_jug.correct_amm and
            self.ice_bucket.correct_amm and
            self.sugar_bag.correct_amm
        ):
            self.money_status.money_earned += 5
            

    def run(self):
        while True:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    # Handles keyboard events
                    if event.key == pygame.K_ESCAPE:
                        # Quits the loop if the Escape key is pressed
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        if self.state == "start":
                            
                            self.state = "playing"
                        elif self.state == "gameover":
                            #pygame.mixer.music.stop() 
                            self.reset_game()
                            self.state = "playing"
                    
                elif event.type == self.timer_event:
                    if self.timer_sec > 0:
                        self.timer_sec -= 1
                        mins = self.timer_sec // 60
                        secs = self.timer_sec % 60
                        self.timer_text = self.timer_font.render("%02d:%02d" % (mins,secs), True,(34, 36, 49))
                    else:
                        pygame.time.set_timer(self.timer_event,0)
                        self.state = "gameover"


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "playing":
                        mouse_pos = event.pos
                        if self.fruit_container.lemon_held:
                            if self.glass_rect.collidepoint(mouse_pos):
                                self.fruit_container.lemon_held = False
                                # add squeeze logic here
                            else:
                                self.fruit_container.lemon_held = False  # drop it anywhere = cancel
                        else:
                            self.water_jug.check_collision()
                            self.sugar_bag.check_collision()
                            self.ice_bucket.check_collision()
                            self.done_btn.check_collision()
                            self.fruit_container.check_collision()
                            self.check_recipie_complete()


            #update display
            self.update_display()
    
    def draw_elements(self):
        self.display.fill((237, 218, 239))
        
        if self.state == "start":
            self.draw_start_screen()
        elif self.state == "playing":
            self.draw_game()
        elif self.state == "gameover":
            self.draw_gameover_screen()
    
    def draw_start_screen(self):
        self.display.blit(self.start_screen_img,(0,0))
        
        

    def draw_gameover_screen(self):
        self.display.blit(self.gameOver_screen_img,(0,0))

    def draw_game(self):
        #timer
        self.display.blit(self.timer_text,((self.screen_width/2),10))
        #ENTITIES
        self.money_status.draw_text()
        self.grass.draw_img()
        self.lemonade_stand.draw_img()
        self.extras_container.draw_img()
        self.fruit_container.draw_img()
        self.ice_bucket.draw_img()
        self.sugar_bag.draw_img()
        self.water_jug.draw_img()   
        
        #self.display.blit(self.scaled_drink,(540,(self.screen_height-354)))
        current_frame = self.drink_progress
        frame_img = self.sprite_sheet_basic.get_img(current_frame, 256, 256, 1)
        scaled = pygame.transform.scale(frame_img, (110,110))
        glass_x, glass_y = 540, (self.screen_height-354)
        self.display.blit(scaled,(glass_x,glass_y))
        self.glass_rect = pygame.Rect(glass_x, glass_y, 110, 110)
        
    ##MENU STUFF
        #basic_lem_menu = BasicLemMenu(self.display,self.screen_width,self.screen_height)
        self.basic_lem_menu.draw_img()
        if self.basic_lem_menu.doing_order == False:
            self.basic_lem_menu.draw_recipie()
            #basic_lem_menu = True
        self.done_btn.draw_img()

    #lemon fruit
        if self.fruit_container.lemon_held:
            mouse_pos = pygame.mouse.get_pos()
            self.display.blit(self.fruit_container.lemon,(mouse_pos[0],mouse_pos[1]))

    def reset_game(self):
        self.timer_sec = 60
        self.timer_text = self.timer_font.render("01:00", True, (34, 36, 49))
        pygame.time.set_timer(self.timer_event, 1000)
        self.drink_progress = 0
        self.money_status.money_earned = 0
        self.basic_lem_menu.generate_new_order()
        self.ice_bucket.num_clicked = 0
        self.ice_bucket.correct_amm = False
        self.sugar_bag.num_clicked = 0
        self.sugar_bag.correct_amm = False
        self.water_jug.num_clicked = 0
        self.water_jug.correct_amm = False
        self.fruit_container.lemon_held = False
    
    #-------update display
    def update_display(self):
        self.draw_elements()
        pygame.display.update()
        self.clock.tick(60)
            
Game().run()

