"""
FUNÇÕES E VARIÁVEIS


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Você tem {cheese_count} queijos!")
    print(f"Você tem {boxes_of_crackers} caixas de biscoitos!")
    print("cara isso é o suficiente para uma festa")
    print("Pegue um cobertor. \n")

print("Podemos apenas fornecer os números da função diretamente: ")
cheese_and_crackers(20,30)

print("Ou, podemos usar variáveis do nosso script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Podemos até fazer matemática dentro também:")
cheese_and_crackers(10 + 20, 5 + 6)

print("E nós podemos combinar os dois, variáveis e matemática:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

"""
def esposa_e_filhos(esposa_cont, num_filhos):
    print(f"Você tem {esposa_cont} esposa.")
    print(f"Você tem {num_filhos} filhos.")
    print("Isso é a sua família.")

# print("Fornecendo os números para a função acima: ")
esposa_e_filhos(1, 2)

# print("Podemos usar as variáveis esposa_cont e num_filhos.")
esposa_cont = 1
num_filhos = 2

# print("Usando a matemática: ")
esposa_e_filhos(1+0, 0+2)
print(f"Sua família é composta por {esposa_cont} esposa e {num_filhos} filhos.")
