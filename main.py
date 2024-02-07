import api_requests
import date_handler
import spreadsheet_handler

# Retorna o token de acesso para a conexão com a API
access_token = api_requests.getAcessToken()

# Cálculos de data para o parâmetro de dataInicio e dataFim
dataInicio, dataFim = date_handler.dateReports()

# Pega a resposta da API
response = api_requests.getAttendanceRating(access_token=access_token, dataInicio=dataInicio, dataFim=dataFim)

# Verifique a resposta
if response.status_code == 200:
    # Salve o conteúdo em um arquivo local
    with open('output.xls', 'wb') as file:
        file.write(response.content)

    print("Arquivo salvo com sucesso!")
else:
    # Houve um erro na requisição
    print(f"Erro {response.status_code}: {response.text}")

# Realiza as alterações excluido informações inúteis no xls
modified_data = spreadsheet_handler.process_spreadsheet('output.xls')