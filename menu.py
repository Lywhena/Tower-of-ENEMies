import pygame

class Menu:
    def __init__(self, width, height, background, sound_file):
        self.width = width
        self.height = height
        self.background = pygame.image.load(background)
        self.sound = pygame.mixer.Sound(sound_file)
        self.running = True

    def show(self):
        self.sound.play(-1)  # Toca o som em loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Usuário deseja fechar
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:  # Qualquer tecla para iniciar o jogo
                    self.running = False  # Sai do menu
            screen.blit(self.background, (0, 0))  # Exibe a imagem de fundo
            pygame.display.flip()
        self.sound.stop()  # Para o som quando o menu encerra


# Configuração inicial da tela e Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu do Jogo")