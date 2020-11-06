import simple_draw as sd

sd.resolution = (1400, 900)


def draw_branches(start_point, angle, length):
    if length >= 5:
        if length >= 100:
            width = 10
            color = COLOR_BROWN
        elif 70 < length < 100:
            width = 7
            color = COLOR_BROWN
        elif 30 < length <= 70:
            width = 5
            color = COLOR_BROWN
        elif length <= 30:
            width = 3
            color = sd.COLOR_DARK_GREEN
        else:
            return
    else:
        return
    delta = 30
    coefficient = .75
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v1.draw(color=color)
    next_point = v1.end_point
    next_angle = angle + delta + delta * sd.random_number(-30, 30) / 100
    next_length = length * (coefficient + coefficient * sd.random_number(-20, 20) / 100)
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    next_angle = angle - delta + delta * sd.random_number(-30, 30) / 100
    next_length = length * (coefficient + coefficient * sd.random_number(-20, 20) / 100)
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)


COLOR_BROWN = (131, 9, 0)