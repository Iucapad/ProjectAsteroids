import random
import math
import pygame

class PlayerSpaceShip:
    def __init__(self, sprite_list, x, y,size=50):   # Constructeur
        self.x = x                              # Place le joueur à la position indiquée
        self.y = y   
        self.sprite_list = sprite_list               # L'image du vaisseau 
        self.rect = self.sprite_list["Player"].get_rect(center=(self.x, self.y))
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
        self.is_invincible = 60

    def move(self):
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

        self.x += self.vitesse_horizontale
        self.y -= self.vitesse_verticale

    def teleport(self): # Méthode pour la téléportaiton Todo
        if (True) :
            #TP()
            pass
        else :
            self.teleport()

    @property
    def get_life(self):
        return self.life

    def get_invincibility(self,time):
        self.is_invincible=time

    def draw(self,window): # Méthode d'affichage
        if (self.is_invincible>0):
            self.is_invincible-=1
            sprite = self.sprite_list["Player1"]
            surface = pygame.transform.rotate(sprite,self.angle_orientation)
        else:
            sprite = self.sprite_list["Player"]
            surface = pygame.transform.rotate(sprite,self.angle_orientation)
        self.rect = surface.get_rect(center=(self.x, self.y))
        window.blit(surface,self.rect)

class EnnemySpaceShip:
    def __init__(self, sprite, space_ship_type, x, y): # Constructeur
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.angle = 90
        self.max_vitesse = 15
        self.acceleration = 0 
        self.size = 50
        self.angle_orientation=random.randint(0, 360)
        self.life = 2
        self.acceleration = 0.5
        self.deceleration = 0.1
        self.shoot_rate = 1   
        self.type = space_ship_type

    def move(self):
        print("todo")  

    def shoot(self): # Méthode pour le tir      ####DAMIEN: (sprite_list["LaserShot"])
        pass

    def draw(self,window): # Méthode d'affichage
        surface = pygame.transform.rotate(self.sprite,self.angle_orientation)  
        self.rect = surface.get_rect(center=(self.x, self.y))        
        window.blit(surface,self.rect)


class Asteroid:
    def __init__(self, sprite, window_size, asteroid_type, x=None, y=None): # Constructeur de l'objet
        if (x is None): #Si on ne passe pas de paramètre, créé aléatoirement sur l'écran
            self.x=random.randint(0, window_size[0])
            self.y=random.randint(0, window_size[1])
        else:   # Sinon on crée l'objet à la position demandée
            self.x = x
            self.y = y  
        self.sprite = sprite
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.type = asteroid_type
        self.vitesse=random.randint(7,10)
        self.size = 0
        self.angle = int(math.degrees( math.atan( ((window_size[1]/2)-self.y) / ((window_size[0]/2)-self.x))))                # L'angle est adapté en fct de la postion du vaisseau du joueur
        self.angle_orientation=random.randint(0, 360)
        self.rotation=random.randint(1,2)
        self.appearance(self.sprite)
        self.valX = int((math.cos(math.radians(self.angle)) * self.vitesse) /5)
        self.valY = int((math.sin(math.radians(self.angle)) * self.vitesse) /5)

    def move(self): #Méthode pour le déplacement des astéroïdes
        self.x += self.valX
        self.y -= self.valY        
        if self.rotation==1:                #Orientation du sprite
            self.angle_orientation+=0.1
        if self.rotation==2:
            self.angle_orientation-=0.1

    def appearance(self, sprite):    #Dimensionne l'asteroide selon son type et initialise un angle de déplacement
        if (self.type == 1):    #Type Grand
            size = 60
        elif (self.type == 2):  #Type Moyen
            size = 30
        elif (self.type == 3):  #Type Petit
            size = 15
        scale=random.uniform(0.7,1) 
        self.size = int(scale*size) # Fait varier la dimension pour les rendre uniques
        self.sprite = pygame.transform.scale(sprite,(self.size,self.size))        

    def destroy(self):  #PAS CERTAIN QUE CE SOIT ICI
        #create 2 new asteroids with type-=1 at self.x,self.y
        pass

    def draw(self,window):  #Dessine l'objet présent à sa position
        surface = pygame.transform.rotate(self.sprite,self.angle_orientation)  
        self.rect = surface.get_rect(center=(self.x, self.y))
        window.blit(surface,self.rect)

class LaserShot:

    def __init__(self, laser_shot_type, x, y, angle): # todo:  sprite
        self.x = x 
        self.y = y 
        self.angle = angle
        self.vitesse = 10
        self.type = laser_shot_type # Todo
        self.shots.append(self)

    def shoot(self): # Méthode pour le tir
        tir = LaserShot(1, self.x, self.y, self.angle_orientation)


    def move(self):
        self.x += math.cos(self.angle) * self.vitesse
        self.y += math.sin(self.angle) * self.vitesse

    def draw(self, window): 
        


class BonusItem:
    def __init__(self, sprite, bonus_type, x, y):
        self.x=x
        self.y=y
        self.sprite = sprite
        self.bonus_type = bonus_type

class BlackHole:
    pass