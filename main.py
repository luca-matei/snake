import random
import pygame

from settings import settings

pygame.init()
screen = pygame.display.set_mode((settings.screen_w, settings.screen_h))
clock = pygame.time.Clock()
running = True

x = 1
y = 1
snake_sqrs = [(x, y)]
direction = "right"
apple_x = random.randint(0, settings.pula - 1)
apple_y = random.randint(0, settings.screen_sq_y - 1)


def calculate_direction(_event):
    global direction
    if _event.key == pygame.K_UP:
        if direction != "down":
            direction = "up"

    elif _event.key == pygame.K_DOWN:
        if direction != "up":
            direction = "down"

    elif _event.key == pygame.K_LEFT:
        if direction != "right":
            direction = "left"

    elif _event.key == pygame.K_RIGHT:
        if direction != "left":
            direction = "right"


def calculate_key_press():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                running = False
                break

            calculate_direction(event)


def move_snake():
    global x, y, snake_sqrs

    if direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1

    snake_sqrs = [(x, y)] + snake_sqrs[:-1]


def calculate_boundaries():
    global x, y
    if x >= settings.pula:
        x = -1
        y += 1
    elif y >= settings.screen_sq_y:
        y = -1
        x += 1
    elif x < 0:
        x = settings.pula
        y -= 1
    elif y < 0:
        y = settings.screen_sq_y
        x -= 1


def render():
    # Reset
    screen.fill(settings.screen_bg_color)
    for i in range(0, settings.pula):
        for j in range(0, settings.screen_sq_y):
            pygame.draw.rect(
                screen,
                settings.border_color,
                (i * settings.sq_size, j * settings.sq_size, settings.sq_size, settings.sq_size),
            )
            pygame.draw.rect(
                screen,
                settings.screen_bg_color,
                (
                    i * settings.sq_size + 1,
                    j * settings.sq_size + 1,
                    settings.sq_size - 2,
                    settings.sq_size - 2,
                ),
            )

    # Draw apple
    pygame.draw.rect(
        screen,
        settings.apple_color,
        (
            apple_x * settings.sq_size,
            apple_y * settings.sq_size,
            settings.sq_size,
            settings.sq_size,
        ),
    )

    # Draw snake
    for sx, sy in snake_sqrs:
        pygame.draw.rect(
            screen,
            settings.snake_color,
            (
                sx * settings.sq_size,
                sy * settings.sq_size,
                settings.sq_size,
                settings.sq_size,
            ),
        )

    pygame.display.flip()
    clock.tick(settings.fps)


while running:
    hit_apple = False

    calculate_key_press()
    move_snake()

    if x == apple_x and y == apple_y:
        apple_x = random.randint(0, settings.pula - 1)
        apple_y = random.randint(0, settings.screen_sq_y - 1)

        snake_sqrs.append(snake_sqrs[-1])
        hit_apple = True

    if not hit_apple:
        if (x, y) in snake_sqrs[1:]:
            pygame.quit()
            raise Exception("Game Over!")

    calculate_boundaries()
    render()

pygame.quit()
