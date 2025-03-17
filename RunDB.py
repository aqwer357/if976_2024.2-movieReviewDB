import psycopg2
import os

DB_NAME = "seu_banco"
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASSWORD = "pass"
DB_PORT = 5432

CONSULTAS_SQL = {
    "filmes_assistidos": "SELECT f.NOME FROM Filme f INNER JOIN Assistiu a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = %s;",
    "filmes_para_assistir": "SELECT f.NOME FROM Filme f INNER JOIN Assistira a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = %s;",
    "filmes_por_genero": "SELECT f.NOME FROM Filme f WHERE f.GENERO = %s;",
    "avaliacoes_filme": "SELECT r.USERNAME, r.NOTA, r.DESCRICAO FROM Avaliacao r WHERE r.ID_FILME = %s;",
    "solicitacoes_pendentes": "SELECT s.ID_SOLICITACAO, s.NOME FROM Solicitacao_Filme s LEFT JOIN Aprova a ON a.ID_FILME = s.ID_SOLICITACAO WHERE a.ID_FILME IS NULL;",
    "usuarios_mais_ativos": "SELECT USERNAME, COUNT(*) AS TOTAL FROM Avaliacao GROUP BY USERNAME ORDER BY TOTAL DESC LIMIT 10;",
    "filmes_mais_assistidos": """
        SELECT f.NOME, COUNT(a.USERNAME) AS TOTAL 
        FROM Filme f JOIN Assistiu a ON f.ID_FILME = a.ID_FILME 
        GROUP BY f.NOME ORDER BY TOTAL DESC LIMIT 10;
    """,
}

def conectar_banco():
    """ Conecta ao banco de dados PostgreSQL. """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def inicializar_banco(conn):
    """ Inicializa o banco de dados criando e populando as tabelas. """
    script_dir = os.path.dirname(__file__)
    dbFolderPath = os.path.join(script_dir, 'esquema-fisico')

    try:
        with conn.cursor() as cursor:
            if os.path.exists(os.path.join(dbFolderPath, 'CRIACAO.sql')):
                with open(os.path.join(dbFolderPath, 'CRIACAO.sql'), 'r', encoding='utf-8') as createDBFile:
                    cursor.execute(createDBFile.read())

            if os.path.exists(os.path.join(dbFolderPath, 'POVOAMENTO.sql')):
                with open(os.path.join(dbFolderPath, 'POVOAMENTO.sql'), 'r', encoding='utf-8') as insertFile:
                    cursor.execute(insertFile.read())

            conn.commit()
            print("Banco de dados inicializado com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inicializar o banco: {e}")

def executar_consulta(cursor, query_key, parametros=()):
    """ Executa uma consulta SQL e exibe os resultados. """
    try:
        query = CONSULTAS_SQL.get(query_key)
        if not query:
            print("Consulta não encontrada.")
            return
        
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()
        
        if resultados:
            for linha in resultados:
                print(linha)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao executar consulta: {e}")

def menu(cursor):
    """ Menu interativo para consultas no banco de dados. """
    while True:
        print("\n### MENU ###")
        print("1 - Listar todos os filmes assistidos por um usuário")
        print("2 - Listar todos os filmes que um usuário quer assistir")
        print("3 - Listar todos os filmes de um gênero")
        print("4 - Listar todas as avaliações de um filme")
        print("5 - Listar solicitações de filmes pendentes de aprovação")
        print("6 - Listar os usuários mais ativos (avaliações, favoritos, assistidos)")
        print("7 - Listar os filmes mais assistidos")
        print("8 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            usuario = input("Digite o nome de usuário: ").strip()
            executar_consulta(cursor, "filmes_assistidos", (usuario,))

        elif opcao == "2":
            usuario = input("Digite o nome de usuário: ").strip()
            executar_consulta(cursor, "filmes_para_assistir", (usuario,))

        elif opcao == "3":
            genero = input("Digite o gênero do filme: ").strip()
            executar_consulta(cursor, "filmes_por_genero", (genero,))

        elif opcao == "4":
            filme_id = input("Digite o ID do filme: ").strip()
            if not filme_id.isdigit():
                print("Erro: O ID do filme deve ser um número.")
                continue
            executar_consulta(cursor, "avaliacoes_filme", (int(filme_id),))

        elif opcao == "5":
            executar_consulta(cursor, "solicitacoes_pendentes")

        elif opcao == "6":
            executar_consulta(cursor, "usuarios_mais_ativos")

        elif opcao == "7":
            executar_consulta(cursor, "filmes_mais_assistidos")

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Escolha uma opção de 1 a 8.")

if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        with conn.cursor() as cursor:
            resposta = input("O banco já foi inicializado? (Y/N): ").strip().upper()
            if resposta == "N":
                inicializar_banco(conn)

            menu(cursor)

        conn.close()
