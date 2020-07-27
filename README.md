# Petshop

<p>Esta é uma aplicação feita em Django que oferece um CRUD de Pets, simulando um Petshop Canino bem simples.</p>

<h2>Como Executar</h2>

<p>Siga a lista de comandos abaixo para organizar todas as necessidades e fazer com que a aplicação execute.</p>
<p>Obs.: Este projeto foi criado utilizando o python 3.8. Sugiro que o utilize para evitar conflitos que possam acontecer a partir do versionamento dos pacotes.</p>
<ol>
  <li>Crie o ambiente virtual do projeto: python3 -m venv venv</li>
  <li>Ative-o: source venv/bin/activate</li>
  <li>Instale suas dependências: pip3 install -r requirements.txt</li>
  <li>Crie o banco de dados executando as migrations: python3 manage.py migrate</li>
  <li>Crie um usuário primário: python3 manage.py createsuperuser</li>
  <li>Inicie o Servidor: python3 manage.py runserver</li>
</ol>

<p>E pronto, a aplicação estará executando de forma local na porta 8000.</p>

<h2>Objetos</h2>

<p>Na aplicação, os Pets seguem o seguinte modelo de objeto, tanto na adição quanto no retorno do mesmo:</p>
```
{
  "id": "Presente somente no retorno das requisições GET, PUT e POST.",
  "nome": "Nome do pet. Facultativo.",
  "raca": "A raça do pet. Utiliza de um dos tipos descritos abaixo.",
  "idade": "A idade do pet. Facultativo."
}
```

<p>Opções na inserção de raças (choices):</p>
```
[
  'LAB', // Labrador
  'BUL', // Boldogue
  'POO', // Poodle
  'PAS', // Pastor Alemão
  'BEA', // Beagle
  'GOL', // Golden Retriever
  'CHI', // Chihuahua
  'HUS', // Husky Siberiano
]
```

<h2>Requisições</h2>

<p>Abaixo está uma tabela de requisições em relação aos pets.</p>

| Método | URL                 | Descrição                                    |
| GET    | /api/core/pets      | Retorna todos os pets.                       |
| GET    | /api/core/pets/:id  | Retorna um único pet com o id fornecido.     |
| POST   | /api/core/pets      | Adiciona um pet seguindo o modelo de objeto. |
| PUT    | /api/core/pets/:id  | Altera um pet de acordo com o id fornecido.  |
| DELETE | /api/core/pets/:id  | Deleta um pet de acordo com o id fornecido.  |