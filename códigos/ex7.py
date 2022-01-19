"""
Mais impressão
"""
print("Mary had a little lamb.")
# Maria tinha um cordeirinho
print("Its fleece was white as {}.".format('snow'))
# Sua lã era branca como a neve
print("And everywhere that Mary went.")
# E em todos os lugares que Mary foi
print("." * 10) # what'd that do? O que isso faz?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# Aqui realizamos a juntão de todas as variáveis e transformamos em uma única string. Esta string foi criada no fim com o ', end = ' '. end (nome da string) = (recebe) ' ' (aspas simples vazias/informando que a junção de todas retornará uma única string)
# Removendo a vírgula, o código retorna erro.

print(end7 + end8 + end9 + end10 + end11 + end12) 
# Aqui todos valores das variáveis se juntam e formam um único string

print(end7, end8, end9, end10, end11, end12)
# Separando as variáveis por vírgula, o resultado é B u r g e r (é impresso como uma sequência de variáveis separadas por espaço).
