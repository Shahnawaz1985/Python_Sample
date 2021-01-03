'''
Created on 05-May-2018

@author: Qais
'''
from collections import defaultdict

test_dict = {'A':1, 'B':2, 'Z':9}
print(test_dict)

test_default = test_dict.setdefault('C',3)
print('Default test:',test_default)
print('Default test:',test_dict)

test_defualt_dict = defaultdict(int)
test_defualt_dict['H2'] = 1
print(test_defualt_dict['A1'])

print(test_defualt_dict)

food_counter = defaultdict(int)
for food in ['Bread', 'Egg', 'Egg', 'Bread']:
    food_counter[food] += 1
    
for food, count in food_counter.items():
    print(food, count)