import pygame

pygame.init()

menu_font=pygame.font.SysFont(None, 40, bold=True, italic=False)
text_font=pygame.font.SysFont(None, 30, bold=False, italic=False)

def DrawText(text,font,color,app,x,y):
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    app.window.blit(text_obj,text_rect)

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

        while self.display:
            app.window.fill((45,45,90))
            DrawText("Menu principal",menu_font,(255,255,255),app,app.window_size[0]/2,100)
            DrawText("Meilleur score: x",text_font,(255,255,255),app,app.window_size[0]/2,125)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.display=False
                    app.StartGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass
            pygame.display.update()
            clock.tick(30)
