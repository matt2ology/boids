import math
import pygame


class Shape:
    """A class that represents a shape on the screen.
    """

    def __init__(self, size: int, color: tuple):
        self.size = size
        self.color = color


class Triangle(Shape):
    """A class that represents a triangle on the screen. Inherits from Shape.

    Args:
        Shape (class): The base class for all shapes on the screen.
    """

    def draw(self, surface: pygame.Surface, position: tuple):
        """Draws a triangle on the screen.

        Args:
            surface (pygame.Surface): The surface to draw the triangle on.
            position (tuple): The position of the triangle on the screen.
        """
        x_pos, y_pos = position  # Unpack the position tuple

        # Calculate the vertices of the triangle based on the position and size
        front = (x_pos, y_pos - self.size)  # The front vertex
        left = (x_pos - self.size, y_pos + self.size)
        right = (x_pos + self.size, y_pos + self.size)

        # Draw the triangle
        pygame.draw.polygon(surface, self.color, [front, left, right])

        # Draw a long line from the front vertex
        pygame.draw.line(
            surface,
            self.color,
            front,
            (front[0], front[1] - self.size),  # The end point of the line
            1  # The width of the line in pixels
        )

        def __str__(self) -> str:
            return f"Triangle(size={self.size}, color={self.color})"


# Stub to test the class that represents a shape on the screen
if __name__ == '__main__':
    pygame.init()
    WIDTH: int = 600
    HEIGHT: int = 400
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    CENTER_OF_SCREEN: tuple = (WIDTH//2, HEIGHT//2)
    WHITE: tuple = (255, 255, 255)
    RED: tuple = (255, 0, 0)
    clock: pygame.time.Clock = pygame.time.Clock()
    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running: bool = False
        screen.fill(WHITE)  # Fill the screen with white color (RGB)
        # Draw a red triangle on the screen
        obj = Triangle(5, RED).draw(screen, CENTER_OF_SCREEN)
        print(obj)

        pygame.display.flip()  # Update the display with the new drawing
        clock.tick(30)
