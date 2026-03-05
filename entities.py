import pygame, random
#from recipies import generate_basic_lem_rec
pygame.init()
#font
font_path = "assets/grow_year_regular.ttf"
menu_title_font = pygame.font.Font(font_path, 30)
menu_numbers_font = pygame.font.Font(font_path, 24)
grey_txt_color= (34, 36, 49)
#functions



#classes
class MoneySystem:
    def __init__(self,display,display_w,display_h,money_earned):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.x_pos = self.display_w-150
        self.y_pos = 20
        self.money_earned = money_earned
    def draw_text(self):
        money_surf = menu_title_font.render("$"+str(self.money_earned),True,grey_txt_color)
        self.display.blit(money_surf,((self.x_pos,self.y_pos)))
class LemonadeStand:
    def __init__(self,display,display_w,display_h):
        self.display = display
        self.x_pos = 0
        self.y_pos = 0
        self.display_w = display_w
        self.display_h = display_h
        self.width = 600
        self.height = 600
        self.img_load = pygame.image.load('assets/lemonadeStand.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,((self.display_w-675),(self.display_h-600)))
        
class Grass:
    def __init__(self,display,display_w,display_h):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h-300
        self.width = display_w
        self.height = 660
        self.x_pos = display_w-self.width
        self.y_pos = self.display_h-355
        self.img_load = pygame.image.load('assets/grass.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class ExtrasContainer:
    def __init__(self, display,display_w,display_h):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.x_pos = 15
        self.y_pos = self.display_h-260
        self.width = 340
        self.height = 340
        self.img_load = pygame.image.load('assets/extras_cont.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()

    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class FruitContainer:
    def __init__(self,display,display_w,display_h):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.width = 340
        self.height = 340
        self.x_pos = display_w-self.width
        self.y_pos = self.display_h-270
        self.img_load = pygame.image.load('assets/fruit_cont.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class IceBucket:
    def __init__(self, display, display_w, display_h, menu, money_earned, game):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.game = game
        self.x_pos = 250
        self.y_pos = self.display_h - 200
        self.width = 190
        self.height = 190
        self.img_load = pygame.image.load('assets/ice_bucket.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load, (self.width, self.height))
        self.img_rect = self.img.get_rect(topleft=(self.x_pos, self.y_pos))
        self.menu = menu
        self.num_clicked = 0
        self.correct_amm = False
        self.clicked = False
        self.money_system = money_earned

    def draw_img(self):
        self.display.blit(self.img, (self.x_pos, self.y_pos))

    def check_collision(self):

        mouse_pos = pygame.mouse.get_pos()

        if self.img_rect.collidepoint(mouse_pos):
            self.num_clicked += 1
            #print("IceBucket click:", self.num_clicked)  # change label per class

            if self.num_clicked == 1:
                self.game.drink_progress += 1

            if self.num_clicked <= self.menu.basic_lem_ice:  # change to matching var per class
                self.money_system.money_earned += 1
            else:
                self.money_system.money_earned -= 1

            self.correct_amm = (self.num_clicked == self.menu.basic_lem_ice)  # change per class


class Sugar:
    def __init__(self, display, display_w, display_h, menu, money_earned, game):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.game = game
        self.x_pos = 650
        self.y_pos = self.display_h - 370
        self.width = 130
        self.height = 130
        self.img_load = pygame.image.load('assets/sugar.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load, (self.width, self.height))
        self.img_rect = self.img.get_rect(topleft=(self.x_pos, self.y_pos))
        self.menu = menu
        self.num_clicked = 0
        self.correct_amm = False
        self.clicked = False
        self.money_system = money_earned

    def draw_img(self):
        self.display.blit(self.img, (self.x_pos, self.y_pos))

    def check_collision(self):
    
        mouse_pos = pygame.mouse.get_pos()

        if self.img_rect.collidepoint(mouse_pos):
            self.num_clicked += 1
            #print("IceBucket click:", self.num_clicked)  # change label per class

            if self.num_clicked == 1:
                self.game.drink_progress += 1

            if self.num_clicked <= self.menu.basic_lem_ice:  # change to matching var per class
                self.money_system.money_earned += 1
            else:
                self.money_system.money_earned -= 1

            self.correct_amm = (self.num_clicked == self.menu.basic_lem_ice)  # change per class


class WaterJug:
    def __init__(self, display, display_w, display_h, menu, money_earned, game):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.game = game
        self.x_pos = 340
        self.y_pos = self.display_h - 451
        self.width = 240
        self.height = 240
        self.img_load = pygame.image.load('assets/water_jug.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load, (self.width, self.height))
        self.img_rect = self.img.get_rect(topleft=(self.x_pos, self.y_pos))
        self.menu = menu
        self.num_clicked = 0
        self.correct_amm = False
        self.clicked = False
        self.money_system = money_earned

    def draw_img(self):
        self.display.blit(self.img, (self.x_pos, self.y_pos))

    def check_collision(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.img_rect.collidepoint(mouse_pos):
            self.num_clicked += 1
            #print("IceBucket click:", self.num_clicked)  # change label per class

            if self.num_clicked == 1:
                self.game.drink_progress += 1

            if self.num_clicked <= self.menu.basic_lem_ice:  # change to matching var per class
                self.money_system.money_earned += 1
            else:
                self.money_system.money_earned -= 1

            self.correct_amm = (self.num_clicked == self.menu.basic_lem_ice)  # change per class

class SpriteSheet:
    def __init__(self,img):
        self.sheet_img = img
        
    def get_img(self,frame,width,height,scale):
        #SRCALPHA removes the black on the sprite
        img = pygame.Surface((width,height),pygame.SRCALPHA)
        img.blit(self.sheet_img,(0,0),((frame*width),0,width,height))
        img = pygame.transform.scale(img,(width*scale,height*scale)).convert_alpha()
        
        return img
    
##MENU MECHANIC
class BasicLemMenu:
    def __init__(self,display,display_w,display_h):
        self.display_w = display_w
        self.display_h = display_h
        self.display = display
        self.x_pos = 130
        self.y_pos = self.display_h-690
        self.width = 570
        self.height = 570

        self.img_load = pygame.image.load('assets/basic_lemonade_recipie.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        self.doing_order = False
        

        self.generate_new_order()

    def draw_img(self):
        self.display.blit(self.img,(self.x_pos-250,self.y_pos))

    def generate_new_order(self):
        self.basic_lem_water = 1
        self.basic_lem_ice = random.randint(2, 6)
        self.basic_lem_sugar = random.randint(2, 5)
        self.basic_lem_squeezes = random.randint(2, 6)
        #return self.basic_lem_ice, self.basic_lem_squeezes, self.

    def draw_recipie(self):
        drink_name_surf = menu_title_font.render("Basic Lemonade",True,grey_txt_color)
        self.display.blit(drink_name_surf,((90,225)))

        water_surf = menu_numbers_font.render(str(self.basic_lem_water),True,grey_txt_color)
        self.display.blit(water_surf,((130,290)))

        ice_surf = menu_numbers_font.render(str(self.basic_lem_ice),True,grey_txt_color)
        self.display.blit(ice_surf,((130+90,290)))

        sugar_surf = menu_numbers_font.render(str(self.basic_lem_sugar),True,grey_txt_color)
        self.display.blit(sugar_surf,((130+180,290)))

        squeezes_surf = menu_numbers_font.render(str(self.basic_lem_squeezes),True,grey_txt_color)
        self.display.blit(squeezes_surf,((130,345)))
        

            

        

    

