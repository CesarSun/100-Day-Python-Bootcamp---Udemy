print("      ____                     ")
print("     |  __| __  __  ___  ___   ")
print("     | |__ |__ |__ | o || o_|  ")
print("     |____||__  __||_|_||_|\_\ ")
print("      ____                        ")
print("     |  __|    __       __  ___   ")
print("     | |__  | |__||__| |__ | o_|  ")
print("     |____| | |   |  | |__ |_|\_\ ")

import pandas as pd

def cifra_cesar(texto, chave, modo):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            ascii_inicial = ord('a') if letra.islower() else ord('A')
            if modo == "codificar":
                indice = (ord(letra) - ascii_inicial + chave) % 26
            elif modo == "decodificar":
                indice = (ord(letra) - ascii_inicial - chave) % 26
            nova_letra = chr(indice + ascii_inicial)
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

def criar_tabela_codificada(limite):
    frases_limite = list(range(1, limite + 1))
    tabela_codificada = pd.DataFrame(index=frases_limite, columns=["Chaves", "Frases"])
    return tabela_codificada

def codificar_frase(tabela_codificada, posicao):
    frase = input("Digite a mensagem: ")
    chave = int(input("Digite a chave de deslocamento: "))
    frase_codificada = cifra_cesar(frase, chave, "codificar")
    print("Frase codificada: ", frase_codificada)
    tabela_codificada.at[posicao, "Frases"] = frase_codificada
    tabela_codificada.at[posicao, "Chaves"] = chave
    posicao += 1
    print("Tabela codificada: ", "\n", tabela_codificada.loc[:,"Frases"])
    return tabela_codificada, posicao

def substituir_frase(tabela_codificada):
    posicao = input("Tabela cheia, escolha uma frase para substituir:")
    frase = input("Digite a mensagem: ")
    chave = int(input("Digite a chave de deslocamento: "))
    frase_codificada = cifra_cesar(frase, chave, "codificar")
    print("Frase codificada: ", frase_codificada)
    tabela_codificada.at[posicao, "Frases"] = frase_codificada
    tabela_codificada.at[posicao, "Chaves"] = chave
    posicao = 11
    print("Tabela codificada: ", "\n", tabela_codificada.loc[:,"Frases"])
    return tabela_codificada

def decodificar_frase(tabela_codificada):
    print("Tabela codificada:\n")
    print(tabela_codificada.loc[:, ["Frases"]].to_string(index=True))
    
    tentativas = 0
    while tentativas < 3:
        try:
            indice = int(input("Digite o índice da frase que deseja decodificar: "))
            indices_disponiveis = tabela_codificada.index.tolist()
            if indice in indices_disponiveis:
                frase = tabela_codificada.loc[indice, "Frases"]
                chave = tabela_codificada.loc[indice, "Chaves"]
                if pd.notna(frase) and isinstance(frase, str):
                    chave_input = int(input("Digite a chave de deslocamento: "))
                    if chave == chave_input:
                        frase_decodificada = cifra_cesar(frase, chave, "decodificar")
                        print("Frase decodificada: ", frase_decodificada)
                        break
                    else:
                        print("Chave incorreta. Tente novamente.")
                        tentativas += 1
                else:
                    print("Não existe frase para decodificar nessa posição! Tente novamente.")
                    tentativas += 1
            else:
                print("Não existe frase para decodificar nessa posição! Tente novamente.")
                tentativas += 1
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    if tentativas == 3:
        print("Número máximo de tentativas atingido. O programa será encerrado.")


def main():
    sair = True
    posicao = 1
    limite = 10
    tabela_codificada = criar_tabela_codificada(limite)

    while sair:
        opcao = input("Deseja codificar (C), decodificar (D) ou sair (S)? ")

        if opcao.lower() == "c":
            if posicao <= limite:
                tabela_codificada, posicao = codificar_frase(tabela_codificada, posicao)
            else:
                tabela_codificada = substituir_frase(tabela_codificada)

        elif opcao.lower() == "d":
            decodificar_frase(tabela_codificada)

        elif opcao.lower() == "s":
            sair = False

        else:
            print("Opção inválida. O programa será encerrado.")
            sair = False

main()