import pygame
import numpy as np
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CENTER = np.array([WIDTH // 2, HEIGHT // 2])
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 1

# Define the 4D tesseract vertices (simplified as 16 points)
vertices = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, -1],
    [1, 1, -1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, 1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
    [1, -1, -1, -1],
    [-1, 1, 1, 1],
    [-1, 1, 1, -1],
    [-1, 1, -1, 1],
    [-1, 1, -1, -1],
    [-1, -1, 1, 1],
    [-1, -1, 1, -1],
    [-1, -1, -1, 1],
    [-1, -1, -1, -1]
])

# 4D rotation matrix (for rotating in 4D space)
def rotate4d(vertices, angle_xz, angle_yw, angle_zw, angle_xy):
    rotation_matrix_xz = np.array([
        [math.cos(angle_xz), -math.sin(angle_xz), 0, 0],
        [math.sin(angle_xz), math.cos(angle_xz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    rotation_matrix_yw = np.array([
        [1, 0, 0, 0],
        [0, math.cos(angle_yw), -math.sin(angle_yw), 0],
        [0, math.sin(angle_yw), math.cos(angle_yw), 0],
        [0, 0, 0, 1]
    ])

    rotation_matrix_zw = np.array([
        [math.cos(angle_zw), 0, -math.sin(angle_zw), 0],
        [0, 1, 0, 0],
        [math.sin(angle_zw), 0, math.cos(angle_zw), 0],
        [0, 0, 0, 1]
    ])

    rotation_matrix_xy = np.array([
        [math.cos(angle_xy), -math.sin(angle_xy), 0, 0],
        [math.sin(angle_xy), math.cos(angle_xy), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # Apply all rotations to the vertices
    rotated_vertices = np.dot(vertices, rotation_matrix_xz)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_yw)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_zw)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_xy)
    
    return rotated_vertices

# Project 4D to 3D with additional zoom effect
def project_to_3d(vertices, zoom_factor=1):
    projected = []
    for vertex in vertices:
        x, y, z, w = vertex
        factor = zoom_factor / (4 - w)  # Perspective divide (for depth effect)
        projected.append(np.array([x * factor, y * factor, z * factor]))
    return np.array(projected)

# Initialize pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive 4D Tesseract Animation")

# Variables for rotation speed and control
angle_xz, angle_yw, angle_zw, angle_xy = 0, 0, 0, 0
rotation_speed = 0.02
zoom_factor = 100

# Main loop
clock = pygame.time.Clock()

# Interactive control variables
mouse_x, mouse_y = 0, 0
dragging = False

# UI for rotation speed and zoom
rotation_ui_active = False
zoom_ui_active = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Capture mouse movement for rotation control
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse click to start dragging
                dragging = True
                mouse_x, mouse_y = event.pos
            elif event.button == 3:  # Right click to toggle UI
                rotation_ui_active = not rotation_ui_active
                zoom_ui_active = not zoom_ui_active

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Release left mouse button to stop dragging
                dragging = False

        if event.type == pygame.MOUSEMOTION:
            if dragging:
                dx, dy = event.pos[0] - mouse_x, event.pos[1] - mouse_y
                angle_xz += dx * rotation_speed  # XZ plane rotation
                angle_yw += dy * rotation_speed  # YW plane rotation
                mouse_x, mouse_y = event.pos

        # Arrow key control for rotation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle_xz -= rotation_speed
        if keys[pygame.K_RIGHT]:
            angle_xz += rotation_speed
        if keys[pygame.K_UP]:
            angle_yw -= rotation_speed
        if keys[pygame.K_DOWN]:
            angle_yw += rotation_speed

        # Zoom with mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom_factor += 10
            elif event.y < 0:
                zoom_factor -= 10

    # Rotate the tesseract in 4D space with continuous rotation
    rotated_vertices = rotate4d(vertices, angle_xz, angle_yw, angle_zw, angle_xy)

    # Project 4D vertices to 3D
    projected_vertices = project_to_3d(rotated_vertices, zoom_factor)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw edges between vertices (connecting each pair of vertices)
    for i, vertex in enumerate(projected_vertices):
        for j in range(i + 1, len(projected_vertices)):
            pygame.draw.line(screen, LINE_COLOR, CENTER + vertex[:2] * zoom_factor, CENTER + projected_vertices[j][:2] * zoom_factor, LINE_WIDTH)

    # Display rotation and zoom info
    if rotation_ui_active:
        font = pygame.font.SysFont('Arial', 24)
        rotation_text = font.render(f'Rotation Speed: {rotation_speed:.2f}', True, LINE_COLOR)
        screen.blit(rotation_text, (10, 10))
    
    if zoom_ui_active:
        zoom_text = font.render(f'Zoom Factor: {zoom_factor}', True, LINE_COLOR)
        screen.blit(zoom_text, (10, 40))

    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    clock.tick(FPS)
