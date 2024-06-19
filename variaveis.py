# Apenas declarando o valor, o Python já identifica o 'tipo' da variável.
media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'willianDotnet', 40
status = True

# função 'type()'
print(type(media))
print(type(n2))
print(type(n4))
print(type(nome))
print(type(idade))
print(type(status))
# atalho 'ALT + SHIFT + SETA PRA BAIXO' copia a linha atual para a linha de baixo.

# função 'isinstance()'
altura = 10
fisico = 'magro'
print(isinstance(altura, str))
print(isinstance(altura, float))
print(isinstance(altura, int))
print(isinstance(altura, (float, int)))
# Note que é possível 'perguntar' se a variável é de mais de um tipo usando a função apenas uma vez.

altura = 180
peso = 90
resultado = altura * peso
print(resultado)
