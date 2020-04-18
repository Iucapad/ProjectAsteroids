import pygame
import random

class Player:

    def __init__(self,sprite,x,y):
        self.sprite=sprite
        self.x=x
        self.y=y
        self.size=50
        self.angle=90

    def Key(self,key):
        if (key==pygame.K_RIGHT):
            print('right')

    def Shoot(self):
        pass

    def Teleport(self):
        if (True) :
            #TP()
            pass
        else :
            Teleport()

    def Draw(self,window):
        window.blit(self.sprite,(self.x-self.size/2,self.y-self.size/2))

class Asteroid:

    def __init__(self,sprite,window_size,initialType,x=None,y=None): #Constructeur de l'objet
        self.sprite=sprite
        self.type=initialType
        self.size=0
        if (x is None): #Si on ne passe pas de paramètre, créé aléatoirement sur l'écran
            self.x=random.randint(0,window_size[0])
            self.y=random.randint(0,window_size[1])
        else:   #Sinon on crée l'objet à la bonne position
            self.x=x
            self.y=y        
        self.Appearance(self.sprite)

    def Appearance(self,sprite):    #Dimensionne l'asteroide selon son type et altère la taille pour les rendre uniques
        if (self.type==1):
            size=60
        elif (self.type==2):
            size=30
        elif (self.type==3):
            size=15
        scale=random.uniform(0.7,1)
        self.size=int(scale*size)
        self.sprite=pygame.transform.scale(sprite,(self.size,self.size))

    def Destroy(self):
        #create 2 new asteroids with type-=1
        pass

    def Draw(self,window):
        window.blit(self.sprite,(self.x-self.size/2,self.y-self.size/2))