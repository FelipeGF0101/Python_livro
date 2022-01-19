"""
Fazendo perguntas

Grande parte do que um software faz é o seguinte:

1- Pega uma entrada de alguém.
2- Altera-a
3- Imprime algo para mostrar como mudou

"""
print('How old are you?', end=" ") # Quantos anos você tem?
age = input()                      # A finalidade do end=" " é fazer a resposta(input) finar na mesma linha da pergunta.

print('How tall are you?', end=" ") # Qual a sua altura?
height=input()

print('How much do you weigh?', end=" ") # Quanto você pesa?
weight=input()

print(f'So, you\'re {age} old, {height} tall and {weight} heavy.') # Então, você tem 30 anos, 180 de altura e 113 de peso.

# Aviso = Colocamos end=' ' no final de cada linha print. Isso informa ao print para não terminar a linha com um caractere de nova linha e ir para a próxima.

