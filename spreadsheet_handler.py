import os
import pandas as pd

def process_spreadsheet(file_path):
    # Carregar o arquivo XLS
    df = pd.read_excel(file_path, header=None)  # Desativar o cabeçalho existente

    # Excluir as linhas 1 e 2
    df = df.drop([0, 1])

    # Definir a linha 3 como cabeçalho
    df.columns = df.iloc[0]
    df = df[2:]

    # Excluir a segunda coluna
    df = df.drop(df.columns[1], axis=1)

    # Print de confirmação
    print('Dados modificados com sucesso!')

    # Exibir as 10 primeiras linhas do DataFrame
    print('Primeiras 4 linhas do DataFrame após as modificações:')
    print(df.head(4))

    # Retornar os dados modificados
    return df

def delete_file(file_path):
    # Verificar se o arquivo existe antes de tentar excluir
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'O arquivo {file_path} foi excluído com sucesso!')
    else:
        print(f'O arquivo {file_path} não existe.')