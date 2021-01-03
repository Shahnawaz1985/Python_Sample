'''
Created on 04-May-2018

@author: Qais
'''
import TestClass

def test():
    ''' This is a test Function
    , testing it internally'''
    print('This function is named as :', test.__name__)
    print('Description is:',test.__doc__)
    

test()

short_list = [1, 3, 5]
position = 5

try:
    print(short_list[position])
except IndexError as index:
    print('Need a position between 0 and', len(short_list)-1, 'but got',position, ' hence issue is:',index)
