"""
Lista de comandos:

* close: Fecha o arquivo. Como File -> Save... no editor.
* read: Lê o conteúdo do arquivo. Você pode atribuir o resultado a uma variável.
* readline: Lê apenas uma linha de um arquivo de texto.
* truncate: Esvazia o arquivo. Tenha cuidado se o arquivo for importante.
* write('stuff'): Escreve "Stuff" no arquivo.
* seek (0): Move o local de leitura/ gravação para o início do arquivo.
"""
from sys import argv

script, filename = argv

print(f"Nós vamos apagar {filename}.") # We're going to erase
print("Se você não quer isso, aperte CTRL-C (^C).") # If you don't want that, hit CTRL-C (^C)
print("Se você quiser isso, clique em RETORNAR.") # If you do want that, hit RETURN.

input("?")

print("Abrindo o arquivo...")
target = open(filename,'w')

print("Truncando o arquivo. Adeus!") #Truncating the file. Goodbye!
target.truncate()

print("Agora eu vou pedir três linhas.") # Now I'm going to ask you for three lines.

line1 = input("Linha 1: ")
line2 = input("Linha 2: ")
line3 = input("Linha 3: ")

print("Vou escrever isso no arquivo.") # I'm going to write these to the file.

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(" E finalmente, nós fechamos isso.")
target.close()

# Para executar: Entre na pasta do arquivo pelo terminal e digite python ex16.py + nome do arquivo (texto.txt) 