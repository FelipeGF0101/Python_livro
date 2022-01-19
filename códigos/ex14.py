"""
Neste exercício, usaremos input de modo um pouco diferente, fazendo com que imprima um simples prompt >.

"""
from sys import argv 

script, user_name = argv
prompt = '> '

print(f"Oi {user_name}, eu sou {script} script.") 
print("Eu gostaria de fazer algumas perguntas.")
print(f"Você gosta de mim, {user_name}?") 
likes = input(prompt)

print(f"Onde você mora? {user_name}?") 
lives = input(prompt)

print(f'Qual a sua idade? ')
idade = input(prompt)

print("Que tipo de computador você tem?") 
computer = input(prompt)

print(f"""
Então seu nome é {user_name}.
Você tem {idade} anos.
Tudo bem, então você disse {likes} sobre gostar de mim. 
Você mora em {lives}. Não tenho certeza de onde é.
E você tem um {computer}. Agradável.
""")

"""
Criamos uma variável, prompt, que é definida para o prompt que desejamos, e fornecemos a input, ao invés de digitar sempre. Agora, se quisermos que prompt seja outra coisa, basta alterarmos ele naquele ponto e executarmos de novo o script.
"""
