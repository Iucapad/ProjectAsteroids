import pygame

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

class MainMenu:
    
    def __init__(self,app):
        self.value=0
        clock = pygame.time.Clock()
        self.display=True
        button1 = self.create_button(100, 100, 250, 80, 'Click me!', self.test())
        button2 = self.create_button(100, 200, 250, 80, 'Me too!', self.test1())    

        while self.display:
            app.window.fill((45,45,90))
            DrawText("Menu principal",menu_font,(255,255,255),app,app.window_size[0]/2,100)
            DrawText("Meilleur score: x",text_font,(255,255,255),app,app.window_size[0]/2,125)
            
            app.window.blit(button1,(10,10))
            button_list = [button1, button2]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.display=False
                    app.StartGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                    if event.button == 1:
                        for button in button_list:
                        # `event.pos` is the mouse position.
                            if button['rect'].collidepoint(event.pos):
                            # Increment the number by calling the callback
                            # function in the button list.
                                button['callback']()
            pygame.display.update()
            clock.tick(30)

    def create_button(self,x, y, w, h, text, callback):
    # The button is a dictionary consisting of the rect, text,
    # text rect, color and the callback function.
        button_rect = pygame.Rect(x, y, w, h)
        text_obj = text_font.render(text,1,(10,10,10))
        text_rect = text_obj.get_rect(center=button_rect.center)
        button = {
            'rect': button_rect,
            'text': text_font,
            'text rect': text_rect,
            'color': (255,255,255),
            'callback': callback,
            }
        return button

    def test(self):
        pass
    def test1(self):
        pass