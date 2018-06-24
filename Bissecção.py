from math import *
import math
def trun_n_d(n,d):
    s=repr(n).split('.')
    if (len(s)==1):
        return int(s[0])
    return float(s[0]+'.'+s[1][:int(d)])
def f(x):
   f = sin(x) - 1/x
   return f

a = float(input("Insira a: "))
b = float(input("Insira b: "))
p = float(input("Insira a precisão: "))
pl = 10**(-p)
if (f(a)*f(b) < 0):
   x = (a+b)/2
   if (f(x)*f(b)<0):
      a = x
   else:
      b = x
   while (abs(f(x))>pl):
      x = (a+b)/2
      if (f(x)*f(b)<0):
         a = x
      else:
         b = x
   x = trun_n_d(x,p)
   print("A raiz da função , com precisão de {} casas decimais , é {}".format(p,x))
else:
   print("Não tem raiz unica no intervalo")
