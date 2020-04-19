import pygame

import main

class GameInfo:

    def __init__(self):
        pass

    def DrawGameInfo(self,score,level,life):
        print("Score:",score, " Niveau:",level, " Vies:",life)

class MainMenu:
    
    def __init__(self,app):
        self.value=0
        clock = pygame.time.Clock()
        self.display=True

        while self.display:
            app.window.fill((45,45,90))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.display=False
                    app.StartGame()
            pygame.display.update()
            clock.tick(30)
