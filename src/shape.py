import math
import pygame


class Shape:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self, surface, position):
        equilateral_triangle_height: float = (math.sqrt(3)/2) * self.size

        x_pos, y_pos = position  # Unpack the position tuple
        front = (x_pos, y_pos - equilateral_triangle_height/2)
        left = (x_pos - self.size/2, y_pos + equilateral_triangle_height/2)
        right = (x_pos + self.size/2, y_pos + equilateral_triangle_height/2)

        # Draw the triangle
        pygame.draw.polygon(surface, self.color, [front, left, right])


# Stub to test the class that represents a shape on the screen
if __name__ == '__main__':
    pygame.init()
    WIDTH: int = 600
    HEIGHT: int = 400
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE: tuple = (255, 255, 255)
    RED: tuple = (255, 0, 0)
    clock: pygame.time.Clock = pygame.time.Clock()
    running: bool = True
    shape = Shape(20, RED)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running: bool = False
        screen.fill(WHITE)  # Fill the screen with white color (RGB)
        # Draw a red triangle on the screen
        shape.draw(
                screen,
                pygame.Vector2(100, 100),
                pygame.Vector2(100, 100)
            )
        pygame.display.flip()  # Update the display with the new drawing
        clock.tick(30)
