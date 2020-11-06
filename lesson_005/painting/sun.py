import simple_draw as sd

sd.resolution = (1400, 900)


center_point = sd.get_point(0, 900)
radius = 200
COLOR_YELLOW = (255, 255, 0)


def draw_sun():
    sd.circle(center_position=center_point, radius=radius, color=COLOR_YELLOW, width=0)
    angle0 = 270
    for angle_change in range(0, 91, 15):
        angle = angle0 + angle_change
        v1 = sd.get_vector(start_point=center_point, angle=angle, length=300, width=4)
        v1.draw(color=COLOR_YELLOW)