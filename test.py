import random
import math

a = 0
b = 1
NumAppear = 0

A = ['Kappa', 'Kappa', 'PogChamp', 'ResidentSleeper', 'Keepo', 'PogChamp',
         'ResidentSleeper', 'Keepo',
     'PogChamp', 'ResidentSleeper', 'Keepo',
     'PogChamp', 'Keepo', 'PogChamp','Kappa']
NumNames = len (A)
print (NumNames)
while b < NumNames :
    if A [a] == A[b]:
        NumAppear +=1
        del A[b]
    else:
        b +=1
print (len(A))
print (NumAppear)