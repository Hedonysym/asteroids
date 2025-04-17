from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def rectangle(self):
        pass
    
    # player class method override
    def draw(self, screen):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
        a = self.position + forward * self.radius + right
        b = self.position + forward * self.radius - right 
        c = self.position - forward * self.radius - right
        d = self.position - forward * self.radius + right
        rect = [a, b, c, d]
        pygame.draw.polygon(screen, "white", rect, 2)
        pygame.draw.circle(screen, "white", rect[2], self.radius/2.5)
        pygame.draw.circle(screen, "white", rect[3], self.radius/2.5)
    
    # movement time
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    # shooting guys
    def shoot(self):
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer += PLAYER_SHOOT_COOLDOWN

    # self updating
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    