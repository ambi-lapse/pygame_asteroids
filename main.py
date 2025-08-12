import pygame 
from constants import *
from player import *




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        rt = game_clock.tick(60)
        dt = rt/1000
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()

