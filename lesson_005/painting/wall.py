import simple_draw as sd

sd.resolution = (1200, 900)


def draw_wall():
    length = 40
    width = 20
    shift = length / 2
    y = 50
    y1 = width
    start_line = 200
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


draw_wall()

sd.pause()