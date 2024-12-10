#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 04.12.2024
#Autor: Szymon Szeliga

#ZADANIE 9.1 (PADAJĄCY ŚNIEG)
#Zaimplementować prostą grę o topieniu padającego śniegu.
#Przy górnej krawędzi ekranu pojawiają się losowo płatki śniegu, które spadają w dół ruchem jednostajnym.
#Zadaniem gracza jest topienie płatków śniegu przez klikanie na nie myszą.
#Celem gry jest niedopuszczenie, aby jakiś płatek śniegu dotarł do dolnej krawędzi ekranu.
#Można rozważyć wariant gry, w którym tworzą się zaspy śniegu, a gra kończy się, gdy zaspa urośnie do górnej krawędzi ekranu.

import sys
import pygame
import random
import time

#INICJALIZACJA PYGAME
pygame.init()

#PODSTAOWE DANE
WIDTH = 1024
HEIGHT = 768
SIZE = (WIDTH, HEIGHT)

FPS = 60

BACKGROUND_COLOR = (0, 0, 0)
SCORE_COLOR = (255, 255, 255)

SNOW_FLAKE_VELOCITY = 3
SNOWS_FLAKES_FREQUENCY = 25

SCORE = 0
RUNNING = True

#USTAWIENIA OKNA
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("fallingSnow")

clock = pygame.time.Clock()


#KLASA SNOWFLAKE
class Snowflake(pygame.sprite.Sprite):
    def __init__(self, x_positon, image, velocity):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x_positon, 0)
        self.speed = velocity

    def update(self):
        self.rect.y += self.speed


snowflake_image = pygame.image.load('snowFlakeImage.png').convert()
snowflake_image.set_colorkey((0, 0, 0))           #usuniecie czarnego tla z obrazka snowFlakeImage.png
snowflake_image = pygame.transform.scale(snowflake_image, (50, 50))  # a tutaj zmniejszamy obrazek

snowFlakes = pygame.sprite.Group()

while RUNNING:

    window.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked = [snowflake for snowflake in snowFlakes if snowflake.rect.collidepoint(mouse_pos)]
            for clicked_snowflake in clicked:
                clicked_snowflake.kill()
                SCORE += 1


    if random.randint(1, SNOWS_FLAKES_FREQUENCY) == 1:
        x_position = random.randint(0, WIDTH)
        snowflake = Snowflake(x_position, snowflake_image, SNOW_FLAKE_VELOCITY)
        snowFlakes.add(snowflake)

    snowFlakes.update()
    snowFlakes.draw(window)

    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render(f"Punkty: {SCORE}", False, SCORE_COLOR)
    window.blit(score_text, (10, 10))

    for snowflake in snowFlakes:
        if snowflake.rect.top >= HEIGHT:
            game_over_text = font.render("Game Over", False, SCORE_COLOR)
            window.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.update()
            time.sleep(1)
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)

