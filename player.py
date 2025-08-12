from constants import *
from circleshape import *
import pygame


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt-1)
        if keys[pygame.K_d]:
            self.rotate(dt+1)
        if keys[pygame.K_w]:
            self.move(dt+1)
        if keys[pygame.K_s]:
            self.move(dt-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
            print("Fire!")
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt



    def shoot(self):
        self.velocity = (pygame.Vector2(0, 1).rotate(self.rotation))


class Shot(CircleShape):
    def __init__(self, pos, radius):
        self.position = pos
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)


    def update(self, dt):
        self.position += (self.velocity*dt)