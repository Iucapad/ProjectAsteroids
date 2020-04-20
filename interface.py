import pygame

pygame.init()

menu_font=pygame.font.SysFont(None, 50, bold=True, italic=False)
text_font=pygame.font.SysFont(None, 30, bold=False, italic=False)
button_font=pygame.font.SysFont(None, 40, bold=False, italic=False)

def DrawText(text,font,color,app,x,y):
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    app.window.blit(text_obj,text_rect)

def AddButton(left,top,width,height):
    return pygame.Rect(left-width/2,top,width,height)

def CornerText(text,font,color,app,corner,padding):
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

    def DrawGameInfo(self,app,score,level,life):
        CornerText((" Niveau: "+str(level)),text_font,(255,255,255),app,1,25)
        CornerText((" Score: "+str(score)),text_font,(255,255,255),app,2,25)
        CornerText((" Vies: "+str(life)),text_font,(255,255,255),app,3,25)

class PauseMenu:
    def __init__(self,app):
        clock = pygame.time.Clock()
        self.display=True        

        while self.display:
            DrawText("PAUSE",menu_font,(255,255,255),app,app.window_size[0]/2,100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.display=False
                        app.state="game"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass
            pygame.display.update()
            clock.tick(30)

class MainMenu:
    def __init__(self,app):
        clock = pygame.time.Clock()
        self.display=True
        self.click=False
        self.h_align=app.window_size[0]/2
        AddButton(self.h_align,300,200,50)
        self.button1=AddButton(self.h_align,325,200,50)
        self.button2=AddButton(self.h_align,400,200,50)   
        self.button3=AddButton(self.h_align,475,200,50)   

        while self.display:
            app.window.blit(app.background,(0,0)) 
            DrawText("Menu principal",menu_font,(255,255,255),app,self.h_align,100)
            DrawText("Meilleur score: x",text_font,(255,255,255),app,self.h_align,125)            
            pygame.draw.rect(app.window, (10,0,16),self.button1)
            pygame.draw.rect(app.window, (10,0,16),self.button2)
            pygame.draw.rect(app.window, (10,0,16),self.button3)
            DrawText("Jouer",button_font,(255,255,255),app,self.h_align,350)
            DrawText("Options",button_font,(255,255,255),app,self.h_align,425)
            DrawText("Quitter",button_font,(255,255,255),app,self.h_align,500)

            mouse_x,mouse_y=pygame.mouse.get_pos()
            if (self.button1.collidepoint(mouse_x,mouse_y)):
                if (self.click):
                    self.display=False
                    app.StartGame()
            elif (self.button2.collidepoint(mouse_x,mouse_y)):
                pass
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

class Shop:
    def __init__(self, game):
        self.game = game

class GameIntro:
    def __init__(self, app):
        pass

class Settings:
    def __init__(self, app):
        self.app = app