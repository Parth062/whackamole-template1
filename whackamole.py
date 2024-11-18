import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x = 0
        mole_y = 0
        mole_rect = pygame.Rect(mole_x, mole_y, 32, 32)

        def get_random_position():
            x = random.randrange(0,640,32)
            y = random.randrange(0,512,32)
            return x,y

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):

                        mole_x, mole_y = get_random_position()
                        mole_rect.topleft = (mole_x, mole_y)

            screen.fill((144, 238, 144))

            for x in range(0, 640 + 1, 32):
                pygame.draw.line(screen, "dark blue", (x, 0), (x, 512))
            for y in range(0, 512 + 1, 32):
                pygame.draw.line(screen, "dark blue", (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()

            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
