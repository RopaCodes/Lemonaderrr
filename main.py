import pygame, os, sys, time
#import classes
from entities import ExtrasContainer,Grass, Sugar, FruitContainer, IceBucket, LemonadeStand, WaterJug, BasicLemonade
# pygame setup
#find and replace = ctrl + shift + F
clock = pygame.time.Clock()
#functions

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Lemonaderrr')
        self.screen_width = 960
        self.screen_height = 650
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock =  pygame.time.Clock()
        pygame.display.set_caption('Lemonaderrr')

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

            #update display
            self.update_display()
    
    def draw_elements(self):
        self.display.fill((237, 218, 239))

        #ENTITIES
        grass = Grass(self.display,self.screen_width,self.screen_height)
        grass.draw_img()

        lemonade_stand = LemonadeStand(self.display,self.screen_width,self.screen_height)
        lemonade_stand.draw_img()

        extras_container = ExtrasContainer(self.display,self.screen_width,self.screen_height)
        extras_container.draw_img()

        fruit_container = FruitContainer(self.display,self.screen_width,self.screen_height)
        fruit_container.draw_img()

        ice_bucket = IceBucket(self.display,self.screen_width,self.screen_height)
        ice_bucket.draw_img()

        sugar_bag = Sugar(self.display,self.screen_width,self.screen_height)
        sugar_bag.draw_img()

        water_jug = WaterJug(self.display,self.screen_width,self.screen_height)
        water_jug.draw_img()

        basic_lemonade = BasicLemonade(self.display,self.screen_width,self.screen_height)
        basic_lemonade.draw_img()
        #basic_lem0 = basic_lemonade.get_img()

    #-------update display
    def update_display(self):
        self.draw_elements()
        pygame.display.update()
        self.clock.tick(60)
            
Game().run()