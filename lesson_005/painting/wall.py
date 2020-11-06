import simple_draw as sd

sd.resolution = (1400, 900)


def draw_wall():
    length = 40
    width = 20
    shift = length / 2
    y = 50
    y1 = width
    start_line = 400
    sd.line(start_point=sd.get_point(start_line, y), end_point=sd.get_point(start_line + length * 10 + shift, y),
            color=sd.COLOR_RED, width=2)
    sd.line(start_point=sd.get_point(start_line, y + width * 14),
            end_point=sd.get_point(start_line + length * 10 + shift, y + width * 14), color=sd.COLOR_RED, width=2)
    sd.line(start_point=sd.get_point(start_line, y),
            end_point=sd.get_point(start_line, y + width * 14), color=sd.COLOR_RED, width=2)
    sd.line(start_point=sd.get_point(start_line + length * 10 + shift, y),
            end_point=sd.get_point(start_line + length * 10 + shift, y + width * 14), color=sd.COLOR_RED, width=2)
    for i in range(14):
        if i % 2 == 0:
            x1 = start_line
            x2 = start_line + length
        else:
            x1 = start_line + shift
            x2 = start_line + length + shift
        for _ in range(10):
            left_bottom = sd.get_point(x1, y)
            right_top = sd.get_point(x2, y + y1)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)
            x1 += length
            x2 += length
        y += width


def draw_roof():
    sd.polygon(point_list=point_list, color=COLOR_BROWN, width=0)
    sd.circle(center_position=sd.get_point(x, y), radius=radius, color=sd.background_color, width=0)
    sd.circle(center_position=sd.get_point(x, y), radius=radius, color=sd.COLOR_YELLOW, width=3)
    sd.line(start_point=sd.get_point(x - radius, y), end_point=sd.get_point(x + radius, y), color=sd.COLOR_YELLOW, width=2)
    sd.line(start_point=sd.get_point(x, y - radius), end_point=sd.get_point(x, y + radius), color=sd.COLOR_YELLOW, width=2)


point_list = [sd.get_point(350, 330), sd.get_point(870, 330), sd.get_point(610, 450)]
COLOR_BROWN = (131, 9, 0)
x = 610
y = 385
radius = 45