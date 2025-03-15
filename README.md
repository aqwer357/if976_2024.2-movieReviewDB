
# proj2-if976_2024.2

Este repositório contém o projeto de implementação de um banco de dados para um sistema de resenhas de filmes. O objetivo é construir um sistema de gerenciamento e interação de dados relacionados a filmes, usuários e suas interações, como avaliações, favoritos e participações em produções cinematográficas. O projeto foi desenvolvido como parte do curso **IF976 - Banco de Dados**.

## Descrição do Repositório

Este repositório contém:

- **Estrutura do Banco de Dados**: As tabelas necessárias para armazenar informações sobre filmes, usuários, avaliações e interações.
- **Script de População de Dados**: Scripts SQL para povoar o banco de dados com dados de filmes e usuários para testar e utilizar o sistema.
- **Scripts Python**: Funções de integração com o banco de dados e manipulação dos dados armazenados.
- **Esquema Físico**: Descrição do modelo físico do banco de dados, representando as relações entre as tabelas e seus atributos.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e pastas:

```
if976_2024.2-movieReviewDB-main/
│
├── RunDB.py               # Script Python para interagir com o banco de dados
├── esquema-fisico/        # Diagramas e documentos explicativos do modelo físico
├── SQL Scripts/           # Scripts para criação e povoamento do banco de dados
└── README.md              # Este arquivo com a descrição do projeto
```

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- **Cadastro de Filmes**: Permite a inserção de dados relacionados a filmes, como nome, ano, duração, gênero, sinopse, diretor e idioma.
- **Interação com Filmes**: Usuários podem assistir, favoritar e avaliar filmes.
- **Participação de Membros**: Membros (atores, diretores) podem ser associados aos filmes, representando suas funções (ex: ator, diretor).

## Como Executar

Para executar este projeto, siga os passos abaixo:

### 1. Instalação

Clone este repositório para o seu ambiente local:

```bash
git clone <URL_DO_REPOSITORIO>
```

Instale as dependências necessárias (por exemplo, bibliotecas para interação com o banco de dados).

### 2. Configuração

Configure seu banco de dados (MySQL, PostgreSQL, etc.) e ajuste as credenciais no script Python `RunDB.py`.

### 3. Execução

Execute o script Python para interagir com o banco de dados e realizar operações como povoamento, consultas e manipulação de dados.

```bash
python RunDB.py
```
