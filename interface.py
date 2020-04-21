import pygame

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

    def draw_game_info(self,app,score,level,life):
        corner_text((" Niveau: "+str(level)),app.text_font,(255,255,255),app,1,25)
        corner_text((" Score: "+str(score)),app.text_font,(255,255,255),app,2,25)
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
        self.ui_button=app.sprites_list["UI_Button"] 

        while self.display:
            app.window.blit(app.background,(0,0)) 
            draw_text("Menu principal",app.title_font,(255,255,255),app,self.h_align,100)
            draw_text("Meilleur score: "+str(app.best_score),app.text_font,(255,255,255),app,self.h_align,150) 
                       
            app.window.blit(self.ui_button,self.button1)
            app.window.blit(self.ui_button,self.button2)
            app.window.blit(self.ui_button,self.button3)
            app.window.blit(self.ui_button,self.statsbtn)
            draw_text("Jouer",app.button_font,(127,0,0),app,self.h_align,350)
            draw_text("Options",app.button_font,(127,0,0),app,self.h_align,425)
            draw_text("Quitter",app.button_font,(127,0,0),app,self.h_align,500)
            draw_text("Statistiques",app.button_font,(127,0,0),app,app.window_size[0]-110,35)

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
        self.back_button=add_button(self.h_align,550,200,50) 
        self.background=pygame.Rect(self.h_align-320,self.v_align-85,640,170)
        self.item1=pygame.Rect(self.h_align-310,self.v_align-75,200,150)
        self.item2=pygame.Rect(self.h_align-100,self.v_align-75,200,150)
        self.item3=pygame.Rect(self.h_align+110,self.v_align-75,200,150)
        self.ui_button=game.app.sprites_list["UI_Button"] 

        while self.display:
            if (self.top<720):
                self.top+=36
                pygame.draw.rect(game.app.window, (10,10,10),pygame.Rect(self.h_align-330,720-self.top,660,720)) 
            else: 
                pygame.draw.rect(game.app.window, (45,45,45),self.background) 
                pygame.draw.rect(game.app.window, (10,10,10),self.item1) 
                pygame.draw.rect(game.app.window, (10,10,10),self.item2)
                pygame.draw.rect(game.app.window, (10,10,10),self.item3) 
                draw_text("BOUTIQUE",game.app.text_font,(255,255,255),game.app,game.app.window_size[0]/2,100)
                draw_text("Améliorations disponibles",game.app.text_font,(255,255,255),game.app,game.app.window_size[0]/2,self.v_align-110)
                game.app.window.blit(self.ui_button,self.back_button)
                draw_text("Passer",game.app.button_font,(127,0,0),game.app,self.h_align,575)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.back_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
            self.click=False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(120)

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
        self.ui_button=app.sprites_list["UI_Button"]
        self.settings_list = {
            "Difficulty":0,
            "Player_Name":"playername",
            "Sounds":True,
            "Skin_Pack":0
        }   

        self.back_button=add_button(self.h_align,550,200,50)
        self.difficulty_button=add_button(self.h_align,200,100,50) 
        self.sounds_button=add_button(self.h_align,300,100,50) 
        self.skin_button=add_button(self.h_align,400,100,50)   

        while self.display:
            app.window.blit(app.background,(0,0)) 
            draw_text("Options",app.title_font,(255,255,255),app,app.window_size[0]/2,100)
            pygame.draw.rect(app.window, (10,10,10),self.difficulty_button)
            if (self.settings_list["Sounds"]):
                pygame.draw.rect(app.window, (10,10,10),self.sounds_button)
            else:
                pygame.draw.rect(app.window, (45,45,45),self.sounds_button)
            pygame.draw.rect(app.window, (10,10,10),self.skin_button)
            app.window.blit(self.ui_button,self.back_button)
            draw_text("Retour",app.button_font,(127,0,0),app,self.h_align,575)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.difficulty_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Difficulty"]+=1
                    self.settings_list["Difficulty"]%=3
                    print (self.settings_list["Difficulty"])
            if (self.sounds_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Sounds"]= not (self.settings_list["Sounds"])
            if (self.skin_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.settings_list["Skin_Pack"]+=1
                    self.settings_list["Skin_Pack"]%=2 #A mettre le nombre de packs de skins
            if (self.back_button.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
            self.click=False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click=True
            pygame.display.update()
            clock.tick(30)