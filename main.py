import pygame, os, sys, time
#import classes
from entities import ExtrasContainer,Grass, Sugar, FruitContainer, BasicLemMenu
from entities import SpriteSheet, IceBucket, LemonadeStand, WaterJug, MoneySystem
# pygame setup
#find and replace = ctrl + shift + F
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Lemonaderrr')
        self.screen_width = 960
        self.screen_height = 650
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock =  pygame.time.Clock()
        pygame.display.set_caption('Lemonaderrr')

        self.frame_num = 0

        #OBJECT CREATION
        self.basic_lem_menu = BasicLemMenu(self.display, self.screen_width, self.screen_height)
        self.basic_lem_menu = BasicLemMenu(self.display, self.screen_width, self.screen_height)
        self.money_status = MoneySystem(self.display,self.screen_width,self.screen_height,0) 
        
        self.grass = Grass(self.display, self.screen_width, self.screen_height)
        self.lemonade_stand = LemonadeStand(self.display, self.screen_width, self.screen_height)
        self.extras_container = ExtrasContainer(self.display, self.screen_width, self.screen_height)
        self.fruit_container = FruitContainer(self.display, self.screen_width, self.screen_height)
        self.ice_bucket = IceBucket(self.display, self.screen_width, self.screen_height)
        self.sugar_bag = Sugar(self.display, self.screen_width, self.screen_height)
        self.water_jug = WaterJug(self.display, self.screen_width, self.screen_height,self.basic_lem_menu,self.frame_num,self.money_status)
        

        #SPRITE SHEET
        self.sprite_sheet_basic_lem = pygame.image.load("assets/sprite_sheet_basic_lemonade.png")
        self.sprite_sheet_basic = SpriteSheet(self.sprite_sheet_basic_lem)
        self.frame0 = self.sprite_sheet_basic.get_img(self.frame_num,256,256,1)
        self.scaled_drink = pygame.transform.scale(self.frame0,(110,110))

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

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.water_jug.check_collision()

            #update display
            self.update_display()
    
    def draw_elements(self):
        self.display.fill((237, 218, 239))

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
        current_frame = self.water_jug.frame_number
        frame_img = self.sprite_sheet_basic.get_img(current_frame, 256, 256, 1)
        scaled = pygame.transform.scale(frame_img, (110,110))
        self.display.blit(scaled,(540,(self.screen_height-354)))
        
    ##MENU STUFF
        #basic_lem_menu = BasicLemMenu(self.display,self.screen_width,self.screen_height)
        self.basic_lem_menu.draw_img()
        if self.basic_lem_menu.doing_order == False:
            self.basic_lem_menu.draw_recipie()
            #basic_lem_menu = True

    #-------update display
    def update_display(self):
        self.draw_elements()
        pygame.display.update()
        self.clock.tick(60)
            
Game().run()
