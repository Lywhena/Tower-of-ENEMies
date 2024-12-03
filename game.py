import pygame
import sys
import random
import cv2
from enemy import Enemy
from button import Button
from menu import Menu  

# Inicializando o Pygame
pygame.init()

# Definindo constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 20
MARGIN = 10

# Configurando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quiz Game")

# Vídeos de conclusão
CONCLUSION_VIDEO = "./Cutscenes/fim.mp4"
CONCLUSION_AUDIO = "./Cutscenes/fim.mp3"

# Função para reproduzir o vídeo de conclusão
def play_conclusion_video(video_path, audio_path):
    """Reproduz vídeo de conclusão com áudio sincronizado."""
    # Iniciar mixer para reproduzir o áudio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Configurar vídeo com OpenCV
    cap = cv2.VideoCapture(video_path)

    # Loop para reproduzir vídeo
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:  # Fim do vídeo
            break

        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # Corrigir orientação (espelhar verticalmente)
        frame = cv2.flip(frame, 1)
        # Converter frame do OpenCV (BGR) para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Criar uma superfície do Pygame a partir do frame
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Exibir o frame no Pygame
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Verificar eventos (fechar a janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        # Controlar a taxa de quadros
        pygame.time.delay(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

    cap.release()
    pygame.mixer.music.stop()

# Função para reproduzir vídeo com som
def play_video_with_sound(video_path, audio_path):
    """Reproduz vídeo com áudio sincronizado."""
    # Iniciar mixer para reproduzir o áudio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Configurar vídeo com OpenCV
    cap = cv2.VideoCapture(video_path)

    # Loop para reproduzir vídeo
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:  # Fim do vídeo
            break

        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # Corrigir orientação (espelhar verticalmente)
        frame = cv2.flip(frame, 1)
        # Converter frame do OpenCV (BGR) para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Criar uma superfície do Pygame a partir do frame
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Exibir o frame no Pygame
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Verificar eventos (fechar a janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        # Controlar a taxa de quadros
        pygame.time.delay(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

    cap.release()
    pygame.mixer.music.stop()

# Classe para o Jogo
class Game:
    def __init__(self):
        self.enemies = [
            Enemy("Inimigo 1", "./Enemies/inimigo1.png", "./Backgrounds/background1.png", [
                {"question": "O movimento originado da obra Abaporu pretendia se apropriar:", "options": ["AAA Da cultura europeia, para originar algo brasileiro.", "Da arte clássica, para copiar o seu ideal de beleza", "Do ideário republicano, para celebrar a modernidade.", "Das técnicas artísticas nativas, para consagrar sua tradição.", "Da herança colonial brasileira, Para preservar sua identidade."], "answer": 0},
                {"question": "Inovando os padrões estéticos de sua época, a obra de Pablo Picasso foi produzida utilizando características que:", "options": ["AAA Explora a sobreposição de planos geométricos e fragmentos de objetos.", "Busca uma composição reduzida e seus elementos primários de forma.", "Valoriza a composição dinâmica para representar movimento.", "Agrega elementos da publicidade em suas composições.", "Dispensa a representação da realidade."], "answer": 0},
                {"question": "Colcha de retalhos representa a essência do mural e convida o público a:", "options": ["AAA Apreciar a estética do cotidiano.", "Interagir com os elementos da composição.", "Refletir sobre elementos do inconsciente do artista.", "Reconhecer a estética clássica das formas.", "Contemplar a obra por meio da movimentação física."], "answer": 0}
            ]),
            Enemy("Inimigo 2", "./Enemies/inimigo2.png", "./Backgrounds/background2.png", [
                {"question": "O que, de acordo com Nietzsche, caracteriza o surgimento da filosofia entre os gregos?", "options": ["AAA A necessidade de buscar, de forma racional, a causa primeira das coisas existentes.", "A ambição de expor, de maneira metódica, as diferenças entre as coisas.", "A tentativa de justificar, a partir de elementos empíricos, o que existe no real.", "O desejo de explicar, usando metáforas, a origem dos seres e das coisas.", "O impulso para transformar, mediante justificativas, os elementos sensíveis em verdades racionais."], "answer": 0},
                {"question": "O que é a alienação para Karl Marx?", "options": ["AAA O trabalhador é desumanizado e separado de seu trabalho.", "O trabalhador se torna livre no capitalismo.", "A alienação acontece apenas na religião.", "O trabalhador é consciente de sua exploração.", "A aceitação passiva do trabalhador das condições de exploração no sistema feudal"], "answer": 0},
                {"question": "O que Sócrates quis dizer com só sei que nada sei?", "options": ["AAA Reconhecimento da ignorância e importância do questionamento.", "Afirmava que o conhecimento humano é impossível.", "Defendia que só filósofos possuem sabedoria.", "Ele acreditava que o conhecimento era transmitido pela experiência sensorial.", "Ele rejeitava a possibilidade de se alcançar qualquer tipo de sabedoria."], "answer": 0}
            ]),
            Enemy("Inimigo 3", "./Enemies/inimigo3.png", "./Backgrounds/background3.png", [
                {"question": "A referida lei das doze tabuas foi um marco na luta por direitos na Roma Antiga, pois possibilitou que os plebeus:", "options": ["AAA Reivindicassem as mudanças sociais com base no conhecimento das leis.", "Ampliassem a participação política nos cargos políticos públicos.", "Conquistassem a possibilidade de casamento com os patrícios.", "Exercessem a prática da escravidão sobre seus devedores.", "Modificassem a estrutura agrária assentada no latifúndio."], "answer": 0},
                {"question": "A Guerra do Paraguai teve consequências políticas importantes para o Brasil, pois:", "options": ["AAA Representou a afirmação do Exército Brasileiro como um ator político de primeira ordem.", "Confirmou a conquista da hegemonia brasileira sobre a Bacia Platina.", "Concretizou a emancipação dos escravos negros.", "Incentivou a adoção de um regime constitucional monárquico.", "Solucionou a crise financeira, em razão das indenizações recebidas."], "answer": 0},
                {"question": "A referida lei foi um marco na luta por direitos na Roma Antiga, pois possibilitou que os plebeus:", "options": ["AAA Reivindicassem as mudanças sociais com base no conhecimento das leis.", "Ampliassem a participação política nos cargos políticos públicos.", "Conquistassem a possibilidade de casamento com os patrícios.", "Exercessem a prática da escravidão sobre seus devedores.", "Modificassem a estrutura agrária assentada no latifúndio."], "answer": 0}
            ]),
            Enemy("Inimigo 4", "./Enemies/inimigo4.png", "./Backgrounds/background4.png", [
                {"question": "Das opções abaixo, a que não representa um impacto ambiental é:", "options": ["AAA Mobilidade urbana", "Poluição sonora", "Desertificação", "Assoreamento dos rios", "Chuva ácida"], "answer": 0},
                {"question": "As geleiras da Groenlândia sofreram e sofrem impactos, resultantes do:", "options": ["AAA Aquecimento global.", "Inversão térmica.", "Erosão eólica.", "Chuva ácida.", "Ilha de calor."], "answer": 0},
                {"question": "A dinâmica de transformação das cidades tende a apresentar como conseqüência a expansão das áreas periféricas pelo:", "options": ["AAA Crescimento da população urbana e aumento da especulação imobiliária.", "Direcionamento maior do fluxo de pessoas, devido à existência de um grande número de serviços.", "Delimitação de áreas para uma ocupação organizada do espaço físico, melhorando a qualidade de vida.", "Implantação de políticas públicas que promovem a moradia e o direito à cidade aos seus moradores.", "Reurbanização de moradias nas áreas centrais, mantendo o trabalhador próximo ao seu empregoto."], "answer": 0}
            ]),
            Enemy("Boss", "./Enemies/boss.png", "./Backgrounds/background5.png", [
                {"question": "Do ponto de vista da ciência moderna, a descrição dos “quatro elementos” feita por Platão corresponde ao conceito de", "options": ["AAA Fase da matéria.", "Elemento químico.", "Força fundamental.", "Partícula elementar.", "Lei da natureza."], "answer": 0},
                {"question": "O gás natural é uma fonte de energia fóssil composta principalmente por:", "options": ["AAA Metano.", "Propano.", "Butano.", "Etano.", "Carbono."], "answer": 0},
                {"question": "A tecnologia redutora de ruído CR utilizada na produção de fones de ouvido baseia-se em qual fenômeno ondulatório?", "options": ["AAA Interferência.", "Absorção.", "Polarização.", "Reflexão.", "Difração."], "answer": 0},
                {"question": "Um contribuinte vende por R$34 mil um lote de ações que custou R$26mil, paga de Imposto de Renda à Receita Federal(15%):", "options": ["AAA R$ 1 200,00.", "R$ 2 100,00.", "R$ 900,00.", "R$ 3 900,00.", "R$ 5 100,00."], "answer": 0}
            ])
        ]

        # Adiciona vídeos de transição
        self.transitions = [
            ("./Transitions/sec.mp4", "./Transitions/sec.mp3"),
            ("./Transitions/ter.mp4", "./Transitions/ter.mp3"),
            ("./Transitions/quar.mp4", "./Transitions/quar.mp3"),
            ("./Transitions/enemus.mp4", "./Transitions/enemus.mp3")
        ]
        self.current_enemy_index = 0
        self.transition_displaying = False
        self.transition_start_time = 0
        self.show_question = True
        self.buttons = []

        # Randomizando as perguntas de cada inimigo
        for enemy in self.enemies:
            enemy.randomize_questions()

    def get_current_enemy(self):
        return self.enemies[self.current_enemy_index]

    def next_enemy(self):
        if self.current_enemy_index < len(self.enemies) - 1:
            self.current_enemy_index += 1
            return True
        return False

    def reset_game(self):
        self.current_enemy_index = 0
        for enemy in self.enemies:
            enemy.reset_questions()

    def start_transition(self):
        self.transition_displaying = True
        self.transition_start_time = pygame.time.get_ticks()

    def update(self):
        if self.transition_displaying:
            # Verifica se passou 1 segundo desde o início da transição
            if pygame.time.get_ticks() - self.transition_start_time > 1000:
                self.transition_displaying = False
                self.next_enemy()  # Passa para o próximo inimigo após a transição

# Função principal do jogo
def main():
    # Exibe o menu inicial
    menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, './Backgrounds/background.jpeg', './Audio/thunder.wav')
    menu.show()
    
    # Após o menu, reproduz o vídeo de introdução e inicia o jogo
    play_video_with_sound("./Cutscenes/vid.mp4", "./Cutscenes/vid_audio.mp3")
    play_video_with_sound("./Transitions/prim.mp4", "./Transitions/prim.mp3")  # Novo vídeo de transição

    # Depois disso, inicie o jogo normalmente
    game = Game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, FONT_SIZE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in game.buttons:
                    if button.is_clicked(event):
                        current_question = game.get_current_enemy().get_current_question()
                        if current_question['options'].index(button.text) == current_question['answer']:
                            print("Resposta correta!")
                            if game.get_current_enemy().next_question():
                                game.show_question = True
                            else:
                                if game.current_enemy_index == len(game.enemies) - 1:  # Verifica se é o Boss e se é a última pergunta
                                    play_conclusion_video(CONCLUSION_VIDEO, CONCLUSION_AUDIO)  # Reproduz vídeo de conclusão
                                    pygame.quit()  # Fecha o Pygame
                                    sys.exit()  # Encerra o programa
                                else:
                                    game.start_transition()  # Inicia a transição
                        else:
                            print("Resposta errada! Reiniciando o jogo...")
                            game.reset_game()
                            game.show_question = True

        screen.fill(WHITE)
        current_enemy = game.get_current_enemy()

        if game.transition_displaying:
            transition_video, transition_audio = game.transitions[game.current_enemy_index]
            play_video_with_sound(transition_video, transition_audio)  # Reproduz vídeo de transição
        else:
            screen.blit(current_enemy.background, (0, 0))
            draw_text(f"Inimigo: {current_enemy.name}", font, screen, -100, -100)
            screen.blit(current_enemy.image, (300, 10))

            if game.show_question:
                question = current_enemy.get_current_question()
                draw_text(question['question'], font, screen, MARGIN, SCREEN_HEIGHT - 180)
                game.buttons = []

                for i, option in enumerate(question['options']):
                    button = Button(option, 20, SCREEN_HEIGHT - 160 + (i * 32), 750, 30, font)
                    game.buttons.append(button)
                    button.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        game.update()

# Função para desenhar texto
def draw_text(text, font, surface, x, y):
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(topleft=(x, y))
    surface.blit(text_surf, text_rect)

# Rodar o jogo
if __name__ == "__main__":
    main()