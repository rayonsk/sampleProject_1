import random
import sys
import os

num = 21;
if num > 21 :
    print('number greater than 21')
elif num == 21:
    print('number is 21')
else :
    print('number is less than 21')
#and, or not
print('****condition with and, or ,not****')
if ((num > 21 ) and (num == 21)):
    print('number greater than 21 and 21')
elif ((num > 21 ) or (num == 21)):
    print('number greater than 21 or 21')
else :
    print('number is less than 21')
# forloop
print('****forloop****')
for x in range(0,5):
    print(x,'',end="")

print('\n')
for x in ['a','b','c']:
    print(x)

list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0, 3):
        print(list[x][y])