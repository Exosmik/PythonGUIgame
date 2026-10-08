import math
import pygame
import time

#initiating the game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clicker Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
CoinEarnt = pygame.mixer.Sound("soundeffects/freesound_gamestudio-button-394464.mp3")
CoinEarnt.set_volume(0.5)

# Circle settings
circle_center = (400, 300)
base_radius = 100
max_radius = base_radius + 35   #hard cap
grow_amount = 25                # added per click
shrink_speed = 120              # pixels per second
current_radius = float(base_radius)
circle_color = (210, 150, 80)

# Score
score = 0

# Program start
running = True
while running:
    dt = clock.tick(60) / 1000 #Seconds since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            distance = math.hypot(mouse_x - circle_center[0],
                                  mouse_y - circle_center[1])
            if distance <= current_radius: #Give the player a point every time they click the circle
                score += 1 
                CoinEarnt.play() # Sound effect played
                current_radius =  min(current_radius + grow_amount, max_radius) # Increase radius

    # Animating the circle shrinking to normal
    if current_radius > base_radius:
        current_radius -= shrink_speed * dt
        current_radius = max(current_radius, base_radius)


    # Drawing
    screen.fill((30, 30, 40))
    pygame.draw.circle(screen, circle_color, circle_center, int(current_radius))

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()