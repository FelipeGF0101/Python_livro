"""
Aqui veremos como fazer formatação de string mais complicada.
"""
# Neste exercício, estou usando algo chamado função para transformar a variável formatter em outras strings. Quando me vir escrever formatter.format(...), estou informando ao Python para fazer o seguinte:
# Pegar a string formatter definida na linha 1
# Chamar sua função format, que é como pedir para executar um comando da linha de comando denominado format.
# Passar quatro argumentos para format, que correspondem às quatro {}s na variável formatter. É como passar argumentos para o comando format da linha de comando.
# O resultado de chamar format em formatter é uma nova string com as {} substituídas por quatro variáveis. Isso é o que o print imprime.

# Aqui foi determinado que cada string contenha apenas 4 valores. Se um par de chaves for apagado, um valor de cada string abaixo deixa de ser imprimido na tela.
formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# COMPLEMENTO DO COMENTÁRIO ACIMA = Se for adicionado valores a mais do que o limite estabelecido em 'formatter', o programa irá simplesmente ignorá-los. Porém, se forem valores a menos, o programa retornará error.
formatter = '{} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('hello', 'world'))
print(formatter.format(True, False))

