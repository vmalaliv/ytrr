# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:23:20 2022

@author: DELL
"""

def fizzbuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i) + "= FIZZBUZZ")
        else:
            if(i%5==0):
                print(str(i)+"= Buzz")
            else:
                if(i%3==0):
                    print(str(i)+ "= FiZZ")
                else:
                    print(str(i))

fizzbuzz(41)

                
                
                