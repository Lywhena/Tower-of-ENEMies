import pygame
import sys

class Menu:
    def __init__(self, width, height, background, sound_file):
        self.width = width
        self.height = height
        self.background= pygame.image.load(background)
        self.sound = pygame.mixer.Sound(sound_file)
        self.running = True

    def show(self):
        self.sound.play(-1)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.running = False
            screen.blit(self.background, (0, 0))
            pygame.display.flip()
        self.sound.stop() 
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu do Jogo")
menu = Menu(WIDTH, HEIGHT, 'background.jpeg', 'thunder.wav')

menu.show()
pygame.quit()