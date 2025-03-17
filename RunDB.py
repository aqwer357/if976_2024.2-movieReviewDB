import psycopg2

DB_CONFIG = {
    "dbname": "seu_banco",
    "host": "localhost",
    "user": "postgres",
    "password": "pass",
    "port": 5432,
}

CONSULTAS_SQL = {
    "filmes_assistidos": """
        SELECT f.NOME 
        FROM Filme f 
        INNER JOIN Assistiu a ON a.ID_FILME = f.ID_FILME 
        WHERE a.USERNAME = %s;
    """,
    "filmes_para_assistir": """
        SELECT f.NOME 
        FROM Filme f 
        INNER JOIN Assistira a ON a.ID_FILME = f.ID_FILME 
        WHERE a.USERNAME = %s;
    """,
    "filmes_por_genero": "SELECT f.NOME FROM Filme f WHERE f.GENERO = %s;",
    "filmes_por_tag": """
        SELECT f.NOME 
        FROM Filme f 
        JOIN Tags t ON f.ID_FILME = t.ID_FILME 
        WHERE t.TAG = %s;
    """,
    "filmes_por_ator": """
        SELECT f.NOME 
        FROM Filme f 
        JOIN Participou p ON f.ID_FILME = p.ID_FILME 
        WHERE p.NOME = %s;
    """,
    "filmes_por_diretor": "SELECT NOME FROM Filme WHERE DIRETOR = %s;",
    "filmes_por_idioma": "SELECT NOME FROM Filme WHERE IDIOMA = %s;",
    "filmes_comuns_dois_usuarios": """
        SELECT f.NOME 
        FROM Filme f 
        JOIN Assistiu a1 ON f.ID_FILME = a1.ID_FILME 
        JOIN Assistiu a2 ON f.ID_FILME = a2.ID_FILME 
        WHERE a1.USERNAME = %s AND a2.USERNAME = %s;
    """,
    "filmes_favoritados_usuario": """
        SELECT f.NOME 
        FROM Filme f 
        JOIN Favoritou fav ON f.ID_FILME = fav.ID_FILME 
        WHERE fav.USERNAME = %s;
    """,
    "usuarios_registrados": "SELECT USERNAME FROM Pessoa;",
    "usuarios_assistiram_filme": "SELECT USERNAME FROM Assistiu WHERE ID_FILME = %s;",
    "usuarios_favoritaram_filme": "SELECT USERNAME FROM Favoritou WHERE ID_FILME = %s;",
    "usuarios_mais_filmes_favoritados": """
        SELECT USERNAME, COUNT(ID_FILME) AS NUM_FAVORITOS 
        FROM Favoritou 
        GROUP BY USERNAME 
        ORDER BY NUM_FAVORITOS DESC 
        LIMIT 10;
    """,
    "solicitacoes_pendentes": """
        SELECT s.ID_SOLICITACAO, s.NOME 
        FROM Solicitacao_Filme s 
        LEFT JOIN Aprova a ON a.ID_FILME = s.ID_SOLICITACAO 
        WHERE a.ID_FILME IS NULL;
    """,
    "solicitacoes_aprovadas": """
        SELECT s.ID_SOLICITACAO, s.NOME 
        FROM Solicitacao_Filme s 
        JOIN Aprova a ON s.ID_SOLICITACAO = a.ID_FILME 
        WHERE a.USERNAME = %s;
    """,
}

def conectar_banco():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        return None

def executar_consulta(cursor, query_key, parametros=()):
    query = CONSULTAS_SQL.get(query_key)
    if not query:
        print("❌ Consulta não encontrada.")
        return
    
    try:
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()
        
        if resultados:
            print("\n🔹 Resultados encontrados:")
            for linha in resultados:
                print(linha)
        else:
            print("⚠ Nenhum resultado encontrado.")
    except Exception as e:
        print(f"❌ Erro ao executar consulta: {e}")

def menu(cursor):
    while True:
        print("\n### MENU ###")
        print("1️⃣  - Listar filmes assistidos por um usuário")
        print("2️⃣  - Listar filmes que um usuário quer assistir")
        print("3️⃣  - Listar filmes por gênero")
        print("4️⃣  - Listar filmes por tag")
        print("5️⃣  - Listar filmes por ator")
        print("6️⃣  - Listar filmes por diretor")
        print("7️⃣  - Listar filmes por idioma")
        print("8️⃣  - Listar filmes em comum entre dois usuários")
        print("9️⃣  - Listar filmes favoritados por um usuário")
        print("🔟  - Listar usuários registrados")
        print("1️⃣1️⃣ - Listar usuários que assistiram um filme")
        print("1️⃣2️⃣ - Listar usuários que favoritaram um filme")
        print("1️⃣3️⃣ - Listar usuários com mais filmes favoritados")
        print("1️⃣4️⃣ - Listar solicitações pendentes")
        print("1️⃣5️⃣ - Listar solicitações aprovadas por um administrador")
        print("0️⃣  - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            usuario = input("🔹 Digite o nome de usuário: ").strip()
            executar_consulta(cursor, "filmes_assistidos", (usuario,))
        elif opcao == "2":
            usuario = input("🔹 Digite o nome de usuário: ").strip()
            executar_consulta(cursor, "filmes_para_assistir", (usuario,))
        elif opcao == "3":
            genero = input("🔹 Digite o gênero do filme: ").strip()
            executar_consulta(cursor, "filmes_por_genero", (genero,))
        elif opcao == "4":
            tag = input("🔹 Digite a tag do filme: ").strip()
            executar_consulta(cursor, "filmes_por_tag", (tag,))
        elif opcao == "5":
            ator = input("🔹 Digite o nome do ator: ").strip()
            executar_consulta(cursor, "filmes_por_ator", (ator,))
        elif opcao == "6":
            diretor = input("🔹 Digite o nome do diretor: ").strip()
            executar_consulta(cursor, "filmes_por_diretor", (diretor,))
        elif opcao == "7":
            idioma = input("🔹 Digite o idioma do filme: ").strip()
            executar_consulta(cursor, "filmes_por_idioma", (idioma,))
        elif opcao == "8":
            usuario1 = input("🔹 Digite o primeiro usuário: ").strip()
            usuario2 = input("🔹 Digite o segundo usuário: ").strip()
            executar_consulta(cursor, "filmes_comuns_dois_usuarios", (usuario1, usuario2))
        elif opcao == "9":
            usuario = input("🔹 Digite o nome de usuário: ").strip()
            executar_consulta(cursor, "filmes_favoritados_usuario", (usuario,))
        elif opcao == "10":
            executar_consulta(cursor, "usuarios_registrados")
        elif opcao == "11":
            id_filme = input("🔹 Digite o ID do filme: ").strip()
            executar_consulta(cursor, "usuarios_assistiram_filme", (id_filme,))
        elif opcao == "12":
            id_filme = input("🔹 Digite o ID do filme: ").strip()
            executar_consulta(cursor, "usuarios_favoritaram_filme", (id_filme,))
        elif opcao == "14":
            executar_consulta(cursor, "solicitacoes_pendentes")
        elif opcao == "15":
            admin = input("🔹 Digite o nome do administrador: ").strip()
            executar_consulta(cursor, "solicitacoes_aprovadas", (admin,))
        elif opcao == "0":
            print("🚪 Saindo...")
            break
        else:
            print("❌ Opção inválida! Escolha um número válido.")

if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        with conn.cursor() as cursor:
            menu(cursor)
        conn.close()
