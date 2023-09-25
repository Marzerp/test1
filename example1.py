#!/usr/bin/env python3
# by araceliromerozerpa@gmail.com
# GNU/GPL License

import numpy as np 

data_list = np.arange(1,11,1)

for x in data_list:
    print("value: "+ str(x))

x = "hola"

try:
    z = int(x)+1
except:
    print("error in sum of z.")


#x = np.cos(x)

print(data_list)


