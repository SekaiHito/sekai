import pygame
import random

# Ініціалізація pygame
pygame.init()

# Розміри екрану
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20  # Розмір одного блоку змійки

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Ігровий екран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змійка")

# Швидкість змійки
clock = pygame.time.Clock()
speed = 10

# Функція для генерації позиції їжі
def random_food():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return x, y

# Функція для відображення рахунку
def show_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Рахунок: " + str(score), True, WHITE)
    screen.blit(text, [0, 0])

# Функція для відображення повідомлення про завершення гри
def show_game_over():
    font = pygame.font.Font(None, 48)
    text = font.render("Гра закінчена!", True, RED)
    screen.blit(text, [WIDTH // 2 - 100, HEIGHT // 2 - 50])
    restart_text = font.render("Натисніть R для перезапуску", True, WHITE)
    screen.blit(restart_text, [WIDTH // 2 - 160, HEIGHT // 2])

# Основна функція гри
def game():
    game_over = False
    x, y = WIDTH // 2, HEIGHT // 2  # Початкова позиція змійки
    x_speed, y_speed = 0, 0
    snake = [(x, y)]
    food_x, food_y = random_food()
    score = 0

    while True:
        # Перевірка на події
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_LEFT and x_speed == 0:
                        x_speed, y_speed = -BLOCK_SIZE, 0
                    elif event.key == pygame.K_RIGHT and x_speed == 0:
                        x_speed, y_speed = BLOCK_SIZE, 0
                    elif event.key == pygame.K_UP and y_speed == 0:
                        x_speed, y_speed = 0, -BLOCK_SIZE
                    elif event.key == pygame.K_DOWN and y_speed == 0:
                        x_speed, y_speed = 0, BLOCK_SIZE
                if game_over and event.key == pygame.K_r:
                    game()  # Перезапуск гри

        if not game_over:
            # Оновлення позиції змійки
            x += x_speed
            y += y_speed
            snake.append((x, y))
            if len(snake) > score + 1:
                del snake[0]

            # Перевірка на зіткнення з їжею
            if x == food_x and y == food_y:
                food_x, food_y = random_food()
                score += 1

            # Перевірка на зіткнення зі стінами чи собою
            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake[:-1]:
                game_over = True

        # Відображення на екрані
        screen.fill(BLACK)
        for part in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        show_score(score)

        # Відображення повідомлення про завершення гри
        if game_over:
            show_game_over()

        pygame.display.flip()
        clock.tick(speed)

# Запуск гри
if __name__ == "__main__":
    game()
