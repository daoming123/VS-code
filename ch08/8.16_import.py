import printing_models
printing_models.make_pizza(16, 'pepperoni')
printing_models.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from printing_models import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from printing_models import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


import printing_models as pm
pm.make_pizza(16, 'pepperoni')
pm.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from printing_models import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')