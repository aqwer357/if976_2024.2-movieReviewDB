-- Sugestão de integração: transformar em variáveis os values

-- Consultas relacionadas a filmes

    -- Listar todos os filmes assistidos por 1 usuário
SELECT f.NOME FROM Filme f INNER JOIN Assistiu a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = 'Joao'
    -- Listar todos os filmes que 1 usuário quer assistir
SELECT f.NOME FROM Filme f INNER JOIN Assistira a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = 'Joao'
    -- Listar todos os filmes de 1 gênero
SELECT f.NOME FROM Filme f WHERE f.GENERO = 'TERROR'

-- Consultas relacionadas a avaliações:

    -- Listar todas as avaliações feitas por 1 usuário
    -- Listar todas as avaliações de 1 filme
SELECT r.USERNAME, r.NOTA, r.DESCRICAO FROM Avaliacao r WHERE r.ID_FILME = 'The Substance'

-- Consultas relacionadas a usuários:


-- Consultas relacionadas a solicitações:

-- RELATÓRIOS

-- Filmes mais assistidos por período:
-- Gêneros mais populares entre os usuários:
-- Filmes com melhor avaliação média:
-- Filmes com pior avaliação média:
-- Tags mais utilizadas em filmes assistidos:
-- Atores mais presentes em filmes assistidos:
-- Usuários mais ativos (avaliações, favoritos, assistidos):
-- Filmes assistidos por idioma:
-- ...