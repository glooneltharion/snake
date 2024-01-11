import pygame
from random import randrange

WINDOW = 600
TILE_SIZE = 30
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game')


def get_random_position():
    x = randrange(TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    y = randrange(TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    return [x, y]


snake_head = pygame.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake_head.center = get_random_position()
length = 1
snake_body = [snake_head.copy()]
snake_dir = (0, 0)
dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

food = snake_head.copy()
food.center = get_random_position()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dirs[pygame.K_UP]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 0, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            elif event.key == pygame.K_DOWN and dirs[pygame.K_DOWN]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            elif event.key == pygame.K_LEFT and dirs[pygame.K_LEFT]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 0}
            elif event.key == pygame.K_RIGHT and dirs[pygame.K_RIGHT]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 0, pygame.K_RIGHT: 1}

    screen.fill('black')

    # eat food
    if snake_head.colliderect(food):
        food.center = get_random_position()
        while any(tile.colliderect(food) for tile in snake_body):
            food.center = get_random_position()
        length += 1

    # move snake
    snake_head.move_ip(snake_dir)
    snake_body.append(snake_head.copy())
    snake_body = snake_body[-length:]

    # check for collisions after the snake has moved
    self_eating = False
    for tile in snake_body[:-1]:
        if tile == snake_head:
            self_eating = True
    if (
            snake_head.left < 0
            or snake_head.right > WINDOW
            or snake_head.top < 0
            or snake_head.bottom > WINDOW
            or self_eating
    ):
        snake_head.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        snake_body = [snake_head.copy()]
        self_eating = False

    # draw food
    pygame.draw.rect(screen, 'red', food)
    # draw snake
    [pygame.draw.rect(screen, 'green', tile) for tile in snake_body]

    pygame.display.flip()
    clock.tick(8)
