"""导入模块练习."""

import printing_models
import printing_models as pm
from printing_models import make_pizza
from printing_models import make_pizza as mp

printing_models.make_pizza(16, 'pepperoni')
printing_models.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


pm.make_pizza(16, 'pepperoni')
pm.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
