import os.path
import pygame
import random

pygame.init()


def draw_text(text,font,color,app,x,y):
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    app.window.blit(text_obj,text_rect)

def add_button(left,top,width,height):
    return pygame.Rect(left-width/2,top,width,height)

def corner_text(text,font,color,app,corner,padding):
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    if corner==1:
        text_rect.topleft = (padding,padding)
    elif corner==2:
        text_rect.topright = (app.window_size[0]-padding,padding)
    elif corner==3:
        text_rect.bottomright = (app.window_size[0]-padding,app.window_size[1]-padding)
    elif corner==4:
        text_rect.bottomleft = (padding,app.window_size[1]-padding)
    app.window.blit(text_obj,text_rect)

class GameInfo:
    def __init__(self,app):
        self.app=app

    def draw_game_info(self,app,score,coins,level,life):
        corner_text((" Niveau: "+str(level)),app.text_font,(255,255,255),app,1,25)
        corner_text((" Score: "+str(score)),app.text_font,(255,255,255),app,2,25)
        corner_text((str(coins))+" $",app.text_font,(255,255,255),app,1,60)
        corner_text((" Vies: "+str(life)),app.text_font,(255,255,255),app,3,25)

class PauseMenu:
    def __init__(self,app):
        clock = pygame.time.Clock()
        self.display=True
        self.click=False
        self.top=0
        self.h_align=app.window_size[0]/2
        self.v_align=app.window_size[1]/2
        self.ui_menu=app.sprites_list["UI_Menu"]
        self.ui_button=app.sprites_list["UI_Button"]
        self.resume=add_button(self.h_align,self.v_align-30,200,50)
        self.quit=add_button(self.h_align,self.v_align+30,200,50)

        while self.display:
            if (self.top<720):
                self.top+=36
                app.window.blit(self.ui_menu,pygame.Rect(self.h_align-250,720-self.top,500,720)) 
            else:
                draw_text("PAUSE",app.text_font,(255,255,255),app,app.window_size[0]/2,100)
                app.window.blit(self.ui_button,self.resume)
                app.window.blit(self.ui_button,self.quit)
                draw_text("Reprendre",app.button_font,(127,0,0),app,self.h_align,self.v_align-5)
                draw_text("Quitter",app.button_font,(127,0,0),app,self.h_align,self.v_align+55)
            
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.resume.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    app.state="game"
            elif (self.quit.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    app.state="menu"
                    app.menu=MainMenu(app)                    
            self.click=False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.display=False
                        app.state="game"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(120)

class GameOver:
    def __init__(self,game):
        clock = pygame.time.Clock()
        self.display=True
        self.click=False
        self.top=0
        self.h_align=game.app.window_size[0]/2
        self.v_align=game.app.window_size[1]/2
        self.ui_menu=game.app.sprites_list["UI_Menu"]
        self.ui_button=game.app.sprites_list["UI_Button"]
        self.resume=add_button(self.h_align,self.v_align-30,200,50)
        self.quit=add_button(self.h_align,self.v_align+30,200,50)

        while self.display:
            game.app.window.fill((0,0,0))
            if (self.top<720):
                self.top+=36
                game.app.window.blit(self.ui_menu,pygame.Rect(self.h_align-250,720-self.top,500,720)) 
            else:
                game.app.window.blit(self.ui_menu,pygame.Rect(self.h_align-250,0,500,720)) 
                draw_text("GAME OVER",game.app.text_font,(255,255,255),game.app,game.app.window_size[0]/2,100)
                game.app.window.blit(self.ui_button,self.resume)
                game.app.window.blit(self.ui_button,self.quit)
                draw_text("Recommencer",game.app.button_font,(127,0,0),game.app,self.h_align,self.v_align-5)
                draw_text("Quitter",game.app.button_font,(127,0,0),game.app,self.h_align,self.v_align+55)
            
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.resume.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    game.app.start_game()
            elif (self.quit.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    game.app.state="menu"
                    game.app.menu=MainMenu(game.app)                    
            self.click=False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.display=False
                        app.state="game"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(120)

class MainMenu:
    def __init__(self,app):
        clock = pygame.time.Clock()
        self.display=True
        self.click=False
        self.h_align=app.window_size[0]/2
        self.button1=add_button(self.h_align,325,200,50)
        self.button2=add_button(self.h_align,400,200,50)   
        self.button3=add_button(self.h_align,475,200,50)
        self.statsbtn=add_button(app.window_size[0]-110,10,200,50)

        while self.display:
            self.ui_button=app.sprites_list["UI_Button"]
            app.window.blit(app.background,(0,0)) 
            draw_text("Menu principal",app.title_font,(255,255,255),app,self.h_align,100)
            try:
                draw_text("Meilleur score: "+str(app.best_list[app.settings_list["Player_Name"]]),app.text_font,(255,255,255),app,self.h_align,150) 
            except:
                app.best_list[app.settings_list["Player_Name"]]=0
            app.window.blit(self.ui_button,self.button1)
            app.window.blit(self.ui_button,self.button2)
            app.window.blit(self.ui_button,self.button3)
            app.window.blit(self.ui_button,self.statsbtn)
            draw_text("Jouer",app.button_font,(127,0,0),app,self.h_align,350)
            draw_text("Options",app.button_font,(127,0,0),app,self.h_align,425)
            draw_text("Quitter",app.button_font,(127,0,0),app,self.h_align,500)
            draw_text("Classement",app.button_font,(127,0,0),app,app.window_size[0]-110,35)
            draw_text(app.settings_list["Player_Name"],app.button_font,(127,0,0),app,110,35)
            draw_text("Asteroids ©2020 HeH, developed by Vitali L., Belga D., De Troch T., Lambrecht B., Vlassembrouck M.",app.mini_font,(255,255,255),app,app.window_size[0]/2,app.window_size[1]-35)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.button1.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    app.start_game()
            elif (self.button2.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings=Settings(app)
            elif (self.button3.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    pygame.quit()
            self.click=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(30)

class ViewStatistics:

    def __init__(self,player):
        self.player=player
        clock = pygame.time.Clock()
        self.display=True
        self.click=False

        while self.display:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.close.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    pass
            self.click=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(30)

class Shop:

    def __init__(self, game):
        self.game = game
        clock = pygame.time.Clock()
        self.display=True        
        self.click=False
        self.top=0
        self.h_align=game.app.window_size[0]/2
        self.v_align=game.app.window_size[1]/2
        self.ui_menu=game.app.sprites_list["UI_Menu"]
        self.back_button=add_button(self.h_align,550,200,50) 
        self.background=pygame.Rect(self.h_align-240,self.v_align-85,490,170)
        self.item1=pygame.Rect(self.h_align-230,self.v_align-75,150,150)
        self.item2=pygame.Rect(self.h_align-70,self.v_align-75,150,150)
        self.item3=pygame.Rect(self.h_align+90,self.v_align-75,150,150)
        self.ui_button=game.app.sprites_list["UI_Button"]
        self.items={
            0:"5 Vies",
            1:"Stabilité ++",
            2:"Tir ++",
            3:"Bouclier"
        }
        self.prices=[50,100,250,1000]
        self.generate_sale()

        while self.display:
            if (self.top<720):
                self.top+=36
                game.app.window.blit(self.ui_menu,pygame.Rect(self.h_align-245,720-self.top,490,720)) 
            else: 
                pygame.draw.rect(game.app.window, (45,45,45),self.background) 
                pygame.draw.rect(game.app.window, (10,10,10),self.item1) 
                pygame.draw.rect(game.app.window, (10,10,10),self.item2)
                pygame.draw.rect(game.app.window, (10,10,10),self.item3)
                draw_text(self.items[self.item_1],game.app.button_font,(127,0,0),game.app,self.item1.x+75,self.item1.y+15)
                draw_text(self.items[self.item_2],game.app.button_font,(127,0,0),game.app,self.item2.x+75,self.item2.y+15)
                draw_text(self.items[self.item_3],game.app.button_font,(127,0,0),game.app,self.item3.x+75,self.item3.y+15)
                draw_text(str(self.prices[self.item_1]),game.app.button_font,(127,0,0),game.app,self.item1.x+75,self.item1.y+130)
                draw_text(str(self.prices[self.item_2]),game.app.button_font,(127,0,0),game.app,self.item2.x+75,self.item2.y+130)
                draw_text(str(self.prices[self.item_3]),game.app.button_font,(127,0,0),game.app,self.item3.x+75,self.item2.y+130)
                draw_text("BOUTIQUE",game.app.text_font,(255,255,255),game.app,game.app.window_size[0]/2,100)
                draw_text("Améliorations disponibles",game.app.text_font,(255,255,255),game.app,game.app.window_size[0]/2,self.v_align-140)
                draw_text("Vous avez "+str(game.coins)+"$",game.app.button_font,(255,255,255),game.app,game.app.window_size[0]/2,self.v_align-105)
                game.app.window.blit(self.ui_button,self.back_button)
                draw_text("Passer",game.app.button_font,(127,0,0),game.app,self.h_align,575)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.back_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
            if (self.item1.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    if (game.coins>self.prices[self.item_1]):
                        self.transaction(self.item_1)
                        print("Achat de "+str(self.items[self.item_1]+"pour un prix de "+str(self.prices[self.item_1])))
                        self.display=False
                    else:
                        print('t pauvre')
            if (self.item2.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    if (game.coins>self.prices[self.item_2]):
                        self.transaction(self.item_2)
                        self.display=False
                    else:
                        print('t pauvre')
            if (self.item3.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    if (game.coins>self.prices[self.item_3]):
                        self.transaction(self.item_3)
                        self.display=False
                    else:
                        print('t pauvre')
            self.click=False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(120)

    def transaction(self,item):
        self.game.coins-=self.prices[item]
        if (item==0):            
            self.game.player_space_ship.life+=5
        elif (item==1):
            if (self.game.player_space_ship.deceleration==0.07):
                self.game.player_space_ship.deceleration=0.09
            elif (self.game.player_space_ship.deceleration==0.09):
                self.game.player_space_ship.deceleration=0.11
            elif (self.game.player_space_ship.deceleration==0.11):
                self.game.player_space_ship.deceleration=0.13
        elif (item==2):
            if (self.game.player_space_ship.shoot_rate>0.05):
                self.game.player_space_ship.shoot_rate-=0.05
        elif (item==3):
            self.game.player_space_ship.is_invincible = 1800

    def generate_sale(self):
        it1=random.randint(0,3)
        it2=random.randint(0,3)
        it3=random.randint(0,3)
        if (it3!=it1 and it3!=it2 and it1!=it2 and self.is_available(it1) and self.is_available(it2) and self.is_available(it3)):
            self.item_1=it1
            self.item_2=it2
            self.item_3=it3
        else:
            self.generate_sale()

    def is_available(self,item):
        if (item==1):
            return not self.game.player_space_ship.deceleration==0.13
        elif (item==2):
            print(self.game.player_space_ship.shoot_rate)
            return not self.game.player_space_ship.shoot_rate==0.05 #todo fix
        else:
            return True

class GameIntro:

    def __init__(self, app):
        pass

class Settings:

    def __init__(self, app):
        self.app = app
        clock = pygame.time.Clock()
        self.display=True
        self.click=False
        self.h_align=app.window_size[0]/2
        self.settings_list = app.settings_list
        self.back_button=add_button(self.h_align,550,200,50)
        self.text=add_button(self.h_align,155,200,40)
        self.textbox=add_button(self.h_align,190,200,5)
        self.active=False
        self.difficulty_button=add_button(self.h_align,250,200,50) 
        self.sounds_button=add_button(self.h_align,350,200,50) 
        self.skin_button=add_button(self.h_align,450,200,50)   

        while self.display:
            self.ui_button=app.sprites_list["UI_Button"]
            self.pack_banner=app.sprites_list["Pack_Banner"]
            app.window.blit(app.background,(0,0)) 
            draw_text("Options",app.title_font,(255,255,255),app,app.window_size[0]/2,100)
            if (self.active):
                pygame.draw.rect(app.window, (45,0,0),self.textbox)
            else:
                pygame.draw.rect(app.window, (127,0,0),self.textbox)
            pygame.draw.rect(app.window, (10,10,10),self.difficulty_button)
            pygame.draw.rect(app.window, (10,10,10),self.sounds_button)
            app.window.blit(self.pack_banner,self.skin_button)
            app.window.blit(self.ui_button,self.back_button)
            draw_text(self.settings_list["Player_Name"],app.button_font,(255,255,255),app,self.h_align,175)
            draw_text("Difficulté",app.button_font,(255,255,255),app,self.h_align,235)
            if (self.settings_list["Difficulty"]==0):
                draw_text("Facile",app.button_font,(127,0,0),app,self.h_align,275)
            elif (self.settings_list["Difficulty"]==1):
                draw_text("Normal",app.button_font,(127,0,0),app,self.h_align,275)
            elif (self.settings_list["Difficulty"]==2):
                draw_text("Difficile",app.button_font,(127,0,0),app,self.h_align,275)
            draw_text("Son",app.button_font,(255,255,255),app,self.h_align,335)
            if (self.settings_list["Sounds"]==0):
                draw_text("Sans",app.button_font,(127,0,0),app,self.h_align,375)
            elif (self.settings_list["Sounds"]==1):
                draw_text("Avec",app.button_font,(127,0,0),app,self.h_align,375)
            draw_text("Pack de skins",app.button_font,(255,255,255),app,self.h_align,435)
            draw_text("Retour",app.button_font,(127,0,0),app,self.h_align,575)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.text.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.active=True
            if (self.difficulty_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Difficulty"]+=1
                    self.settings_list["Difficulty"]%=3
                    self.save_options()
            if (self.sounds_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Sounds"]+=1
                    self.settings_list["Sounds"]%=2
                    self.save_options()
            if (self.skin_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Skin_Pack"]+=1
                    self.settings_list["Skin_Pack"]%=2 #A mettre le nombre de packs de skins
                    self.save_options()
                    self.app.load_sprites()
            if (self.back_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.app.load_statistics()
                    self.save_options()
                    self.display=False
            self.click=False            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.active=False
                        self.click=True
                elif event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.active=False
                        elif event.key == pygame.K_BACKSPACE:
                            self.settings_list["Player_Name"] = self.settings_list["Player_Name"][:-1]
                        else:
                            self.settings_list["Player_Name"] += event.unicode
            pygame.display.update()
            clock.tick(30)

    def save_options(self):
        if self.settings_list["Player_Name"]=="":
            self.settings_list["Player_Name"]="Joueur"
        try:
            f = open(os.path.join(self.app.folder,"Files/settings.txt"),"w")
            f.write(
                "Player_Name:"+str(self.settings_list["Player_Name"])+"\nDifficulty:"+str(self.settings_list["Difficulty"])+"\nSounds:"+str(self.settings_list["Sounds"])+"\nSkin_Pack:"+str(self.settings_list["Skin_Pack"])
            )
            f.close()
        except:
            print("Erreur de sauvegarde")