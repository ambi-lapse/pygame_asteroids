import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Asteroid.containers = (update_group, draw_group, asteroid_group)
    Player.containers = (update_group, draw_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (update_group, draw_group, shot_group)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    ass_field = AsteroidField()


    
    

    




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        rt = game_clock.tick(60)
        dt = rt/1000
        screen.fill("black")

        update_group.update(dt)

        for obj in draw_group:
            obj.draw(screen)

        for roid in asteroid_group:
            if player.collision(roid):
                print("Game Over")
                sys.exit()
            for bullet in shot_group:
                if bullet.collision(roid):
                    bullet.kill()
                    roid.kill()

        pygame.display.flip()
        


if __name__ == "__main__":
    main()

