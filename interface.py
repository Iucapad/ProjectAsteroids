import pygame

class GameInfo:

    def __init__(self):
        pass

    def DrawGameInfo(self,score,level,life):
        print("Score:",score, " Niveau:",level, " Vies:",life)

class MainMenu:
    
    def __init__(self,window):
        self.window=window
        clock = pygame.time.Clock()
        
        while True:
            self.window.fille((255,255,255))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            clock.tick(10)