'''
Created on Mar 13, 2014

@author: C_TLU
'''

A = [1,2,1,2,3,4,4]
def singleNumber(A):
    temp = 0
    for i in A:
        temp = temp^i
    return temp
print singleNumber(A)