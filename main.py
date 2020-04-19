import pygame
import os.path
from threading import Thread
pygame.init()

#Import des modules contenant les classes que l'on va instancier
import objects, interface

class Game: # La partie 
    def __init__(self, sprites_list, window_size):
        self.window_size = window_size
        self.sprites_list = sprites_list
        self.score = 0
        self.level = 1
        self.StartLevel(self.level)
        self.game_info=interface.GameInfo()

    def StartLevel(self, level): #On instancie les objets au début de niveau        
        self.player_space_ship = objects.PlayerSpaceShip(self.sprites_list["Player"],self.window_size[0]/2,self.window_size[1]/2)
        self.asteroids = [] #Création d'un tableau qui contient tous les astéroides
        self.ennemyspaceships = [] #Création d'un tableau contenant tous les vaisseaux ennemis
        for i in range(2*level):
            self.asteroids.append(objects.Asteroid(self.sprites_list["Asteroid"],self.window_size,1))
        self.ennemyspaceships.append(objects.EnnemySpaceShip(self.sprites_list["Ennemy"],1,200,300))

    def UpdateLoop(self,window,window_size):
        self.GameEvents(window_size)#Gestion des évènements de la partie
        self.GameDraw(window) #Dessiner ce qu'elle contient dans la fenêtre

    def GameEvents(self,window_size):   #Gère les évènements de la partie en continu
        self.BorderWrapping(self.player_space_ship,window_size)
        for asteroid in self.asteroids:
            self.BorderWrapping(asteroid,window_size)

    def BorderWrapping(self,obj,window_size):   #Si les objets sont à la limite de la fenêtre, ils se tp à l'opposé
        if (obj.x > window_size[0]):
            obj.x = 0
        elif (obj.x < 0 ):
            obj.x = window_size[0]
        if (obj.y > window_size[1]):
            obj.y = 0
        elif (obj.y < 0 ):
                obj.y = window_size[1]

    def GameDraw(self,window):    #Demande à chaque élément contenu dans la partie de se dessiner dans la fenêtre
        self.player_space_ship.Draw(window)
        for asteroid in self.asteroids:
            asteroid.Draw(window)
            asteroid.Move()
        for ennemyspaceship in self.ennemyspaceships:
            ennemyspaceship.Draw(window)
        self.game_info.DrawGameInfo(self.score,self.level,self.player_space_ship.GetLife)    #Todo: Executer sur un thread différent -> Pas besoin d'update à 60fps l'affichage

class App: # Le programme
    def __init__(self):
        self.folder = os.path.dirname(__file__) #Va chercher le répertoire dans lequel est le Main
        self.window_size=[1280,720] #Tableau qui contient la résolution de la fenêtre
        pygame.display.set_caption("Asteroids")
        self.window = pygame.display.set_mode((self.window_size[0],self.window_size[1]), pygame.DOUBLEBUF)    #Création de la fenêtre
        self.GetAssets()
        self.game = Game(self.sprite_list,self.window_size)    #Sera instancié quand on clique sur NEW GAME
        clock = pygame.time.Clock()

        self.running = True        
        while self.running:  #Boucle qui exécute et affiche le jeu + vérifie les inputs
            self.Events()   #Gestion des évènements/inputs/clics
            self.window.fill((0,0,0)) #Vide l'affichage de la frame
            self.FrameDraw() #Appelle la fonction qui dessine les objets du jeu
            clock.tick(60)
        pygame.quit()

    def GetAssets(self):   #Va chercher les assets dans les fichiers du jeu
        self.sprite_list = {    #Dictionnaire qui associe une image à un mot clé
            "Player": pygame.image.load(os.path.join(self.folder, 'Assets/player.png')),
            "Asteroid": pygame.image.load(os.path.join(self.folder, 'Assets/rock.png')),
            "Ennemy": pygame.image.load(os.path.join(self.folder, 'Assets/ennemy.png'))
        }

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Lorsque l'on clique sur la croix pour quitter
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
        self.game.UpdateLoop(self.window,self.window_size) #Evènements de la partie à exécuter
        pygame.display.update() #Met à jour l'affichage

if __name__ == "__main__":  #Instancie le programme
    app = App()