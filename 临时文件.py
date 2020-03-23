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
print("初始:\n",A)
A[[0,4]] = A[[4,0]]
print("结果:\n",A)