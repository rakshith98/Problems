#!/usr/bin/env python

#using recursion
def fact(x):
  if(x==1):
    return 1
  else:
    return x*fact(x-1)
a=int(input())
answer1=fact(a)

#using loops
answer2=1
for i in range(1,a+1):
  answer2=answer2*i
