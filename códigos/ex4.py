"""Variáveis e nomes"""

# Variável = valor
cars = 100
space_in_a_car = 4.0
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Aqui está sendo realizada a concatenação das variáveis.
# Quando separamos as variáveis do restante da string por vírgulas, o nome dessa varíavel é substituído pelo seu valor.
# É possível realizar cálculos com os nomes das variáveis, quando estas representam números inteiros ou reais.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

"""
Qual a diferença entre = (igual simples) e == (igual duplo)? O sinal = (igual simples) atribui o valor à direita a uma variável à esquerda. O sinal == (igual duplo) testa para saber se duas coisas têm o mesmo valor.
"""

