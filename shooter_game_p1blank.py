#Create your own shooter

from xxxxxxx import *

#background music
xxxxxx.init()
xxxxxx.music.load('fire.ogg')
xxxxxxx.music.play()
fire_sound = xxxxxxxx.Sound('fire.ogg')


#we need the following images:
img_back = "xxxxxxx.xxx" #game background
img_hero = "rocket.png" #hero


#parent class for other sprites
class GameSprite(sprite.Sprite):
 #class constructor
   def XXXXXXXXXX(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)


       #every sprite must store the image property
       self.XXXXXXX = transform.scale(image.load(player_image), (size_x, size_y))
       self.XXXXX = player_speed


       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = XXXXXXXX
       self.rect.y = XXXXXXXX

 #method drawing the character on the window
   def reset(self):
       window.XXXXXXXXX(self.image, (self.rect.x, self.rect.y))


#main player class
class Player(XXXXXXXXX):
   #method to control the sprite with arrow keys
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= XXXXXXXX
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           XXXXXX += self.speed
 #method to "shoot" (use the player position to create a bullet there)
   def fire(self):
       pass


#create a window
win_width = 700
win_height = 500
display.set_caption("XXXXXXXX")
window = display.XXXXXXXX((win_width, win_height))
background = transform.XXXXXX(image.load(XXXXXXXX), (win_width, win_height))


#create sprites
ship = Player(XXXXXXXX, 5, win_height - 100, 80, 100, 10)


#the "game is over" variable: as soon as True is there, sprites stop working in the main loop
finish = False
#Main game loop:
run = True #the flag is reset by the window close button
while run:
   #"Close" button press event
   for e in event.get():
       if e.type == QUIT:
           run = XXXXX


   if not finish:
       #update the background
       window.XXXXX(background,(0,0))


       #launch sprite movements
       ship.XXXXXX()


       #update them in a new location in each loop iteration
       XXXXXXX.reset()


       display.update()
   #the loop is executed each 0.05 sec
   time.delay(50)
