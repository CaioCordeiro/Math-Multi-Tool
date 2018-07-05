'''


		LIBS


'''
from math import *
import math
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def f(fx,x):#definindo a função matematica
   f = eval(fx)
   return f


'''


		METODO DE SIMPSON


'''

def simpson():
    fx = input("Insira a função : ")
    N =  int(input("Numero de pontos: "))
    # lower & upper limits of the integral
    a = float(input("Insira a : "))
    b = float(input("Insira b : "))

    # step size
    h = (b - a) / N

    # Sum the values for Simpson's integration
    s = f(fx, a) + f(fx, b)
    for i in range(1, N):
        t = a + i * h
        if i % 2 == 1:
            s += 4.0 * f(fx, t)
        else:
            s += 2.0 * f(fx, t)

    # multiply by h/3 to get the integral
    # and divide by pi to get the Bessel function.
    print(s * h / (3.0)) 



'''


		METODO DE JACOBI


'''

def jacobi(A, b, N=2000):

    x = zeros(len(A[0]))
    x_ant = zeros(len(A[0]))
    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b - dot(R, x)) / D
        if(x.all() == x_ant.all()):
            return x
        x_ant = x
    return x


def _print_arrays(number_of_variables):
    print("\n\n\n Your table:\n\n")
    for collumn in range(0, number_of_variables):
        print("|-----", end='')
    print("|   |----|   |----|")

    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            print("| A"+str(row)+str(collumn), end=' ')
        if(row == number_of_variables//2):
            print("| . | X"+str(row)+" | = | b"+str(row)+" |")
        else:
            print("|   | X"+str(row)+" |   | b"+str(row)+" |")

    for collumn in range(0, number_of_variables):
        print("|-----", end='')
    print("|   |----|   |----|\n\n\n")


def _print_arrays_final(number_of_variables, A, b, x):
    print("\n\n\n Your table:\n\n")
    for collumn in range(0, number_of_variables):
        print("|------", end='')
    print("|   |-------|   |------|")

    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            print("| "+"{0:.2f}".format(A[row][collumn]), end=' ')
        if(row == number_of_variables//2):
            print("| . | "+"{0:.2f}".format(x[row]) +
                  " | = | "+"{0:.2f}".format(b[row])+" |")
        else:
            print("|   | "+"{0:.2f}".format(x[row]) +
                  " |   | "+"{0:.2f}".format(b[row])+" |")

    for collumn in range(0, number_of_variables):
        print("|------", end='')
    print("|   |------|   |------|\n\n\n")


def _get_A_array(number_of_variables):
    temp_collumn = []
    A = []
    for row in range(0, number_of_variables):
        for collumn in range(0, number_of_variables):
            temp_collumn.append(
                float(input("Type the A"+str(row)+str(collumn)+" :")))
        print("")
        A.append(temp_collumn)
        temp_collumn = []
    return array(A)


def _get_b_array(number_of_variables):
    b = []
    for variable in range(0, number_of_variables):
        b.append(
            float(input("Type the b" + str(variable) + " :")))
    print("")
    return array(b)

# Start of the program

def jacobi1():
    number_of_variables = int(input("How many variables do you want to have? "))
    _print_arrays(number_of_variables)
    A = _get_A_array(number_of_variables)

    b = _get_b_array(number_of_variables)

    x = jacobi(A, b)

    _print_arrays_final(number_of_variables, A, b, x)


'''


		METODO DA BISSECÇÃO


'''

def trun_n_d(n,d):
    s=repr(n).split('.')#dando split no numero pelo "." criando uma lista com 2 valores , um com o numero inteiro e outro com um numero decimal
    if (len(s)==1):
        return int(s[0])#se s só tiver 1 valor é porque o numero ja é inteiro , por isso retorna ele mesmo
    return float(s[0]+'.'+s[1][:int(d)])#retorna o numero inteira + "." + o 1 valor + uma sequencia de numeros definida por "d"
def bisseccao():
   fx = input("Insira a função: ")

   a = float(input("Insira a: "))#1º Valor do intervalo [a,b]
   b = float(input("Insira b: "))
   p = float(input("Insira a precisão(Entre 1 - 16): "))#Numero de casas decimais
   pl = 10**(-p)#Definindo a precisão em numeros decimais 
   if (f(fx ,a)*f(fx ,b) < 0):#Aplicando Bozzano
      x = (a+b)/2#1ª media do intervalo
      
      if (f(fx,x)*f(fx,b)<0):#Define se o Numero achado será o novo "a" ou o novo "b"
         a = x
      else:
         b = x
      while (abs(f(fx,x))>pl):#Cria um loop em que ele só termina caso o numero atender a precisão
         x = (a+b)/2
         if (f(fx,x)*f(fx,b)<0):
            a = x
         else:
            b = x
      x = trun_n_d(x,p)#Trunca o  numero pra caber na precisão
      print("A raiz da função , com precisão de {} casas decimais , é {}".format(p,x))
   else:
      print("Não tem raiz unica no intervalo")#Caso Bozzano esteja falso
'''


		DEFININDO A GRAPHIC INTERFACE


'''
gui1 = """
======================================
|Digite (1) para -> Zeros da Função  
|Digite (2) para -> Interpolação	 
|Digite (3) para -> Integração		 
|Digite (4) para -> Sistemas Lineares
|Digite (0) para -> SAIR			 
======================================
"""
gui2 = """
===============================
|Digite (1) para -> Bissecção 
|Digite (2) para -> Newton	  
===============================
"""
gui3 = """
===============================
|Digite (1) para -> Newton    
|Digite (2) para -> Lagrange  
===============================
"""
gui4 = """
===============================
|Digite (1) para -> Simpson 
|Digite (2) para -> Trapézios  
===============================
"""
gui5 = """
===============================
|Digite (1) para -> Jacobi    
|Digite (2) para -> LU   	  
===============================
"""
guin = """
===============================
|Opção inválida no momento    |
===============================
"""
guiout = """
===============================
|Obrigado e adeus!            |
===============================
"""
'''


		RODANDO O FLUXO DE TELAS


'''
while True:
	x = int(input(gui1))

	if x == 1:
		y = int(input(gui2))
		if y == 1:
			bisseccao()
			continue
		else:
			print(guin)
			continue
	elif x == 2:
		y = int(input(gui3))
		if y == 1:
			#INSIRA O METODO DE NEWTON AQUI
			continue
		else:
			print(guin)
	elif x == 3:
		y = int(input(gui4))
		if y == 1:
			simpson()
			continue
		else:
			print(guin)
			continue
	elif x == 4:
		y = int(input(gui5))
		if y == 1:
			jacobi1()
			continue
		else:
			print(guin)
			continue
	elif x == 0:
		print(guiout)
		break
