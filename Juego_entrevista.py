import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Esquivando Enemigos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Jugador
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_speed = 8

# Enemigos
enemy_size = 50
enemy_speed = 5
enemies = []

# Puntuación
score = 0
font = pygame.font.SysFont(None, 50)

# Función para dibujar la nave del jugador
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

# Función para dibujar los enemigos
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, red, [enemy[0], enemy[1], enemy_size, enemy_size])

# Función para mostrar la puntuación
def show_score():
    score_text = font.render("Puntuación: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

# Función para mostrar el menú
def show_menu():
    menu_text = font.render("Presiona ESPACIO para empezar", True, white)
    screen.blit(menu_text, [screen_width // 2 - 250, screen_height // 2 - 30])

# Función para mostrar el mensaje de fin de juego
def game_over():
    over_text = font.render("¡Fin del Juego! Puntuación: " + str(score), True, white)
    screen.blit(over_text, [screen_width // 2 - 250, screen_height // 2 - 30])

# Bucle principal del juego
running = True
menu = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and menu:
                menu = False
                enemies.clear()
                score = 0

    if not menu:
        keys = pygame.key.get_pressed()
        player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

        # Generar enemigos aleatorios
        if random.randint(0, 100) < 5:
            enemy_x = random.randint(0, screen_width - enemy_size)
            enemy_y = -enemy_size
            enemies.append([enemy_x, enemy_y])

        # Mover enemigos hacia abajo
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                enemies.remove(enemy)
                score += 1

        # Verificar colisiones
        for enemy in enemies:
            if (
                player_x < enemy[0] + enemy_size
                and player_x + player_size > enemy[0]
                and player_y < enemy[1] + enemy_size
                and player_y + player_size > enemy[1]
            ):
                menu = True

        # Limpiar la pantalla
        screen.fill(black)

        # Dibujar elementos
        draw_player(player_x, player_y)
        draw_enemies()
        show_score()

    else:
        # Pantalla del menú
        screen.fill(black)
        show_menu()

    # Mostrar mensaje de fin de juego
    if menu and len(enemies) == 0 and score > 0:
        game_over()

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(30)

# Salir del juego
pygame.quit()
sys.exit()