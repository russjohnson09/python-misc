import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Square Example")

RED = (255, 0, 0)  # RGB values for red
WHITE = (255, 255, 255) # RGB values for white background


screen.fill(WHITE)  # Fill the screen with white
pygame.draw.rect(screen, RED, (100, 100, 50, 50)) # Draw a red rectangle at (100,100) with size 50x50


pygame.display.flip() # Or pygame.display.update()


pygame.time.wait(15000)





pygame.quit()
