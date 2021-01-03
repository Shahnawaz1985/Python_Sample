'''
Created on 29-Apr-2018

@author: Qais
'''
for x in range(1, 5):
    print(x)
    

sample_dict = {'a': 'A','b': 'B', 'c':'C'}
for key in sample_dict:
    print(key)
    
for value in sample_dict.values():
    print(value)
    
for item in sample_dict.items():
    print(item)
    
for key1,value1 in sample_dict.items():
    print('Key:',key1, ' has the value:',value1)
    
number = []
for x in range(1,15,2):
    number.append(x)
    
for a in number:
    print(a)
    
number1 = list(range(1,10))
print(number1)