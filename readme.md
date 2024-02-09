# Relatório Automatizado

Este projeto Python consiste em um script automatizado para obter dados de atendimento de uma API, realizar manipulações em uma planilha Excel local e inserir os dados resultantes em um banco de dados. A seguir, apresentamos uma descrição do código e sua estrutura.

## Estrutura de Arquivos

1. **main.py**: O script principal que coordena todas as operações.
2. **spreadsheet_handler.py**: Contém funções para processamento da planilha Excel.
3. **date_handler.py**: Fornece funções para manipulação de datas.
4. **database.py**: Gerencia a conexão com o banco de dados e insere os dados.
5. **api_requests.py**: Lida com as solicitações à API para obter o token de acesso e os dados de atendimento.
6. **config.py**: Arquivo de configuração para armazenar informações sensíveis como credenciais da API e do banco de dados.

## Como Usar

1. **Instalação de Dependências**: Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte comando:
   ```bash
   pip install pandas sqlalchemy requests
   ```


2. **Configuração** : Abra o arquivo `config.py` e insira suas credenciais de API e do banco de dados.
3. **Execução do Script** : Execute o script `main.py` para iniciar o processo automatizado. O script realizará as seguintes etapas:

* Obter o token de acesso da API.
* Calcular o intervalo de datas para a requisição à API.
* Realizar a requisição à API para obter os dados de atendimento.
* Salvar os dados em uma planilha Excel local chamada `output.xls`.
* Processar a planilha, realizando ajustes e removendo informações desnecessárias.
* Inserir os dados processados no banco de dados.

4. **Limpeza** : O script também apaga a planilha temporária `output.xls` após o processamento.

## Observações Importantes

* Certifique-se de proteger e manter em sigilo suas credenciais armazenadas no arquivo `config.py`.
* A execução do script pode ser agendada para automação recorrente, por exemplo, utilizando programadores de tarefas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull para melhorar este projeto.
