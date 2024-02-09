import os
import pandas as pd

def process_spreadsheet(file_path):
    # Carregar o arquivo XLS
    xls = pd.ExcelFile(file_path)

    # Criar uma lista para armazenar DataFrames de cada página
    dfs = []

    # Excluir a segunda coluna em todas as páginas
    first_df = pd.read_excel(file_path, sheet_name=xls.sheet_names[0], header=None)
    first_df = first_df.drop(first_df.columns[1], axis=1)

    # Ajustar as colunas da primeira página
    first_df = first_df.drop([0, 1])
    first_df.columns = first_df.iloc[0]
    first_df = first_df[2:]
    dfs.append(first_df)

    # Iterar sobre todas as páginas no arquivo, ajustando as colunas
    for sheet_name in xls.sheet_names[1:]:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        df = df.drop(df.columns[1], axis=1)
        df.columns = first_df.columns  # Ajustar as colunas para serem iguais à primeira página
        dfs.append(df)

    # Concatenar todos os DataFrames
    result_df = pd.concat(dfs, ignore_index=True)

    # Salvar o resultado em um novo arquivo Excel
    #output_file_path = 'resultado_concatenacao.xlsx'
    #result_df.to_excel(output_file_path, index=False)
    #print(f'Resultado salvo em: {output_file_path}')

    # Retornar os dados modificados
    return result_df

def delete_file(file_path):
    # Verificar se o arquivo existe antes de tentar excluir
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'O arquivo {file_path} foi excluído com sucesso!')
    else:
        print(f'O arquivo {file_path} não existe.')