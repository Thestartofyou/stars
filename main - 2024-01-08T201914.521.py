import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STAR_RADIUS = 2
CONSTELLATION_DISTANCE_THRESHOLD = 100

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to generate random stars
def generate_stars(num_stars):
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(num_stars)]
    return stars

# Function to connect stars based on distance
def connect_stars(stars):
    connections = []
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            distance = calculate_distance(stars[i], stars[j])
            if distance < CONSTELLATION_DISTANCE_THRESHOLD:
                connections.append((stars[i], stars[j]))
    return connections

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Constellations")
    clock = pygame.time.Clock()

    stars = generate_stars(50)  # Adjust the number of stars as needed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw stars
        for star in stars:
            pygame.draw.circle(screen, WHITE, star, STAR_RADIUS)

        # Connect stars to form constellations
        connections = connect_stars(stars)
        for connection in connections:
            pygame.draw.line(screen, WHITE, connection[0], connection[1], 1)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

