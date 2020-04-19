import pygame

import main

class GameInfo:

    def __init__(self):
        pass

    def DrawGameInfo(self,score,level,life):
        print("Score:",score, " Niveau:",level, " Vies:",life)

class MainMenu:
    
    def __init__(self,window):
        self.window=window
        self.value=0
        clock = pygame.time.Clock()

        while True:
            self.window.fill((45,45,90))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    main.App.StartGame()
            pygame.display.update()
            clock.tick(30)
