import simple_draw as sd

sd.resolution = (1400, 900)


snow_x_list = []
snow_y_list = []
length_list = []

for _ in range(30):
    snow_x_list.append(sd.random_number(80, 300))
    snow_y_list.append(sd.random_number(400, 500))
    length_list.append(sd.random_number(10, 40))


def draw_snowfall():
    while True:
        sd.start_drawing()
        for i, x in enumerate(snow_x_list):
            length = length_list[i]
            point = sd.get_point(snow_x_list[i], snow_y_list[i])
            sd.snowflake(center=point, length=length, color=sd.background_color)
            if snow_y_list[i] > 70:
                snow_y_list[i] -= 10
                point_fall = sd.get_point(snow_x_list[i], snow_y_list[i])
                sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
            else:
                last_point = sd.get_point(snow_x_list[i], snow_y_list[i])
                sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(0.01)
        if sd.user_want_exit():
            break