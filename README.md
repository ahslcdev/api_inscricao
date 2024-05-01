Este projeto é parte de um desafio de desenvolvimento e visa implementar uma aplicação utilizando diversas tecnologias e práticas de desenvolvimento.

## Tecnologias Utilizadas

- Python
- FastAPI
- TinyDB
- RabbitMQ
- Redis
- Docker

## Funcionalidades Implementadas

O projeto foi dividido em 2 apis, cada uma com as suas funcionalidades.

### API de Idades
- Adicionar novo grupo de idades
- Deletar um grupo de idades
- Visualizar grupos de idades
Para esta API, todos os endpoints deveriam exigir autenticação básica proveniente de um arquivo estático que encontra-se no diretorio app/apis/age_api/credentials.json.

### API de Inscrição
- Solicitar inscrição
- Checar o status da inscrição
Ademais, para desenvolver as funcionalidades desta API, era obrigatório utilizar algum serviço de filas e que para processar a inscrição do cliente, deveria ter um tempo mínimo de 2 segundos.

## Como Rodar o Projeto e os Testes

1. Certifique-se de ter o Docker instalado na sua máquina.
2. Clone este repositório: `git clone https://github.com/ahslcdev/api_inscricao`
3. Navegue até o diretório do projeto: `cd api_inscricao`
4. Construa a imagem do Docker e inicie os serviços: `docker compose up -d --build`
5. Execue os testes: `docker run enrollment_api pytest` / `docker run age_api pytest`

Agora é possível acessar as APIs nos seguintes endereços
- API de Idades `http://localhost:8000/docs`
- API de Inscrição `http://localhost:8080/docs`
- Celery Flower `http://localhost:5556`