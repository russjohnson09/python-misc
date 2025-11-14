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

def main():
    i = 0
    running = True
    while running:
        i += 1
        print(i)
        if i > 2000:
            return
        for event in pygame.event.get():  # Process all events in the queue
            if event.type == pygame.QUIT:
                running = False
                return
        
        pygame.time.wait(1)


main()

pygame.quit()

# pygame.time.wait(15000)





pygame.quit()
