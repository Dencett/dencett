import simple_draw as sd

sd.resolution = (1400, 900)

def draw_human():
    sd.circle(center_position=center_face, radius=38, color=sd.COLOR_PURPLE, width=0)
    sd.circle(center_position=sd.get_point(a - 20, b + 15), radius=8, color=sd.COLOR_BLUE, width=2)
    sd.circle(center_position=sd.get_point(a + 20, b + 15), radius=8, color=sd.COLOR_BLUE, width=2)
    sd.line(start_point=sd.get_point(a - 25, b - 5), end_point=sd.get_point(a - 10, b - 15), color=sd.COLOR_BLUE,
            width=2)
    sd.line(start_point=sd.get_point(a - 10, b - 15), end_point=sd.get_point(a + 10, b - 15), color=sd.COLOR_BLUE,
            width=2)
    sd.line(start_point=sd.get_point(a + 10, b - 15), end_point=sd.get_point(a + 25, b - 5), color=sd.COLOR_BLUE,
            width=2)
    sd.line(start_point=sd.get_point(a, y), end_point=sd.get_point(a, y - 90), color=sd.COLOR_PURPLE, width=4)
    sd.line(start_point=sd.get_point(a, y - 40), end_point=sd.get_point(a - 30, y - 50), color=sd.COLOR_PURPLE, width=4)
    sd.line(start_point=sd.get_point(a, y - 40), end_point=sd.get_point(a + 30, y - 50), color=sd.COLOR_PURPLE, width=4)
    sd.line(start_point=sd.get_point(a, y - 90), end_point=sd.get_point(a - 15, y - 150), color=sd.COLOR_PURPLE, width=4)
    sd.line(start_point=sd.get_point(a, y - 90), end_point=sd.get_point(a + 15, y - 150), color=sd.COLOR_PURPLE, width=4)


a = 920
b = 238
y = b - 38
center_face = sd.get_point(a, b)

