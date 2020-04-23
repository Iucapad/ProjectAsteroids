import os.path
import random
import pygame 
import math
import time
import objects, interface   #Import des modules contenant les classes que l'on va instancier

pygame.init()

class Game: # La partie 
    def __init__(self, app):
        self.son_tir_laser = pygame.mixer.Sound(os.path.join(app.folder,"Assets/asteroids-ship-shoot.wav"))
        self.son_tir_ennemy = pygame.mixer.Sound(os.path.join(app.folder,"Assets/fire.wav"))
        self.son_gameover = pygame.mixer.Sound(os.path.join(app.folder,"Assets/boom.wav"))
        self.son_dmg = pygame.mixer.Sound(os.path.join(app.folder,"Assets/beep-03.wav"))
        self.son_teleport = pygame.mixer.Sound(os.path.join(app.folder, "Assets/teleport.wav"))
        self.app=app
        self.score = 0
        self.level = 1
        self.game_info = interface.GameInfo(self.app)
        self.key_pressed = {}
        self.player_space_ship = objects.PlayerSpaceShip(self.app.sprites_list, self.app.window_size[0]/2, self.app.window_size[1]/2)
        self.coins = 0
        self.ennemy_number = 0
        self.difficulty=app.settings_list["Difficulty"]
        self.start_level(self.level)

    def start_level(self, level): # On instancie les objets au début de niveau
        self.asteroids = [] # Création d'un tableau qui contient tous les astéroides
        self.ennemyspaceships = [] #Création d'un tableau contenant tous les vaisseaux ennemis
        self.shots = [] # Création d'un tableau contenant tout les tirs
        self.bonus_list = [] #Création d'un tableau contenant les bonus apparus
        self.black_hole = []
        

        for i in range(level+3):
            alt_spr = random.randint(1,3)
            self.asteroids.append(objects.Asteroid(self.app.sprites_list["Asteroid"+str(alt_spr)], self.app.window_size, 1))          # Instanciation des objets asteroids

        if self.level > 1 :
            if self.ennemy_number == 0:
                self.ennemy_number += 1
            if self.level % 5 == 0:
                    self.ennemy_number += 1
                    self.black_hole_number = 1
            else :
                self.black_hole_number = 0
            for i in range(self.ennemy_number):
                if (self.difficulty>=0):
                    self.ennemyspaceships.append(objects.EnnemySpaceShip(self.app.sprites_list["Ennemy"], 1, 200, 300))
                if (self.difficulty>=1):
                    self.ennemyspaceships.append(objects.EnnemySpaceShip(self.app.sprites_list["Ennemy1"], 2, 200, 300))
                if (self.difficulty==2):
                    self.ennemyspaceships.append(objects.EnnemySpaceShip(self.app.sprites_list["Ennemy"], 1, 200, 300))
            if self.black_hole_number == 1:
                tmp_x = random.randint(0, 1)
                tmp_y = random.randint(0, 1)
                if tmp_x == 0:
                    if tmp_y == 0:
                        self.black_hole.append( objects.BlackHole(self.app.sprites_list["BlackHole"], random.randint(100, (self.app.window_size[0]/2)-200), random.randint(100, (self.app.window_size[1]/2)-100)))  # Instanciation du trou noir
                    else:
                        self.black_hole.append( objects.BlackHole(self.app.sprites_list["BlackHole"], random.randint(100, (self.app.window_size[0]/2)-200), random.randint(100, (self.app.window_size[1]/2)+100)))
                else :
                    if tmp_y == 0:
                        self.black_hole.append( objects.BlackHole(self.app.sprites_list["BlackHole"], random.randint(100, (self.app.window_size[0]/2)+200), random.randint(100, (self.app.window_size[1]/2)-100)))
                    else:
                       self.black_hole.append( objects.BlackHole(self.app.sprites_list["BlackHole"], random.randint(100, (self.app.window_size[0]/2)+200), random.randint(100, (self.app.window_size[1]/2)+100)))
            
    def complete_level(self):
        self.player_space_ship.x=self.app.window_size[0]/2
        self.player_space_ship.y=self.app.window_size[1]/2
        self.score += 100
        self.shop=interface.Shop(self)
        self.level += 1
        self.start_level(self.level)
        self.player_space_ship.teleported = 0
        self.player_space_ship.is_invincible = 120

    def update_loop(self,window,window_size):
        self.game_draw(window) #Dessiner ce qu'elle contient dans la fenêtre
        self.game_events(window_size)#Gestion des évènements de la partie
        self.game_collisions()#Gestion des collisions des objets        

    def game_events(self,window_size):   # Gère les évènements de la partie en continu
        self.border_wrapping(self.player_space_ship,window_size)
        if (len(self.asteroids) == 0 and len(self.ennemyspaceships) == 0):      # Si le niveau est fini
            self.complete_level()
        for asteroid in self.asteroids:
            self.border_wrapping(asteroid,window_size)

        for ennemy_space_ship in self.ennemyspaceships:                       # Les vaisseaux ennemis
            if (ennemy_space_ship.type==2):
                self.border_wrapping(ennemy_space_ship, window_size)
                if math.sqrt( ( (ennemy_space_ship.x - self.player_space_ship.x)**2 )+ ( (ennemy_space_ship.y - self.player_space_ship.y )**2) ) < 400:                                   
                    if time.time() > ennemy_space_ship.last_shot + ennemy_space_ship.shoot_rate: 
                        tir = objects.LaserShot(self.app.sprites_list["LaserShot2"], 2, ennemy_space_ship.x, ennemy_space_ship.y, ennemy_space_ship.angle_orientation)    # Instanciation du tir des vaisseaux ennemis
                        if (self.app.settings_list["Sounds"]):
                            self.son_tir_ennemy.play()
                        self.shots.append(tir)
                        ennemy_space_ship.last_shot = time.time() 
            if ennemy_space_ship.life == 0:                
                self.coins += 20
                self.score+=ennemy_space_ship.type*25
                self.ennemyspaceships.remove(ennemy_space_ship)

        if self.key_pressed.get(pygame.K_LEFT):                             # Les input        
            self.player_space_ship.angle_orientation += 5

        if self.key_pressed.get(pygame.K_RIGHT):
            self.player_space_ship.angle_orientation -= 5

        if self.key_pressed.get(pygame.K_UP):
            self.player_space_ship.thrust = True
            self.player_space_ship.angle_inertie = self.player_space_ship.angle_orientation
        else:
            self.player_space_ship.thrust = False
        if self.key_pressed.get(pygame.K_DOWN):
            self.player_space_ship.teleport(self.asteroids, self.ennemyspaceships, self.son_teleport, self.black_hole,self.app.settings_list["Sounds"])

        if self.key_pressed.get(pygame.K_SPACE):
            if time.time() > self.player_space_ship.last_shot + self.player_space_ship.shoot_rate: 
                tir = objects.LaserShot(self.app.sprites_list["LaserShot"], 1, self.player_space_ship.x, self.player_space_ship.y, self.player_space_ship.angle_orientation)
                if (self.app.settings_list["Sounds"]):
                    self.son_tir_laser.play()
                self.shots.append(tir)
                self.player_space_ship.last_shot = time.time()

    def game_collisions(self): 
        if (self.player_space_ship.is_invincible==0):
            if pygame.sprite.spritecollide(self.player_space_ship, self.asteroids, False, pygame.sprite.collide_mask):  # Collision entre le joueur et les astéroids
                if (self.app.settings_list["Sounds"]):
                    self.son_dmg.play()
                self.loose_life()                
            collisions =  pygame.sprite.spritecollide(self.player_space_ship, self.shots, False, pygame.sprite.collide_mask)    # Collision entre le joueur et les tirs ennemis
            for key in collisions:
                if (key.type==2):   # Type = 1 tir de joueur, 2 tir ennemis
                    self.shots.remove(key)                    
                    if (self.app.settings_list["Sounds"]):
                        self.son_dmg.play()
                    self.loose_life()
            if pygame.sprite.spritecollide(self.player_space_ship, self.ennemyspaceships, False, pygame.sprite.collide_mask): # Collision entre  le joueur et les vaisseaux ennemis
                if (self.app.settings_list["Sounds"]):
                    self.son_dmg.play()
                self.loose_life()
            if pygame.sprite.spritecollide(self.player_space_ship, self.black_hole,  False, pygame.sprite.collide_mask):    # Collision entre le joueuer et le trou noir
                while self.player_space_ship.life > 0 : 
                    self.player_space_ship.life -= 1
                    self.loose_life()
                
        for ennemyspaceship in self.ennemyspaceships:
            collisions =  pygame.sprite.spritecollide(ennemyspaceship, self.shots, False, pygame.sprite.collide_mask) # Collision entre les vaisseaux ennemis et les tirs
            for key in collisions:
                if (key.type==1):
                    self.shots.remove(key)
                    ennemyspaceship.life-=1

        for black_hole in self.black_hole:
            collisions = pygame.sprite.spritecollide(black_hole, self.shots, False, pygame.sprite.collide_mask) # Collision entre le trou noir et les tirs
            for key in collisions:
                if key.type == 1:
                    self.shots.remove(key)
        
        
        for asteroid in self.asteroids:
            collisions =  pygame.sprite.spritecollide(asteroid, self.shots, False, pygame.sprite.collide_mask)  # Collision entre les astéroids et les tirs 
            for key in collisions:
                if (key.type==1):
                    self.shots.remove(key)  
                    if (asteroid.type==3):
                        luck=random.randint(0,10)
                        if (luck > 3):
                            if (luck >9):
                                self.bonus_list.append(objects.BonusItem(self.app.sprites_list["Bonus2"],2,asteroid.x,asteroid.y))
                            else:
                                self.bonus_list.append(objects.BonusItem(self.app.sprites_list["Bonus1"],1,asteroid.x,asteroid.y))                  
                    if (asteroid.type<3):
                        alt_spr=random.randint(1,3)                    
                        self.asteroids.append(objects.Asteroid(self.app.sprites_list["Asteroid1"], self.app.window_size, asteroid.type+1,asteroid.x+random.randint(10,20),asteroid.y+random.randint(10,20)))
                        self.asteroids.append(objects.Asteroid(self.app.sprites_list["Asteroid2"], self.app.window_size, asteroid.type+1,asteroid.x-random.randint(10,20),asteroid.y-random.randint(10,20)))
                    self.score+=asteroid.type*10
                    self.asteroids.remove(asteroid)
        for shot in self.shots:                
            if (shot.x<0 or shot.x>self.app.window_size[0] or shot.y<0 or shot.y>self.app.window_size[1]):  # Suppression des tirs si ils sortent de l'écran (optimisation)
                self.shots.remove(shot)

        collisionbonus = pygame.sprite.spritecollide(self.player_space_ship, self.bonus_list, False, pygame.sprite.collide_mask)    # Collision entre le joueur et les items bonus
        for key in collisionbonus:
            if (key.bonus_type==1):           
                self.coins+=5
            elif (key.bonus_type==2): 
                self.player_space_ship.life+=1
            self.bonus_list.remove(key)

        for black_hole in self.black_hole:
            collisionbonus_trou_noir = pygame.sprite.spritecollide(black_hole, self.bonus_list, False, pygame.sprite.collide_mask)    # Collision entre les items et le trou noir
            for key in collisionbonus_trou_noir:
                self.bonus_list.remove(key)

    def border_wrapping(self,obj,window_size):   #Si les objets sont à la limite de la fenêtre, ils se tp à l'opposé
        if (obj.x > window_size[0]):
            obj.x = 0
        elif (obj.x < 0 ):
            obj.x = window_size[0]
        if (obj.y > window_size[1]):
            obj.y = 0
        elif (obj.y < 0 ):
                obj.y = window_size[1]

    def loose_life(self):
        if  self.player_space_ship.life > 1: #Vérifie que le joueur ait + d'une vie
            self.player_space_ship.life-=1
            self.player_space_ship.get_invincibility(120)
        else:
            if (self.app.settings_list["Sounds"]):
                self.son_gameover.play()
            if (self.score>int(self.app.best_list[self.app.settings_list["Player_Name"]])):  #Vérifie si le score est un nouveau record personnel
                    f = open(os.path.join(self.app.folder,"Files/stats.txt"),"w")
                    for key in self.app.best_list:
                        if (key==str(self.app.settings_list["Player_Name"])):
                            f.write(
                            str(key)+":"+str(self.score)+"\n"
                            )
                        else:
                            f.write(
                            str(key)+":"+str(self.app.best_list[key])+"\n"
                            )
                    f.close()
            game_over=interface.GameOver(self)

    def game_draw(self, win):    # Cette fonction va dessiner chaque élément du niveau
        for black_hole in self.black_hole:
            black_hole.draw(win)
        for shot in self.shots:
            shot.draw(win)
            shot.move()
        for bonus in self.bonus_list:
            bonus.draw(win)
            bonus.move(self.black_hole)
        self.player_space_ship.draw(win)
        self.player_space_ship.move()
        for ennemyspaceship in self.ennemyspaceships:
            ennemyspaceship.draw(win)
            ennemyspaceship.move(self.player_space_ship)
        for asteroid in self.asteroids:
            asteroid.draw(win)
            asteroid.move()        
            
        self.game_info.draw_game_info(self.app,self.score,self.coins,self.level,self.player_space_ship.get_life)    #Todo: Executer sur un thread différent -> Pas besoin d'update à 60fps l'affichage

class App: # Le programme
    def __init__(self):
        self.state="menu"
        self.folder = os.path.dirname(__file__)
        self.window_size = [1280,720]
        pygame.display.set_caption("Asteroids")
        self.window = pygame.display.set_mode((self.window_size[0],self.window_size[1]),pygame.DOUBLEBUF)        
        self.best_list={}
        self.settings_list={}
        try:                       # Si le fichier n'est pas présent ou corrompu, on aura une erreur plutôt qu'un plantage
            self.load_settings()
            self.load_sprites()
            self.load_statistics()
        except:
            print("except")         #todo afficher une erreur

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

    def load_settings(self):
        file = open(os.path.join(self.folder,'Files/settings.txt'), 'r')    #Charge le fichier de settings
        lines = file.readlines() 
        for line in lines: 
            if line.strip():                 
                key,value = line.split(":")          
                self.settings_list[key]=value.strip()          # Affecte la valeur à la clé correspondante dans le dictionnaire
        self.settings_list["Difficulty"]=int(self.settings_list["Difficulty"])
        self.settings_list["Sounds"]=int(self.settings_list["Sounds"])
        self.settings_list["Skin_Pack"]=int(self.settings_list["Skin_Pack"])

    def load_statistics(self):
        file = open(os.path.join(self.folder,'Files/stats.txt'), 'r')    #Charge le fichier de settings
        lines = file.readlines() 
        for line in lines: 
            if line.strip():                 
                key,value = line.split(":")          
                self.best_list[key]=value.strip()          # Affecte la valeur à la clé correspondante dans le dictionnaire

    def load_sprites(self):                                       # Va chercher les assets dans les fichiers du jeu
        pack=str(self.settings_list["Skin_Pack"])
        self.sprites_list = {
            "Player": pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/player.png")),
            "Player1": pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/player1.png")),
            "LaserShot": pygame.image.load(os.path.join(self.folder, "Assets/laser_shot.png")),
            "LaserShot2": pygame.image.load(os.path.join(self.folder, "Assets/laser_shot2.png")),
            "Asteroid1": pygame.image.load(os.path.join(self.folder, "Assets/asteroid1.png")),
            "Asteroid2": pygame.image.load(os.path.join(self.folder, "Assets/asteroid2.png")),
            "Asteroid3": pygame.image.load(os.path.join(self.folder, "Assets/asteroid3.png")),
            "Ennemy": pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/ennemy.png")),
            "Ennemy1": pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/ennemy1.png")),
            "Bonus1": pygame.image.load(os.path.join(self.folder, "Assets/bonuscoin.png")),
            "Bonus2": pygame.image.load(os.path.join(self.folder, "Assets/bonuslife.png")),
            "BlackHole" : pygame.image.load(os.path.join(self.folder, "Assets/Black_hole.png")),
            "UI_Menu": pygame.image.load(os.path.join(self.folder, "Assets/ui_menu.png")),
            "UI_Button": pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/ui_button.png")),
            "Pack_Banner" : pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+str((self.settings_list["Skin_Pack"]+1)%2)+"/pack_banner.png"))
        }
        self.title_font = pygame.font.Font(os.path.join(self.folder, 'Assets/title_font.ttf'), 48)
        self.text_font = pygame.font.Font(os.path.join(self.folder, 'Assets/text_font.ttf'), 32)
        self.button_font = pygame.font.Font(os.path.join(self.folder, 'Assets/text_font.ttf'), 26)
        self.mini_font = pygame.font.Font(os.path.join(self.folder, 'Assets/text_font.ttf'), 18)
        background=pygame.image.load(os.path.join(self.folder, "Assets/Pack_"+pack+"/background.png"))
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