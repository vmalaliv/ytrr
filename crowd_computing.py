# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:37:29 2022

@author: DELL
"""
from statistics import mean
from scipy import stats


estimates=[30044, 301, 302, 303, 304, 305, 306, 
           307, 308, 309, 310, 311, 312, 313,
           314, 315, 316, 317, 318, 31869, 320,
           321, 322, 323, 324, 3625, 326, 327,
           328, 329, 330, 331, 332, 3383, 334, 
           335, 3364, 337, 9338, 339, 340, 341,
           342, 343, 344, 34445, 346, 347, 348,
           349, 350, 351, 352, 353, 354, 355,
           356, 357, 358, 359, 360, 361, 362,
           363, 364, 365, 366, 367, 3268, 369,
           370, 371, 372, 373, 374, 3075]
estimates.sort()
m = stats.trim_mean(estimates, 0.1)
print(m)

# tv=int(0.1*len(estimates))
# estimates=estimates[tv:]
# estimates=estimates[:len(estimates)-tv]
# print(mean(estimates))

