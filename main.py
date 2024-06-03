import sys
import json
import csv
import time
import os


def ler_automato(caminho):
    if not os.path.exists(caminho):
        print(f"O arquivo {caminho} não foi encontrado.")
        return None
    with open(caminho, 'r', encoding='utf-8') as file:
        automato = json.load(file)
    return automato


def ler_entradas(caminho):
    if not os.path.exists(caminho):
        print(f"O arquivo {caminho} não foi encontrado.")
        return None
    entradas = []
    with open(caminho, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row:  
                if len(row) >= 2:  
                    entradas.append((row[0], int(row[1])))
                else:
                    print(f"A linha não possui informações suficientes: {row}")
            else:
                print("A linha está vazia.")
    return entradas


def simular_automato(automato, palavra):
    estado_atual = automato['initial']
    estados_finais = automato['final']
    transicoes = automato['transitions']

    for simbolo in palavra:
        proximo_estado = None
        for transicao in transicoes:
            if transicao['from'] == estado_atual and transicao['read'] == simbolo:
                proximo_estado = transicao['to']
                break
        if proximo_estado is None:
            return 0  
        estado_atual = proximo_estado

    return 1 if estado_atual in estados_finais else 0  


def main(arquivo_aut, arquivo_teste, arquivo_saida):
    automato = ler_automato(arquivo_aut)
    if automato is None:
        return
    entradas = ler_entradas(arquivo_teste)
    if entradas is None:
        return
    resultados = []

    for entrada, resultado_esperado in entradas:
        inicio = time.time()
        resultado_obtido = simular_automato(automato, entrada)
        fim = time.time()
        tempo = fim - inicio
        resultados.append((entrada, resultado_esperado, resultado_obtido, tempo))

    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for resultado in resultados:
            writer.writerow(resultado)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python automato.py <arquivo_aut.aut> <arquivo_teste.in> <arquivo_saida.out>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])