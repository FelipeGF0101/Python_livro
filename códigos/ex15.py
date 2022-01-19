"""
LENDO ARQUIVOS

O exercício envolve escrever dois arquivos. Um é o arquivo ex15.py normal que você executará, mas o outro é denominado ex15_sample.txt. Este segundo arquivo não é um script, mas um arquivo de texto sem formatação que iremos ler em nosso script.

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Tradução:
Isso é o que eu digitei em um arquivo.
É uma coisa muito legal.
Muita diversão aqui.

O que desejamos fazer é abrir o arquivo em nosso script e imprimi-lo. Contudo, não queremos apenas colocar o nome ex15_sample.txt em hard code no nosso script. 'Hard code' significa colocar diretamente no código-fonte alguma informação que deve vir do usuário como uma string. Isso é ruim porque queremos que ele carregue outros arquivos mais tarde. A solução é usar argv ou input para perguntar ao usuário qual arquivo abrir, ao invés de incorporar no código o nome do arquivo.

"""
# Aqui temos o que é chamado de import. É como você adiciona recursos ao script a partir do conjunto de recursos do Python. Ao invés de lhe dar todos os recursos de um só vez, o Python pede que você informe o que pretende usar.
from sys import argv, orig_argv
# A parte 'argv' é a variável do argumento. Essa variável retém os argumentos passados para o script do python quando você o executa. 

# Essa linha descompacta argv, ao invés de conter todos os argumentos. Ele é atribuído às variáveis que você pode trabalhar(script e filename). Em outras palavras: "Pegue qualquer coisa em argv, descompacte e atribua a todas essas variáveis à esquerda, em ordem."
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open (file_again)

print(txt_again.read())

"""
As linhas 1-3 usam argv para obter um nome de arquivo. Em seguida temos a linha 5, na qual usamos um novo comando, open.

A linha 7 imprime uma pequena mensagem, mas, na linha 8, temos algo bem novo e sugestivo. Chamamos uma função no txt denominada read. O que você obtém com open é um file(arquivo) e ele também tem comando que você pode dar.
Você fornece a um file um comando usando o . (ponto), o nome do comando e parâmetros, exatamente como em open e input. A diferença é que txt.read() informa: 'oi txt! Use o comando read sem parâmetros!' 
"""
