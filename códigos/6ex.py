"""
STRINGS E TEXTO

Uma string geralmente é um pequeno texto que você deseja exibir para alguém ou 'exportar' do programa que está escrevendo. O python sabe que você deseja que algo seja uma string quando coloca "(aspas duplas) ou '(aspas simples) em volta do texto. Você viu isso muitas vezzes usando print quando colocou o texto que queria dentro da string entre " ou ' após o print para imprimir a string.

As strings podem conter diversas variáveis que estão em seu script do Python. Lembre que uma variável é como qualquer linha de código, na qual você define um 'nome = valor'. No código deste exercício, types_of_people = 10 cria uma variável denominada types_of_people e define-a = 10. É possível colocar isso em qualquer string com {types_of_people}. Também é possível ver que tenho que usar um tipo especial de string para 'formatar'. Isso é chamado de "f-string" e fica assim:

f"some stuff here{avariable}"

O python também tem outro tipo de formatação que usa a sintaxe .format().

"""
# Criando uma variável
# nome_variável = valor
types_of_people = 10
# Concatenação de variável 
x = f'There are {types_of_people} types of people.'

binary = 'binary'

do_not = "don't"

y = f'Those who know {binary} and those who {do_not}.'

print(x)
print(y)

print(f'I said: {x}')
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
# Neste caso, as strings foram somadas, se tornando uma única string.
