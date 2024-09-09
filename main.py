import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50
target_img = pygame.transform.scale(target_img, (target_width, target_height))

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

MAX_SPEED = 1

# Начальное положение и скорость мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-1, 1]) * random.uniform(0.1, MAX_SPEED)
target_speed_y = random.choice([-1, 1]) * random.uniform(0.1, MAX_SPEED)

# Флаг, указывающий, началась ли игра
game_started = False

# Создаем шрифт для отображения текста
font = pygame.font.SysFont(None, 48)
welcome_text = font.render('Нажмите любую кнопку, чтобы начать!', True, (255, 255, 255))

# Переменные для таймера и счетчика попаданий
start_time = 0
hits = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if not game_started:
                # Начинаем игру при первом щелчке мышью или нажатии клавиши
                game_started = True
                start_time = time.time()  # Запоминаем время начала игры
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                    # Пересчитываем скорость после попадания
                    target_speed_x = random.choice([-1, 1]) * random.uniform(0.1, MAX_SPEED)
                    target_speed_y = random.choice([-1, 1]) * random.uniform(0.1, MAX_SPEED)
                    hits += 1  # Увеличиваем количество попаданий

    if game_started:
        # Обновляем позицию мишени только после начала игры
        target_x += target_speed_x
        target_y += target_speed_y

        # Проверка столкновения с границами экрана
        if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
            target_speed_x *= -1
        if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
            target_speed_y *= -1

        screen.blit(target_img, (target_x, target_y))

        # Обновляем таймер
        elapsed_time = int(time.time() - start_time)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_text = font.render(f'{hours:02}:{minutes:02}:{seconds:02}', True, (255, 255, 255))
        screen.blit(timer_text, (10, SCREEN_HEIGHT - 40))

        # Обновляем счетчик попаданий
        hits_text = font.render(f'Попадания: {hits}', True, (255, 255, 255))
        screen.blit(hits_text, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 40))
    else:
        # Отображаем приветственное сообщение, если игра еще не началась
        text_rect = welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(welcome_text, text_rect)

    pygame.display.update()

pygame.quit()