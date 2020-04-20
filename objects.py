import pygame
import random
import math

class PlayerSpaceShip:
    def __init__(self, sprite, x, y,size=50):   # Constructeur
        self.sprite = sprite                    # L'image du vaisseau 
        self.rect = self.sprite.get_rect()
        self.rect.x = x-size/2                  # Place le joueur à la position indiquée
        self.rect.y = y-size/2    
        self.angle_orientation = 0              # angle de vue
        self.angle_inertie = 0                  # angle de déplacement
        self.thrust = False                     # true = le vaisseau accélère
        self.vitesse = 1                        # Vitesse actuelle
        self.max_vitesse = 6                    # Vitesse max
        self.vitesse_horizontale = 0
        self.vitesse_verticale = 0
        self.acceleration = 0.5 		        # Inertie
        self.deceleration = 0.1			        # Inertie                      
        self.life = 3                           # Nombre de vie
        self.shoot_rate = 1                     # Cadence de tir  
        self.shoot_type = 0      
        self.is_invincible = False

    def Move(self):
        self.vitesse = math.sqrt(self.vitesse_horizontale**2 + self.vitesse_verticale**2)     # Calcul de la vitesse actuelle
        
        if self.thrust: # Si l'utilisateur appuie appuie sur ↑
            if self.vitesse + self.acceleration < self.max_vitesse:  # Si la vitesse actuelle est inférieure à la vitesse maximale
                self.vitesse_horizontale += self.acceleration * math.cos(self.angle_orientation * math.pi / 180)  
                self.vitesse_verticale += self.acceleration * math.sin(self.angle_orientation * math.pi / 180)
            else:   # Si la vitesse actuelle est égale à la vitesse max
                self.vitesse_horizontale = self.max_vitesse * math.cos(self.angle_orientation * math.pi / 180) 
                self.vitesse_verticale = self.max_vitesse * math.sin(self.angle_orientation * math.pi / 180)

        else:   # Si l'utilisateur n'appuie pas sur ↑
            if self.vitesse - self.deceleration > 0:   # Si le vaisseau est toujours en mouvement 
                change_in_vitesse_horizontale = (self.deceleration * math.cos(self.vitesse_verticale / self.vitesse_horizontale))
                change_in_vitesse_verticale = (self.deceleration * math.sin(self.vitesse_verticale / self.vitesse_horizontale))
                if self.vitesse_horizontale != 0:
                    if change_in_vitesse_horizontale / abs(change_in_vitesse_horizontale) == self.vitesse_horizontale / abs(self.vitesse_horizontale):
                        self.vitesse_horizontale -= change_in_vitesse_horizontale
                    else:
                        self.vitesse_horizontale += change_in_vitesse_horizontale
                if self.vitesse_verticale != 0:
                    if change_in_vitesse_verticale / abs(change_in_vitesse_verticale) == self.vitesse_verticale / abs(self.vitesse_verticale):
                        self.vitesse_verticale -= change_in_vitesse_verticale
                    else:
                        self.vitesse_verticale += change_in_vitesse_verticale
            else: # Si le vaisseau a perdu toute sa vitesse
                self.vitesse_horizontale = 0
                self.vitesse_verticale = 0

        self.rect.x += self.vitesse_horizontale
        self.rect.y -= self.vitesse_verticale
  

    def Shoot(self): # Méthode pour le tir
        pass    # Todo

    def Teleport(self): # Méthode pour la téléportaiton Todo
        if (True) :
            #TP()
            pass
        else :
            Teleport()

    @property
    def GetLife(self):
        return self.life

    @property
    def GetInvincibilty(self):
        return self.is_invincible

    @is_invincible.setter
    def SetInvincibility(self, value):
        self.is_invincible = value

    def Draw(self,window): # Méthode d'affichage
        surface = pygame.transform.rotate(self.sprite,self.angle_orientation)     
        window.blit(surface,self.rect)

class EnnemySpaceShip:
    def __init__(self, sprite, space_ship_type, x, y): # Constructeur
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 90
        self.max_vitesse = 15
        self.acceleration = 0 
        self.size = 50
        self.life = 2
        self.acceleration = 0.5
        self.deceleration = 0.1
        self.shoot_rate = 1   
        self.type = space_ship_type

    def Move(self):
        print("todo")
  

    def Shoot(self): # Méthode pour le tir
        pass

    def Teleport(self): # Méthode pour la téléportation
        if (True) :
            #TP()
            pass
        else :
            Teleport()

    def Draw(self,window): # Méthode d'affichage
        window.blit(self.sprite,self.rect)


class Asteroid:
    def __init__(self, sprite, window_size, asteroid_type, x=None, y=None): #Constructeur de l'objet
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.type = asteroid_type
        self.vitesse=random.randint(7,10)
        self.size = 0
        self.angle=random.randint(0, 360)
        self.angle_orientation=random.randint(0, 360)
        self.rotation=random.randint(1,2)
        if (x is None): #Si on ne passe pas de paramètre, créé aléatoirement sur l'écran
            self.rect.x=random.randint(0, window_size[0])
            self.rect.y=random.randint(0, window_size[1])
        else:   #Sinon on crée l'objet à la position demandée
            self.x = x
            self.y = y    
        self.Appearance(self.sprite)
        self.valX=(math.cos(self.angle)*self.vitesse)/5
        self.valY=(math.sin(self.angle)*self.vitesse)/5

    def Move(self): #Méthode pour le déplacement des astéroïdes
        self.rect.x += self.valX
        self.rect.y += self.valY        
        if self.rotation==1:                #Orientation du sprite
            self.angle_orientation+=0.1
        if self.rotation==2:
            self.angle_orientation-=0.1

    def Appearance(self, sprite):    #Dimensionne l'asteroide selon son type et initialise un angle de déplacement
        if (self.type == 1):    #Type Grand
            size = 60
        elif (self.type == 2):  #Type Moyen
            size = 30
        elif (self.type == 3):  #Type Petit
            size = 15
        scale=random.uniform(0.7,1) #Donne un angle aléatoire pour son mouvement initial
        self.size = int(scale*size) #Fait varier la dimension pour les rendre uniques
        self.sprite = pygame.transform.scale(sprite,(self.size,self.size))        

    def Destroy(self):  #PAS CERTAIN QUE CE SOIT ICI
        #create 2 new asteroids with type-=1 at self.x,self.y
        pass

    def Draw(self,window):  #Dessine l'objet présent à sa position
        surface = pygame.transform.rotate(self.sprite,self.angle_orientation)
        window.blit(surface,self.rect)

class LaserShot:
    def __init__(self, sprite, laser_shot_type, x, y):
        self.x = x 
        self.y = y 
        self.angle = 90
        self.vitesse = 1
        self.type = laser_shot_type # Todo

class BonusItem:
    def __init__(self, sprite, bonus_type):
        self.sprite = sprite
        self.bonus_type = bonus_type

