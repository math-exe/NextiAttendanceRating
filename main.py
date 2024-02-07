import api_requests
import date_handler

access_token = api_requests.getAcessToken()

dataInicio, dataFim = date_handler.dateReports()

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