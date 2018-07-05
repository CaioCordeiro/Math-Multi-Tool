
def f(fx,x):#definindo a função matematica
   f = eval(fx)
   return f

def J():
    f = input("Insira a função : ")
    N =  float(input("Numero de pontos: "))
    # lower & upper limits of the integral
    a = float(input("Insira a : "))
    b = float(input("Insira b : "))

    # step size
    h = (b - a) / N

    # Sum the values for Simpson's integration
    s = f(f, a) + f(f, b)
    for i in range(1, N):
        t = a + i * h
        if i % 2 == 1:
            s += 4.0 * f(f, t)
        else:
            s += 2.0 * f(f, t)

    # multiply by h/3 to get the integral
    # and divide by pi to get the Bessel function.
    print(s * h / (3.0)) 
