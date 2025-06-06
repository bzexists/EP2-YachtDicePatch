import random

def rolar_dados(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1, 6))
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados[dado_para_guardar]
    dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(valor)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    valor = dados_no_estoque[dado_para_remover]
    dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(valor)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(lista):
    pontuacao = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in lista:
        if dado in pontuacao:
            pontuacao[dado] += dado
    return pontuacao
