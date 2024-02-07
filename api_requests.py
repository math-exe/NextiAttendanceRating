import requests
from config import CLIENT_ID, CLIENT_SECRET

def getAcessToken():

    token_url = "https://api.nexti.com/security/oauth/token"

    # Parâmetros da solicitação
    params = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Cabeçalhos da solicitação
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic b3JiZW5rOjRlOWZhNTFiMTAwNDlkMzM0ZDljNDYyZWFjMjY3MDVkZGJmMTc3YjU="
    }

    try:
        # Realizar a solicitação para obter o token de acesso
        response = requests.post(token_url, params=params, headers=headers)
        response.raise_for_status()  # Lança um erro se a solicitação não for bem-sucedida

        # Extrai o token de acesso da resposta
        token_data = response.json()
        access_token = token_data.get('access_token')

        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o token de acesso: {e}")
        return None
    
def getAttendanceRating(access_token, dataInicio, dataFim):

    request_url = "https://orbenk.api.nexti.com/report/direct/attendanceRating"

    # Defina os parâmetros do payload conforme necessário
    payload = {
        "idsCustomer": [61],
        "startDate": None,
        "finishDate": None,
        "attendanceStartDate": dataInicio,
        "attendanceFinishDate": dataFim,
        "format": "XLS"
        # ... outros parâmetros ...
    }

    # Defina os cabeçalhos da requisição conforme necessário (especialmente o cabeçalho de autorização)
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Referer": "https://orbenk.nexti.com/",
        # ... outros cabeçalhos ...
    }

    # Realize a requisição POST
    response = requests.post(request_url, json=payload, headers=headers)

    return response