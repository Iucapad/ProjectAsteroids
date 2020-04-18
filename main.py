import pygame
import os.path
from threading import Thread
pygame.init()

#Import des modules contenant les classes que l'on va instancier
import objects

class Game: # La partie 
    def __init__(self, sprites_list, window_size):
        self.window_size = window_size
        self.sprites_list = sprites_list
        self.score = 0
        self.level = 1
        self.StartLevel(self.level)

    def StartLevel(self, level): #On instancie les objets au début de niveau        
        self.player_space_ship = objects.PlayerSpaceShip(self.sprites_list["Player"],self.window_size[0]/2,self.window_size[1]/2)
        self.asteroids = []
        for i in range(2*level):
            self.asteroids.append(objects.Asteroid(self.sprites_list["Asteroid"],self.window_size,1))

    def GameDraw(self,win):    #Cette fonction va dessiner chaque élément du niveau
        self.player_space_ship.Draw(win)
        for asteroid in self.asteroids:
            asteroid.Draw(win)

class App: # Le programme
    def __init__(self):
        self.folder = os.path.dirname(__file__)
        self.window_size=[1280,720]
        self.window = pygame.display.set_mode((self.window_size[0],self.window_size[1]))        
        self.GetSprites()
        self.game = Game(self.sprite_list,self.window_size)    #Sera instancié quand on clique sur NEW GAME

        self.running = True        
        while self.running:  #Boucle qui exécute et affiche le jeu + vérifie les inputs
            pygame.time.delay(100)
            self.Events()   #Gestion des évènements/inputs/clics
            self.window.fill((0,0,0)) #Vide l'affichage de la frame
            self.FrameDraw() #Appelle la fonction qui dessine les objets du jeu
            pygame.display.update() #Met à jour l'affichage
        pygame.quit()

    def GetSprites(self):   #Va chercher les assets dans les fichiers du jeu
        self.sprite_list = {
            "Player": pygame.image.load(os.path.join(self.folder, 'Assets/player.png')),
            "Asteroid": pygame.image.load(os.path.join(self.folder, 'Assets/rock.png'))
        }

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print('Clic gauche')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   # PlayerSpaceShip.angle += 10
                #player.Key(event.key)
                    pass

    def FrameDraw(self):    #Cette fonction va dessiner chaque élément du programme
        self.game.GameDraw(self.window)

if __name__ == "__main__":  #Instancie le programme
    app = App()