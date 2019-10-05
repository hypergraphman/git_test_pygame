import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw_rect(point_start, point_finish, color):
    rect_color = pygame.Color(color)
    rect_width = 0
    rect_point = [point_start, point_finish]

    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


draw_rect((0, 0), (300, 300), 'White')
draw_rect((10, 10), (10, 280), 'Black')

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()