import simple_draw as sd

sd.resolution = (1200, 900)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow():
    point = sd.get_point(100, -100)
    radius = 1200
    for color in rainbow_colors[::-1]:
        for _ in range(7):
            radius += 2
            sd.circle(center_position=point, radius=radius, color=color, width=4)

draw_rainbow()  # TODO эта строка не нужна


sd.pause()  # TODO как и эта тоже. Всё это в основном модуле вызывается
