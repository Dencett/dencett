# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

# проверить для
paper_x, paper_y = 9, 8
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

paper_x, paper_y = 6, 8
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

paper_x, paper_y = 8, 6
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

paper_x, paper_y = 3, 4
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

paper_x, paper_y = 11, 9
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

paper_x, paper_y = 9, 11
if paper_x < envelop_x and paper_y < envelop_y:
    print('ДА!')
elif paper_x < envelop_y and paper_y < envelop_x:
    print('ДА!')
else:
    print('НЕТ!')

# (просто раскоментировать нужную строку и проверить свой код)


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 11, 2, 10
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 10, 11, 2
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 10, 2, 11
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 2, 10, 11
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 2, 11, 10
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 3, 5, 6
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 3, 6, 5
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 6, 3, 5
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 6, 5, 3
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 5, 6, 3
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 5, 3, 6
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 11, 3, 6
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 11, 6, 3
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 6, 11, 3
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 6, 3, 11
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 3, 6, 11
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

brick_x, brick_y, brick_z = 3, 11, 6
if brick_x < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_x < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_y < hole_x and brick_z < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_x < hole_y:
    print('Кирпич пройдет через отверстие!')
elif brick_z < hole_x and brick_y < hole_y:
    print('Кирпич пройдет через отверстие!')
else:
    print('Кирпич не пройдет через отверстие!')

# (просто раскоментировать нужную строку и проверить свой код)
