# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:06:42 2019

@author: KYUNGLOK BAIK
"""

import time


def initialize():
    global api_time, count, sys_time
    sys_time = 0
    count = 0
    api_time = 0
    

def api():
    global api_time, count, sys_time  
    api_time=time.time()
    
    
    interval = api_time - sys_time
    
    if interval > 5:
        sys_time = time.time()
        interval = api_time - sys_time
        count = 0

    
    

    
    if count < 2 and interval < 5:
        count+=1
        print('True')
        print(str(interval))
    else:
        count+=1
        print('False')
        print(str(interval))

    


if __name__ == '__main__':
    initialize()
    sys_time = time.time()
    print(api())
    print(api())
    print(api())
    print(api())
    print('=================')
    time.sleep(6)
    print(api())
#    print(api())
#    print(api())
#    print(api())
    print('=================')
    time.sleep(6)
    
    print(api())
#    print(api())
#    print(api())
#    print(api())
#    print('=================')
    time.sleep(6)
    