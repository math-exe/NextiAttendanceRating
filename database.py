from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from config import SERVER, DATABASE, USERNAME, PASSWORD

def insert_into_database(df):
    # Configurações do banco de dados
    server = SERVER
    database = DATABASE
    username = USERNAME
    password = PASSWORD

    # Cria a string de conexão para o SQLAlchemy
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

    try:
        # Tenta criar uma conexão com o banco de dados
        engine = create_engine(connection_string)
        connection = engine.connect()
        print("Conexão bem-sucedida!")

        # Se a conexão for bem sucedida, então, enviar as informações de df para o banco de dados, dentro da tabela 'NEXTI_AVATEN'.
        rows_inserted = df.to_sql('NEXTI_AVATEN', con=engine, if_exists='replace', index=False)
        print(f"{rows_inserted} linhas inseridas no banco de dados.")
        return rows_inserted
    except SQLAlchemyError as error:
        print("Falha na conexão!")
        print(error)
        return 0  # Retorna 0 em caso de falha
    finally:
        # Fecha a conexão com o banco de dados
        connection.close()
        engine.dispose()
        print("Conexão Finalizada!")