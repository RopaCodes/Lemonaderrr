import pygame
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
        self.display.blit(self.img,((self.display_w-775),(self.display_h-600)))
        
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
    def __init__(self,display,display_w,display_h):
        self.display = display
        self.display_w = display_w
        self.display_h = display_h
        self.x_pos = 250
        self.y_pos = self.display_h-200
        self.width = 190
        self.height = 190
        self.img_load = pygame.image.load('assets/ice_bucket.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class Sugar:
    def __init__(self,display,display_w,display_h):
        self.display_w = display_w
        self.display_h = display_h
        self.display = display
        self.x_pos = 540
        self.y_pos = self.display_h-370
        self.width = 130
        self.height = 130
        self.img_load = pygame.image.load('assets/sugar.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height))
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class WaterJug:
    def __init__(self,display,display_w,display_h):
        self.display_w = display_w
        self.display_h = display_h
        self.display = display
        self.x_pos = 230
        self.y_pos = self.display_h-451
        self.width = 240
        self.height = 240
        self.img_load = pygame.image.load('assets/water_jug.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_load,(self.width,self.height)).convert_alpha()
        #self.img.convert_alpha()
    def draw_img(self):
        self.display.blit(self.img,(self.x_pos,self.y_pos))

class SpriteSheet:
    def __init__(self,img):
        self.sheet_img = img
    def get_img(self,frame,width,height,scale):
        #SRCALPHA removes the black on the sprite
        img = pygame.Surface((width,height),pygame.SRCALPHA)
        img.blit(self.sheet_img,(0,0),((frame*width),0,width,height))
        img = pygame.transform.scale(img,(width*scale,height*scale)).convert_alpha()
        
        return img

