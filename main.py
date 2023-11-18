def comparar_arquivos(arquivo1, arquivo2, arquivo_saida):
    with open(arquivo1, 'r', encoding='utf-8') as f1, open(arquivo2, 'r', encoding='utf-8') as f2:
        linhas_arquivo1 = f1.readlines()
        linhas_arquivo2 = f2.readlines()

    diferencas = set(linhas_arquivo1) - set(linhas_arquivo2)

    with open(arquivo_saida, 'w', encoding='utf-8') as f_saida:
        f_saida.writelines(diferencas)

if __name__ == "__main__":
    arquivo1 = "meuglobal.ini"
    arquivo2 = "global.ini"
    arquivo_saida = "alteracoes.ini"

    comparar_arquivos(arquivo1, arquivo2, arquivo_saida)

    print("Diferenças encontradas e salvas em 'alteracoes.txt'")
