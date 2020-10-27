# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from my_burger import bottom_bun_function
from my_burger import cutlet_function
from my_burger import cucumber_function
from my_burger import tomato_function
from my_burger import mayonnaise_function
from my_burger import ketchup_function
from my_burger import cheese_function
from my_burger import top_bun_function

bottom_bun_function()
cutlet_function()
cucumber_function()
mayonnaise_function()
cheese_function()
cutlet_function()
tomato_function()
cheese_function()
ketchup_function()
top_bun_function()
print('Готово!')
