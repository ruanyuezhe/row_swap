# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:08:14 2019

@author: Administrator
"""
  #!/usr/bin/env python
 # -*- coding:utf-8 -*-
# Author: jyro

import numpy as np
A = np.arange(25).reshape(5,5)
#B = np.copy(A[0])
#A[0] = A[4]
#A[4] = B
#print(B)
def change_double(array, r1, r2):
    print("初始:\n",array)
    B = np.copy(array[r1])
    array[r1] = array[r2]
    array[r2] = B
    print("结果:\n",array)

change_double(A,0,4)