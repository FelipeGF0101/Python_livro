"""
Agora, iremos difitar ainda mais variáveis e imprimi-las. Desta vez, usaremos algo chamado string de formatação.
AS strings são muito úteis, portanto, neste exercício, você aprenderá a criar strings que têm variáveis incorporadas.
Você incorpora as variáveis em uma string usando uma sequência {} especial, então, coloca a variável desejada dentro dos caracteres {}. Deve iniciar a string com a letra f para "formatar", como em f"Hello{somevar}". Esse pequeno f antes da " (aspas duplas) e os caracteres {} informam ao Python 3: "Ei, essa string precisa ser formatada. Coloque as variáveis aqui."
"""
# nome_da_variável = (recebe) 'valor'
my_name = 'Zed A. Shaw' # mue nome = 'Zed A. Shaw' 
my_age = 35 # Minha idade = 35
my_height = 74 # Minha altura = 74 polegadas
my_weight = 180 # Meu peso = 180 libras
my_eyes = 'Blue' # Meus olhos = 'Azuis'
my_teeth = 'white' # Meus dentes = 'Brancos'
my_hair = 'Brown' # Meu cabelo = 'Testa

print(f"Let's talk about {my_name}.") # Vamos falar sobre ...
print(f"He's {my_height} inches tall.") # Ele tem ... centímetros de altura.
print(f"He's {my_weight} pounds heavy") # Ele pesa ... libras
print("Actually that's not too heavy") # Na verdade, isso não é muito pesado.
print(f"He's got {my_eyes} eyes and {my_hair} hair.") # Ele tem olhos ... e cabelo ...
print(f"He's teeth are usually {my_teeth} depending on the coffee.") # Seus dentes são geralmente ... dependendo do café.

print('====================================================================')
print('CONVERSOR  DE LIBRAS EM QUILOGRAMAS')

valor = float(input("Digite o seu peso em libras: "))
resultado = valor * 0.454
print(f'O resultado é: {resultado}kg')

print('=====================================================================')

print('CONVERSOR DE POLEGADAS EM CENTÍMETROS')

valor1 = float(input("Digite o valor em polegadas: "))
result = valor1 * 2.54
print(f'O resultado é: {round(result, 1)} cm') # round serve para arredondadar valores grandes

