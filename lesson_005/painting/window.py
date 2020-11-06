import simple_draw as sd

sd.resolution = (1400, 900)


def draw_window():
    sd.rectangle(left_bottom=sd.get_point(x - 70, y - 70), right_top=sd.get_point(x + 70, y + 70),
                 color=sd.background_color, width=0)
    sd.rectangle(left_bottom=sd.get_point(x - 70, y - 70), right_top=sd.get_point(x + 70, y + 70),
                 color=sd.COLOR_YELLOW, width=3)
    sd.circle(center_position=center_face, radius=38, color=sd.COLOR_PURPLE, width=0)
    sd.circle(center_position=sd.get_point(a - 20, b + 15), radius=8, color=sd.COLOR_BLUE, width=2)
    sd.circle(center_position=sd.get_point(a + 20, b + 15), radius=8, color=sd.COLOR_BLUE, width=2)
    sd.line(start_point=sd.get_point(a - 25, b - 5), end_point=sd.get_point(a - 10, b - 15), color=sd.COLOR_BLUE, width=2)
    sd.line(start_point=sd.get_point(a - 10, b - 15), end_point=sd.get_point(a + 10, b - 15), color=sd.COLOR_BLUE, width=2)
    sd.line(start_point=sd.get_point(a + 10, b - 15), end_point=sd.get_point(a + 25, b - 5), color=sd.COLOR_BLUE, width=2)
    sd.line(start_point=sd.get_point(x - 70, y), end_point=sd.get_point(x + 70, y), color=sd.COLOR_YELLOW, width=2)
    sd.line(start_point=sd.get_point(x, y - 70), end_point=sd.get_point(x, y + 70), color=sd.COLOR_YELLOW, width=2)


x = 610
y = 200
a = x + 20
b = y - 30
center_face = sd.get_point(a, b)