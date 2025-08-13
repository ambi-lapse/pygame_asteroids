from constants import *
from circleshape import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)


    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        print("spawn new")
        self.angle = random.uniform(20, 50)
        self.new_r = self.radius - ASTEROID_MIN_RADIUS
        roid_1 = Asteroid(self.position.x, self.position.y, self.new_r)
        roid_1.velocity = self.velocity.rotate(self.angle)*1.2
        
        roid_2 = Asteroid(self.position.x, self.position.y, self.new_r)
        roid_2.velocity = self.velocity.rotate(self.angle*-1)*1.2
        
