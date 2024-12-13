import pygame
import random

# Initialise the pygame library.
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ROBOT_SIZE = 50
TARGET_SIZE = 30

# Defining the colours used in the code.
background_colour = (137, 207, 240)
robot_colour = (255, 0, 0)
target_colour = (0, 0, 0)

# Setting up the window that the game will be played in and the caption.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Robot Chasing Target")

class Robot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ROBOT_SIZE, ROBOT_SIZE))
        self.image.fill(robot_colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move_towards(self, mouse_pos):
        # Simple movement towards the mouse.
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            dx /= distance
            dy /= distance
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TARGET_SIZE, TARGET_SIZE))
        self.image.fill(target_colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def wander(self):
        # The target's random movement
        self.rect.x += random.randint(-self.speed, self.speed)
        self.rect.y += random.randint(-self.speed, self.speed)
        # Keep target within the screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - TARGET_SIZE))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - TARGET_SIZE))

def game_loop():
    # Create the sprite groups
    all_sprites = pygame.sprite.Group()
    robot = Robot(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    target = Target(random.randint(0, SCREEN_WIDTH - TARGET_SIZE),
                    random.randint(0, SCREEN_HEIGHT - TARGET_SIZE))

    # Add sprites to group
    all_sprites.add(robot, target)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(background_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        robot.move_towards(mouse_pos)
        target.wander()

        # Check for collisions
        if robot.rect.colliderect(target.rect):
            print("You caught me :(")
            # Relocate the target
            target.rect.x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
            target.rect.y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)

        # Draw the sprites onto the screen.
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
