import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
width, height = 650, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jueguito que no me acuerdo como se llama de los 90's")

# Cargar imágenes y escalarlas
player_image = pygame.image.load("videos interesantes/imagenes/avion.png")
player_image = pygame.transform.scale(player_image, (60, 60))

bullet_image = pygame.image.load("videos interesantes/imagenes/bala.png")
bullet_image = pygame.transform.scale(bullet_image, (50, 50))

enemy_image = pygame.image.load("videos interesantes/imagenes/alien.png")
enemy_image = pygame.transform.scale(enemy_image, (60, 60))

background_image = pygame.image.load("videos interesantes/imagenes/fondo.jpeg")
background_image = pygame.transform.scale(background_image, (width, height))

# Jugador
player_rect = player_image.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 10  # Alinea el jugador cerca de la parte inferior de la pantalla

player_speed = 10

# Balas
bullets = []

# Enemigos
enemies = []

# Reloj
clock = pygame.time.Clock()

# Mantener registro de teclas presionadas
key_pressed = {'left': False, 'right': False}

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Manejar movimientos del jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_pressed['left'] = True
            elif event.key == pygame.K_RIGHT:
                key_pressed['right'] = True
            elif event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet_rect.midtop = (player_rect.centerx, player_rect.top)
                bullets.append({'rect': bullet_rect, 'image': bullet_image})
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_pressed['left'] = False
            elif event.key == pygame.K_RIGHT:
                key_pressed['right'] = False

    # Actualizar posición del jugador
    if key_pressed['left'] and player_rect.left > 0:
        player_rect.x -= player_speed
    if key_pressed['right'] and player_rect.right < width:
        player_rect.x += player_speed

    # Actualizar posición de las balas
    for bullet in bullets:
        bullet['rect'].y -= 10  # Velocidad de las balas

    # Generar enemigos aleatorios
    if random.randint(0, 100) < 5:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, width - enemy_rect.width)
        enemy_rect.y = 0
        enemies.append(enemy_rect)

    # Actualizar posición de los enemigos
    for enemy in enemies:
        enemy.y += 5  # Velocidad de los enemigos

    # Colisiones entre balas y enemigos
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if enemy.colliderect(bullet['rect']):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Colisiones entre jugador y enemigos
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla con el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar al jugador
    screen.blit(player_image, player_rect)

    # Dibujar las balas
    for bullet in bullets: 
        screen.blit(bullet['image'], bullet['rect'].topleft)

    # Dibujar los enemigos
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer límite de fps
    clock.tick(30)
  