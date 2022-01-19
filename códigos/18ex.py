"""
NOMES, VARIÁVEIS, CÓDIGOS, FUNÇÕES

AS FUNÇÕES FAZEM TRÊS COISAS:

1 - Nomeiam partes do código, assim como as variáveis nomeiam strings e números.

2 - Recebem argumentos da mesma maneira que seus scripts recebem argv.

3 - Usando 1 e 2 permitem que você crie seus próprios 'miniscripts' ou 'pequenos comandos'.

Em python, uma função é uma sequência de comandos que executa alguma tarefa e que tem um nome. A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema.
"""
# É possível criar uma função usando a palavra def no python. Criando quantro funções diferentes que funcionam como scripts.

# Essa aqui é como seus scripts com argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Descartando o *args podemos fazer simplismente isso
def print_two_again(arg1, arg2):
     print(f"arg1: {arg1}, arg2: {arg2}")
    
# Esse recebe apenas um argumento

def print_one(arg1):
    print(f"arg1: {arg1}")

# Esse não recebe nenhum argumento

def print_none():
    print("Eu não tenho nada'.")

print_two("Felipe", "Guedes")
print_two_again("Felipe", "Guedes")
print_one("First!")
print_none()

"""
1 - Informamos ao Python que desejamos criar uma função usando def para "definir".
2 - Na mesma linha de def, nomeamos a função. Neste caso, apenas chamamos de "print_two", mas também poderia ser qualquer outro nome. Não importa, basta que sua função tenha um nome curto e informativo sobre o que faz.
3 - Informamos que desejamos *args, que é muito parecido com o argv, mas para funções. Isso precisa ficar entre parênteses para funcionar.
4 - Terminanos a linha com : e iniciamos o recuo.
5 - Após dois pontos, todas as linhas recuadas com quatro espaços serão anexadas a print_two. Nossa primeira linha recuada descompacta os argumentos, como acontece com seus scripts.  
"""
 