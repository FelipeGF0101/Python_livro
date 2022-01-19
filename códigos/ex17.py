from sys import argv
from os.path import exists

script, from_file, to_file = argv # Argumentos do argv

print(f"Copie de {from_file} para {to_file}.")

# Poderíamos fazer esses dois com uma linha, como?
in_file = open(from_file); indata = in_file.read()

print(f"O arquivo de entrada é {len(indata)} bytes de comprimento.") # len verifica o tamanho total do arquivo

print(f"O arquivo de saída existe?{exists(to_file)}.") # O exists verificará se existe o arquivo para o qual a mensagem será copiada.
print(f"Pronto, aperte ENTER para continuar, CTRL -c para abortar.") # Espera uma ação do usuário.
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Tudo bem, tudo feito.")

out_file.close(); in_file.close()

