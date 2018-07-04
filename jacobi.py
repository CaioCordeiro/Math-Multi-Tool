from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


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

def jacobi():
    number_of_variables = int(input("How many variables do you want to have? "))
    _print_arrays(number_of_variables)
    A = _get_A_array(number_of_variables)

    b = _get_b_array(number_of_variables)

    x = jacobi(A, b)

    _print_arrays_final(number_of_variables, A, b, x)

jacobi()
