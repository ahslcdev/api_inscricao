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
5. Execute os testes: `docker-compose run enrollment_api python -m pytest` / `docker-compose run age_api python -m pytest`

Agora é possível acessar as APIs nos seguintes endereços
- API de Idades `http://localhost:8000/docs`
- API de Inscrição `http://localhost:8080/docs`
- Celery Flower `http://localhost:5556`

## Informações adicionais
- O RabbitMQ foi utilizado como broker do projeto e o Redis foi utilizado para armazenar os resultados, porém é possível colocar o Redis como broker, basta apenas informa na váriavel de ambiente a URL `redis://redis:6379/0/`.
- A escolha do TinyDB se deu pela simplicidade em utiliza-lo
- Para autenticar, deve-se utilizar o usuário `admin` com a senha `123`