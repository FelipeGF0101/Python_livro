"""
O caractere \ (barra invertida) codifica os caracteres difíceis de digitar em uma string. Há várias sequências de escape disponíveis para diferentes caracteres que você pode querer usar.
Uma sequência importante é aplicar o escape em uma aspas simples (') ou dupla ("). Imagine que você tenha uma string que usa aspas duplas e deseja colocar uma aspas duplas dentro dela. Se escrever "I "understand" Joe", o python ficará confuso, porque pensará que as aspas duplas em torno de "understand" realmente terminam a string. Você precisa de um modo de informar ao python que as aspas duplas dentro da string não são reais.
Para resolver o problema, você deve aplicar o escape nas aspas duplas e simples para que o Python as inclua na string. Veja um exemplo:

"I am 6'2\" tall." # escape de aspas duplas dentro da string
'I am 6\'2" tall.' # escape de aspas simples dentro da string

O segundo modo é usando aspas triplas, que são apenas (""') e funcionam como uma string, mas você também pode colocar quantas linhas de texto desejar até digitar (""') de novo. Também iremos experimentar isso. 

"""
tabby_cat = "\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm\\ a \\ cat."

fat_cat="""
I'll do a list:
\t* Cat foot
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#SEQUÊNCIAS DE ESCAPE

#Escape ===== O que faz:

#\\     ===== Barra invertida (\)
#\'     ===== Aspas simples(')
#\"     ===== Aspas duplas (")
#\a     ===== Campainha ASCII (BEL)
#\b     ===== Retorno ASCII (BS)
#\f     ===== Avanço de página ASCII(FF)
#\n     ===== Nova linha ASCII (LF)
#\N{name} === Caractere name no banco de dados Unicode (unicode apenas)
#\r     ===== Retorno de carro (CR)
#\t     ===== Tabulação Horizontal (TAB)
#\uxxxx ===== Caractere com valor hex de 16 bits xxxx
#\Uxxxxxxxx = Caractere com valor hex de 32 bits xxxxxxxx
#\v     ===== Tabulação vertical ASCII(VT)
#\ooo   ===== Caractere com valor ooo
#\xhh   ===== Caractere com o valor hex hh

print('\nFelipe', '\nGuedes')
print('\n\tFelipe','\n\tGuedes')
print('\n\a Felipe', '\nGuedes')
print('\vFelipe')
print('\b Felipe')
print('\fFelipeGuedes')
print('\rFelipe Guedes')