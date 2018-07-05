gui1 = """
======================================
|Digite (1) para -> Zeros da Função  |
|Digite (2) para -> Interpolação	 |	 
|Digite (3) para -> Integração		 |
|Digite (4) para -> Sistemas Lineares|
|Digite (0) para -> SAIR			 |
======================================
"""
gui2 = """
===============================
|Digite (1) para -> Bissecção |
|Digite (2) para -> Newton	  |
===============================
"""
gui3 = """
===============================
|Digite (1) para -> Newton    |
|Digite (2) para -> Lagrange  |
===============================
"""
gui4 = """
===============================
|Digite (1) para -> Trapézios |
|Digite (2) para -> Simpsom	  |
===============================
"""
gui5 = """
===============================
|Digite (1) para -> Jacobi    |
|Digite (2) para -> LU   	  |
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
while True:
	x = int(input(gui1))

	if x == 1:
		y = int(input(gui2))
		if y == 1:
			#INSIRA A FUNÇÃO DE BISSECAO AQUI
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
			#INSIRA O METODO DOS TRAPÉZIOS AQUI
			continue
		else:
			print(guin)
			continue
	elif x == 4:
		y = int(input(gui5))
		if y == 1:
			#INSIRA O METODO DE JACOBI AQUI
			continue
		else:
			print(guin)
			continue
	elif x == 0:
		print(guiout)
		break
