import pygame
import random

class Enemy:
    def __init__(self, name, image_path, background_path, questions):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.background = pygame.image.load(background_path)
        self._questions = questions
        self.current_question_index = 0
        
    def get_current_question(self):
        return self._questions[self.current_question_index]

    def next_question(self):
        if self.current_question_index < len(self._questions) - 1:
            self.current_question_index += 1
            return True
        return False

    def reset_questions(self):
        self.current_question_index = 0

    def randomize_questions(self):
        random.shuffle(self._questions)
        for question in self._questions:
            self._randomize_options(question)

    def _randomize_options(self, question):
        correct_answer = question['options'][question['answer']]
        random.shuffle(question['options'])
        question['answer'] = question['options'].index(correct_answer)
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu do Jogo")