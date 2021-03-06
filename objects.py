import random
import math
import pygame
import time

class PlayerSpaceShip:
    def __init__(self, sprite_list, x, y,size=50):   # Constructeur
        self.x = x                              # Place le joueur à la position indiquée
        self.y = y   
        self.sprite_list = sprite_list               # L'image du vaisseau 
        self.rect = self.sprite_list["Player"].get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite_list["Player"])
        self.angle_orientation = 0              # angle de vue
        self.angle_inertie = 0                  # angle de déplacement
        self.thrust = False                     # true = le vaisseau accélère
        self.vitesse = 1                        # Vitesse actuelle
        self.max_vitesse = 6                    # Vitesse max
        self.vitesse_horizontale = 0
        self.vitesse_verticale = 0
        self.acceleration = 0.5 		        # Inertie
        self.deceleration = 0.07			        # Inertie                      
        self.life = 3                           # Nombre de vie
        self.shoot_rate = 0.3                   # Cadence de tir  (délai entre chaque tir en seconde)
        self.shoot_type = 0   
        self.last_shot = time.time() 
        self.is_invincible = 120
        self.teleported = 0


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

    def teleport(self, asteroids, vaisseaux, son_teleport, black_hole,sound): # Méthode pour la téléportaiton Todo
        if self.teleported == 0:
            self.x = random.randint(200, 1080)
            self.y = random.randint(120, 620)
            if not( pygame.sprite.spritecollide(self, asteroids, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(self, black_hole, pygame.sprite.collide_mask) ) :
                self.teleported = 1
                if (sound):
                    son_teleport.play()
                self.is_invincible = 120
            else :
                self.teleport(asteroids, vaisseaux)

    @property
    def get_life(self):
        return self.life

    def get_invincibility(self,time):
        self.is_invincible=time

    def draw(self,window): # Méthode d'affichage
        if (self.is_invincible>0):
            self.is_invincible-=1
            sprite = self.sprite_list["Player1"]
        else:
            sprite = self.sprite_list["Player"]
        surface = pygame.transform.rotate(sprite,self.angle_orientation)
        self.rect = surface.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(sprite)
        window.blit(surface,self.rect)        

class EnnemySpaceShip:
    def __init__(self, sprite, space_ship_type, x, y): # Constructeur
        self.x = random.randint(100, 1180)
        self.y = random.randint(50, 670)
        self.sprite = sprite
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)                                
        self.max_vitesse = 15
        self.acceleration = 0 
        self.size = 50
        self.angle_orientation = 0
        self.angle_direction = 0
        self.life = 2
        self.acceleration = 0.5
        self.deceleration = 0.1
        self.shoot_rate = 1.5    # Cadence de tir  (délai entre chaque tir en seconde)
        self.last_shot = time.time() 
        self.type = space_ship_type

    def move(self, player):        
        if not(self.rect.colliderect(player.rect)):
            opp=player.y - self.y
            adj=player.x - self.x
            self.angle_direction = -math.atan((opp)/(adj))   # L'angle est adapté en fct de la postion du vaisseau du joueur
            if (adj<0):
                self.angle_orientation = ((self.angle_direction*180)/math.pi)+180
            else:
                self.angle_orientation = ((self.angle_direction*180)/math.pi)
            if self.x > player.x:   
                self.x -= math.cos(self.angle_direction)
                self.y += math.sin(self.angle_direction)
            elif self.x < player.x:
                if self.y > player.y:
                    self.x += math.cos(self.angle_direction)
                    self.y -= math.sin(self.angle_direction)
                elif self.y < player.y :
                    self.x += math.cos(self.angle_direction)
                    self.y -= math.sin(self.angle_direction)

    def draw(self,window): # Méthode d'affichage
        surface = pygame.transform.rotate(self.sprite,self.angle_direction)  
        self.rect = surface.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(surface)       
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
        self.mask = pygame.mask.from_surface(self.sprite)
        self.type = asteroid_type
        self.vitesse=random.randint(7,10)
        self.size = 0
        self.angle = int(math.degrees( math.atan( ((window_size[1]/2)-self.y) / 0.00000001 + ((window_size[0]/2)-self.x))))                # L'angle est adapté en fct de la postion du vaisseau du joueur
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
            size = 120
        elif (self.type == 2):  #Type Moyen
            size = 90
        elif (self.type == 3):  #Type Petit
            size = 60
        scale=random.uniform(0.8,1) 
        self.size = int(scale*size) # Fait varier la dimension pour les rendre uniques
        self.sprite = pygame.transform.scale(sprite,(self.size,self.size))  

    def draw(self,window):  #Dessine l'objet présent à sa position
        surface = pygame.transform.rotate(self.sprite,self.angle_orientation)  
        self.rect = surface.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(surface)
        window.blit(surface,self.rect)

class LaserShot:

    def __init__(self, sprite, laser_shot_type, x, y, angle): # todo:  sprite
        self.x = x 
        self.y = y 
        self.angle = math.radians(angle)
        self.sprite = sprite
        self.rect = sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        self.vitesse = 10
        self.type = laser_shot_type # Todo

    def move(self):
        self.x += math.cos(self.angle) * self.vitesse
        self.y -= math.sin(self.angle) * self.vitesse

    def draw(self, window): 
        surface = pygame.transform.rotate(self.sprite,self.angle)  
        self.rect = surface.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(surface)
        window.blit(surface, self.rect)

class BonusItem:
    def __init__(self, sprite, bonus_type, x, y):
        self.x=x
        self.y=y
        self.sprite = sprite
        self.speed = 1
        self.angle_direction = 0
        self.acceleration_item = 2
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        self.bonus_type = bonus_type

    def draw(self,window):
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        window.blit(self.sprite, self.rect)

    def move(self, trou_noir):
        if len(trou_noir) == 1:
            for black_hole in trou_noir:
                opp = black_hole.y - self.y
                adj = black_hole.x - self.x
                self.angle_direction = -math.atan((opp)/(adj))
                distance = math.sqrt(opp**2 + adj**2)
                self.acceleration_item = 8 / ( distance / 100 )

                if (adj<0):
                    self.angle_orientation = ((self.angle_direction*180)/math.pi)+180
                else:
                    self.angle_orientation = ((self.angle_direction*180)/math.pi)

                if self.x > black_hole.x:   
                    self.x -= math.cos(self.angle_direction) * self.acceleration_item
                    self.y += math.sin(self.angle_direction) * self.acceleration_item
                elif self.x < black_hole.x:
                    if self.y > black_hole.y:
                        self.x += math.cos(self.angle_direction) * self.acceleration_item
                        self.y -= math.sin(self.angle_direction) * self.acceleration_item
                    elif self.y < black_hole.y :
                        self.x += math.cos(self.angle_direction) * self.acceleration_item
                        self.y -= math.sin(self.angle_direction) * self.acceleration_item

class BlackHole:
    def __init__(self, sprite, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.vitesse = 1
        self.sprite = sprite
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window):
        self.angle+=1
        surface = pygame.transform.rotate(self.sprite, self.angle)
        self.rect = surface.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(surface)
        window.blit(surface, self.rect)