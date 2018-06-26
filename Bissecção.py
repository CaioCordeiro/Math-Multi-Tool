#Metodo da Bissecção
from math import *
import math
#Função para truncar de acordo com a precisão
def trun_n_d(n,d):
    s=repr(n).split('.')#dando split no numero pelo "." criando uma lista com 2 valores , um com o numero inteiro e outro com um numero decimal
    if (len(s)==1):
        return int(s[0])#se s só tiver 1 valor é porque o numero ja é inteiro , por isso retorna ele mesmo
    return float(s[0]+'.'+s[1][:int(d)])#retorna o numero inteira + "." + o 1 valor + uma sequencia de numeros definida por "d"
def f(x):#definindo a função matematica
   f = sin(x) - 1/x
   return f

a = float(input("Insira a: "))#1º Valor do intervalo [a,b]
b = float(input("Insira b: "))
p = float(input("Insira a precisão: "))#Numero de casas decimais
pl = 10**(-p)#Definindo a precisão em numeros decimais 
if (f(a)*f(b) < 0):#Aplicando Bozzano
   x = (a+b)/2#1ª media do intervalo
   if (f(x)*f(b)<0):#Define se o Numero achado será o novo "a" ou o novo "b"
      a = x
   else:
      b = x
   while (abs(f(x))>pl):#Cria um loop em que ele só termina caso o numero atender a precisão
      x = (a+b)/2
      if (f(x)*f(b)<0):
         a = x
      else:
         b = x
   x = trun_n_d(x,p)#Trunca o  numero pra caber na precisão
   print("A raiz da função , com precisão de {} casas decimais , é {}".format(p,x))
else:
   print("Não tem raiz unica no intervalo")#Caso Bozzano esteja falso

