import os.path
import random


import pygame

import objects, interface   #Import des modules contenant les classes que l'on va instancier

pygame.init()

class Game: # La partie 
    def __init__(self, app):
        self.app=app
        self.score = 0
        self.level = 1
        self.start_level(self.level)
        self.game_info = interface.GameInfo(self.app)
        self.key_pressed = {}
        self.player_space_ship = objects.PlayerSpaceShip(self.app.sprites_list["Player"], self.app.window_size[0]/2, self.app.window_size[1]/2)
        self.coins = 0

    def start_level(self, level): # On instancie les objets au début de niveau
        self.asteroids = [] # Création d'un tableau qui contient tous les astéroides
        self.ennemyspaceships = [] #Création d'un tableau contenant tous les vaisseaux ennemis
        for i in range(level+1):
            alt_spr=random.randint(1,3)
            self.asteroids.append(objects.Asteroid(self.app.sprites_list["Asteroid"+str(alt_spr)], self.app.window_size, 1))         # Instanciation des objets asteroids
        if (self.level>1):
            self.ennemyspaceships.append(objects.EnnemySpaceShip(self.app.sprites_list["Ennemy"], 1, 200, 300))

    def complete_level(self):
        self.player_space_ship.x=self.app.window_size[0]/2
        self.player_space_ship.y=self.app.window_size[1]/2
        self.score += 100
        self.shop=interface.Shop(self)
        self.level += 1
        self.start_level(self.level)

    def update_loop(self,window,window_size):
        self.game_draw(window) #Dessiner ce qu'elle contient dans la fenêtre
        self.game_events(window_size)#Gestion des évènements de la partie
        self.game_collisions()#Gestion des collisions des objets        

    def game_events(self,window_size):   #Gère les évènements de la partie en continu
        self.border_wrapping(self.player_space_ship,window_size)
        for asteroid in self.asteroids:
            self.border_wrapping(asteroid,window_size)
        for ennemyspaceship in self.ennemyspaceships:
            self.border_wrapping(ennemyspaceship,window_size)

        if self.key_pressed.get(pygame.K_LEFT):
            self.player_space_ship.angle_orientation += 5

        if self.key_pressed.get(pygame.K_RIGHT):
            self.player_space_ship.angle_orientation -= 5

        if self.key_pressed.get(pygame.K_UP):
            self.player_space_ship.thrust = True
            self.player_space_ship.angle_inertie = self.player_space_ship.angle_orientation
        else:
            self.player_space_ship.thrust = False

        if self.key_pressed.get(pygame.K_SPACE):
            pass    #TIR

    def game_collisions(self):
        for asteroid in self.asteroids:
            if (self.player_space_ship.rect.collidepoint(asteroid.rect.x,asteroid.rect.y)):
                print("echo")

    def border_wrapping(self,obj,window_size):   #Si les objets sont à la limite de la fenêtre, ils se tp à l'opposé
        if (obj.x > window_size[0]):
            obj.x = 0
        elif (obj.x < 0 ):
            obj.x = window_size[0]
        if (obj.y > window_size[1]):
            obj.y = 0
        elif (obj.y < 0 ):
                obj.y = window_size[1]

    def game_draw(self, win):    # Cette fonction va dessiner chaque élément du niveau
        self.player_space_ship.draw(win)
        self.player_space_ship.move()
        for asteroid in self.asteroids:
            asteroid.draw(win)
            asteroid.move()
        for ennemyspaceship in self.ennemyspaceships:
            ennemyspaceship.draw(win)
        self.game_info.draw_game_info(self.app,self.score,self.level,self.player_space_ship.get_life)    #Todo: Executer sur un thread différent -> Pas besoin d'update à 60fps l'affichage

class App: # Le programme
    def __init__(self):
        self.state="menu"
        self.folder = os.path.dirname(__file__)
        self.window_size = [1280,720]
        pygame.display.set_caption("Asteroids")
        self.window = pygame.display.set_mode((self.window_size[0],self.window_size[1]),pygame.DOUBLEBUF)        
        self.load_sprites()
        self.menu=interface.MainMenu(self)
        clock = pygame.time.Clock()

        self.running = True        
        while self.running:
            self.window.fill((0,0,0))                           # Vide l'affichage de la frame
            self.frame_draw()                                    # Appelle la fonction qui dessine les objets du jeu
            self.events()                                       # Gestion des évènements/inputs/clics
            clock.tick(60)                                      # Met à jour l'affichage
        pygame.quit()

    def start_game(self):
        self.game = Game(self)
        self.state="game"

    def load_sprites(self):                                       # Va chercher les assets dans les fichiers du jeu
        self.sprites_list = {
            "Player": pygame.image.load(os.path.join(self.folder, 'Assets/player.png')),
            "Asteroid1": pygame.image.load(os.path.join(self.folder, 'Assets/asteroid1.png')),
            "Asteroid2": pygame.image.load(os.path.join(self.folder, 'Assets/asteroid2.png')),
            "Asteroid3": pygame.image.load(os.path.join(self.folder, 'Assets/asteroid3.png')),
            "Ennemy": pygame.image.load(os.path.join(self.folder, 'Assets/ennemy.png'))
        }
        background=pygame.image.load(os.path.join(self.folder, 'Assets/background.png'))
        self.background=pygame.transform.scale(background, (self.window_size[0], self.window_size[1]))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Lorsque l'on clique sur la croix pour quitter
                self.running = False
            if self.state=="game":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state="menu"
                        self.pause=interface.PauseMenu(self)
                    elif event.key == pygame.K_SPACE:
                        self.game.complete_level()
                    else:
                        self.game.key_pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.game.key_pressed[event.key] = False                   


    def frame_draw(self):    #Cette fonction va dessiner chaque élément du programme
        if self.state=="game":
            self.game.update_loop(self.window,self.window_size) #Evènements de la partie à exécuter
            pygame.display.update() #Met à jour l'affichage

if __name__ == "__main__":  #Instancie le programme
    app = App()