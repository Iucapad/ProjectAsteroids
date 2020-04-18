import pygame
import random
import math

class PlayerSpaceShip:

    def __init__(self, sprite, x, y):  # Constructeur
        self.sprite = sprite        # L'image du vaisseau 
        self.x = x                  # Todo, faire centrer le vaisseau du joueur au centre de la fenêtre
        self.y = y
        self.angle = 90
        self.speed = 1              # A test
        self.acceleration = 0       # A test
        self.size = 50              
        self.life = 3   
        self.shoot_rate = 1          # A test   
        self.type = 0               

    def Move(self):
        self.x = x + math.cos(self.angle)   # A test
        self.y = y + math.sin(self.angle)

    def Shoot(self): # Méthode pour le tir
        pass    # Todo

    def Teleport(self): # Méthode pour la téléportaiton Todo
        if (True) :
            #TP()
            pass
        else :
            Teleport()

    def Draw(self,window): # Méthode d'affichage
        window.blit(self.sprite,(self.x-self.size/2,self.y-self.size/2))


class EnnemySpaceShip:

    def __init__(self, sprite, space_ship_type, x, y): # Constructeur
        self.sprite = sprite
        self.x = x
        self.y = y
        self.angle = 90
        self.speed = 1
        self.acceleration = 0 
        self.size = 50
        self.life = 2
        self.shoot_rate = 1   
        self.type = space_ship_type

    def Move(self):
        self.x = x + math.cos(self.angle)   # A test
        self.y = y + math.sin(self.angle)

    def Shoot(self): # Méthode pour le tir
        pass

    def Teleport(self): # Méthode pour la téléportaiton
        if (True) :
            #TP()
            pass
        else :
            Teleport()

    def Draw(self,window): # Méthode d'affichage
        window.blit(self.sprite,(self.x-self.size/2,self.y-self.size/2))


class Asteroid:

    def __init__(self, sprite, window_size, asteroid_type, x=None, y=None): #Constructeur de l'objet
        self.sprite = sprite
        self.type = asteroid_type
        self.size = 0
        if (x is None): #Si on ne passe pas de paramètre, créé aléatoirement sur l'écran
            self.x=random.randint(0, window_size[0])
            self.y=random.randint(0, window_size[1])
        else:   #Sinon on crée l'objet à la bonne position
            self.x = x
            self.y = y        
        self.Appearance(self.sprite)

    def Move(self):
        self.x = x + math.cos(self.angle)   # A test
        self.y = y + math.sin(self.angle)

    def Appearance(self, sprite):    #Dimensionne l'asteroide selon son type et altère la taille pour les rendre uniques
        if (self.type == 1):
            size = 60
        elif (self.type == 2):
            size = 30
        elif (self.type == 3):
            size = 15
        scale=random.uniform(0.7,1)
        self.size = int(scale*size)
        self.sprite = pygame.transform.scale(sprite,(self.size,self.size))

    def Destroy(self):
        #create 2 new asteroids with type-=1
        pass

    def Draw(self,window):
        window.blit(self.sprite,(self.x-self.size/2,self.y-self.size/2))

class LaserShot:
    
    def __init__(self, sprite, laser_shot_type, x, y):
        self.x = x 
        self.y = y 
        self.angle = 90
        self.speed = 1
        self.type = laser_shot_type # Todo
