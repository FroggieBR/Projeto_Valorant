
# Django REST Framework Project

Este é um projeto básico de API desenvolvido com Django e Django REST Framework, criado para fins de estudo. O projeto inclui endpoints para gerenciar `Mapa`, `Personagem`, `Arma` e `Partida`, onde é possível realizar operações CRUD (Create, Read, Update, Delete) em cada um desses modelos.

## Funcionalidades

- **Mapas**: Gerenciamento dos mapas disponíveis.
- **Personagens**: Cadastro e consulta de personagens.
- **Armas**: Controle de armas e tipos disponíveis.
- **Partidas**: Registro e acompanhamento das partidas.

## Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- Django REST Framework

## Pré-requisitos

- [Python](https://www.python.org/) 3.7 ou superior
- [Git](https://git-scm.com/)
- Pip (geralmente incluído com o Python)
- Virtualenv (opcional, mas recomendado para isolar o ambiente do projeto)

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

5. Realize as migrações para configurar o banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

   Acesse o projeto em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Rotas da API

Aqui estão as principais rotas disponíveis na API. Todas as rotas suportam as operações padrão de CRUD, como `GET`, `POST`, `PUT`, `PATCH` e `DELETE`, dependendo da necessidade.

### Endpoints

1. **Mapa**
   - `GET /api/mapas/` - Lista todos os mapas.
   - `POST /api/mapas/` - Cria um novo mapa.
   - `GET /api/mapas/<id>/` - Retorna os detalhes de um mapa específico.
   - `PUT /api/mapas/<id>/` - Atualiza as informações de um mapa específico.
   - `DELETE /api/mapas/<id>/` - Exclui um mapa específico.

2. **Personagem**
   - `GET /api/personagens/` - Lista todos os personagens.
   - `POST /api/personagens/` - Cria um novo personagem.
   - `GET /api/personagens/<id>/` - Retorna os detalhes de um personagem específico.
   - `PUT /api/personagens/<id>/` - Atualiza as informações de um personagem específico.
   - `DELETE /api/personagens/<id>/` - Exclui um personagem específico.

3. **Arma**
   - `GET /api/armas/` - Lista todas as armas.
   - `POST /api/armas/` - Cria uma nova arma.
   - `GET /api/armas/<id>/` - Retorna os detalhes de uma arma específica.
   - `PUT /api/armas/<id>/` - Atualiza as informações de uma arma específica.
   - `DELETE /api/armas/<id>/` - Exclui uma arma específica.

4. **Partida**
   - `GET /api/partidas/` - Lista todas as partidas.
   - `POST /api/partidas/` - Cria uma nova partida.
   - `GET /api/partidas/<id>/` - Retorna os detalhes de uma partida específica.
   - `PUT /api/partidas/<id>/` - Atualiza as informações de uma partida específica.
   - `DELETE /api/partidas/<id>/` - Exclui uma partida específica.

## Utilização da API

Para testar a API, você pode utilizar ferramentas como [Postman](https://www.postman.com/) ou [cURL](https://curl.se/). Outra opção é acessar os endpoints diretamente pelo navegador, pois o Django REST Framework fornece uma interface de navegação automática para os endpoints quando o servidor está em modo de desenvolvimento.

### Exemplo de Requisição com cURL

```bash
# Listar todos os mapas
curl -X GET http://127.0.0.1:8000/api/mapas/

# Criar um novo mapa
curl -X POST http://127.0.0.1:8000/api/mapas/ -H "Content-Type: application/json" -d '{"nome": "Novo Mapa"}'
```

## Acesso ao Django Admin

Após criar o superusuário, você pode acessar o Django Admin para gerenciar os dados manualmente.

- URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Entre com as credenciais do superusuário criado anteriormente.

## Propósito do Projeto

Este projeto foi desenvolvido para estudo e prática com o Django e o Django REST Framework. Ele pode ser expandido com novas funcionalidades e é uma excelente base para aprender sobre desenvolvimento de APIs com Django.

## Licença

Este projeto é livre para uso pessoal e educacional. Sinta-se à vontade para modificar, compartilhar e contribuir.
