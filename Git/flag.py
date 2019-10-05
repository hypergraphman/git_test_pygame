import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw_rect(point_start, width_height, color, width_border):
    rect_color = pygame.Color(color)
    rect_width = width_border
    rect_point = [point_start, width_height]

    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


draw_rect((0, 0), (300, 300), 'White', 0)
draw_rect((10, 10), (10, 280), 'Black', 0)
draw_rect((19, 20), (270, 51), 'Black', 1)
draw_rect((19, 70), (270, 51), 'Black', 1)
draw_rect((19, 120), (270, 51), 'Black', 1)
# просто комментарий
draw_rect((20, 71), (268, 49), 'Blue', 0)


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()