from datetime import date, datetime, timedelta

def dateReports():

    # Data Atual
    today = date.today()

    # Ano Anterior
    anoAnterior = today.year - 1

    # Primeiro dia do ano anterior
    primeiroDiaAnoAnterior = datetime(anoAnterior, 1, 1)

    # Data Final para o intervalo de consulta na requisição
    dataInicio = primeiroDiaAnoAnterior.strftime("%Y-%m-%d")

    # Data Inicial para o intervalo de consulta na requisição
    dataFim = today.strftime("%Y-%m-%d")

    return dataInicio, dataFim