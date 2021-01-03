'''
Created on 05-May-2018

@author: Qais
'''
from TestClass import TestClass

class TestClass2(TestClass):
        def __init__(self):
            print('In class TestClass2')
 

test = TestClass2()
test.sayIt()
    