# This is a basic game where the player controls a spaceship and needs to avoid incoming asteroids

# First, we'll import the pygame module
import pygame
import random

# Next, we'll initialize pygame and create a display window
pygame.init()
window_size = (400, 600)
screen = pygame.display.set_mode(window_size)

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player's spaceship
spaceship_image = pygame.image.load("player.png")
spaceship_rect = spaceship_image.get_rect()
spaceship_rect.x = window_size[0] / 2 - spaceship_rect.width / 2
spaceship_rect.y = window_size[1] - spaceship_rect.height

# Set up the incoming asteroids
asteroid_image = pygame.image.load("asteroid.png")
asteroids = []

# Set up the game loop
running = True
while running:
    # Check for events (e.g. quit, key press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the left or right arrow keys were pressed and move the spaceship accordingly
            if event.key == pygame.K_LEFT:
                spaceship_rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                spaceship_rect.x += 10

    # Update the positions of the asteroids
    for asteroid in asteroids:
        asteroid.y += 5
    
    # Remove any asteroids that have gone off the screen
    asteroids = [a for a in asteroids if a.y < window_size[1]]
    
    # Add a new asteroid at the top of the screen at a random x position
    new_asteroid_rect = asteroid_image.get_rect()
    new_asteroid_rect.x = random.randint(0, window_size[0] - new_asteroid_rect.width)
    new_asteroid_rect.y = 0
    asteroids.append(new_asteroid_rect)
    
    # Check if the spaceship has collided with any asteroids
    for asteroid in asteroids:
        if spaceship_rect.colliderect(asteroid):
            print("Game Over!")
            running = False
            break
    
    # Clear the screen and draw the spaceship and asteroids
    screen.fill(BLACK)
    screen.blit(spaceship_image, spaceship_rect)
    for asteroid in asteroids:
        screen.blit(asteroid_image, asteroid)
    pygame.display.flip()

# Quit pygame when the game loop is finished
pygame.quit()
