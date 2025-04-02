# exercicios.py

# 1. Função que recebe uma lista de números e retorna outra lista com os números ímpares
def filtra_impares(numeros):
    impares = []
    for num in numeros:
        if num % 2 != 0:
            impares.append(num)
    return impares

# Teste da função de números ímpares
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Números ímpares:", filtra_impares(lista1))


# 2. Função que recebe uma lista de números e retorna outra lista com os números primos presentes
def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtra_primos(numeros):
    primos = []
    for num in numeros:
        if eh_primo(num):
            primos.append(num)
    return primos

# Teste da função de números primos
lista2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Números primos:", filtra_primos(lista2))


# 3. Função que recebe duas listas e retorna outra lista com os elementos que estão presentes em apenas uma das listas
def elementos_unicos(lista1, lista2):
    unicos = []
    for item in lista1:
        if item not in lista2:
            unicos.append(item)
    for item in lista2:
        if item not in lista1:
            unicos.append(item)
    return unicos

# Teste da função de elementos únicos
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print("Elementos únicos:", elementos_unicos(l1, l2))


# 4. Função para encontrar o segundo maior valor em uma lista de números inteiros
def segundo_maior(lista):
    unicos = list(set(lista))
    unicos.sort()
    if len(unicos) < 2:
        return None
    return unicos[-2]

# Teste da função de segundo maior valor
lista3 = [5, 3, 9, 1, 9, 4]
print("Segundo maior valor:", segundo_maior(lista3))


# 5. Função que recebe uma lista de tuplas (nome, idade) e retorna a lista ordenada pelo nome em ordem alfabética
def ordena_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda pessoa: pessoa[0])

# Teste da função de ordenação por nome
pessoas = [("Carlos", 25), ("Ana", 30), ("Bruna", 22)]
print("Pessoas ordenadas pelo nome:", ordena_por_nome(pessoas))


# 6. Código com matplotlib e numpy - criando subplots com anotações
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                                transform=axs[row, col].transAxes,
                                ha='center', va='center', fontsize=18,
                                color='darkgrey')
fig.suptitle('plt.subplots()')
plt.show()


# 7. Código com matplotlib e numpy - plotando o seno
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# 8. Leitura de um arquivo CSV utilizando pandas e exibição das primeiras linhas
import pandas as pd

# Substitua 'dados.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('dados.csv')
print("Primeiras linhas do DataFrame:")
print(df.head())


# 9. Selecionar uma coluna específica e filtrar linhas em um DataFrame
# Selecionando a coluna 'idade' e filtrando linhas onde a idade é maior que 30
coluna_idade = df['idade']
filtrado = df[df['idade'] > 30]
print("\nColuna 'idade':")
print(coluna_idade)
print("\nLinhas com idade maior que 30:")
print(filtrado)


# 10. Lidar com valores ausentes (NaN) em um DataFrame
# Exemplo 1: Preencher valores ausentes com 0
df_preenchido = df.fillna(0)

# Exemplo 2: Remover as linhas que contenham valores ausentes
df_sem_nan = df.dropna()

print("\nDataFrame com valores preenchidos (NaN substituídos por 0):")
print(df_preenchido.head())
print("\nDataFrame sem valores ausentes:")
print(df_sem_nan.head())
