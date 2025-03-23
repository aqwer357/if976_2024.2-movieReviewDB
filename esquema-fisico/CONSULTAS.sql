-- Sugestão de integração: transformar em variáveis os values

-- Consultas relacionadas a filmes

    -- Listar todos os filmes assistidos por 1 usuário
SELECT f.NOME FROM Filme f INNER JOIN Assistiu a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = 'ricardocavalcante';
    -- Listar todos os filmes que 1 usuário quer assistir
SELECT f.NOME FROM Filme f INNER JOIN Assistira a ON a.ID_FILME = f.ID_FILME WHERE a.USERNAME = 'leoncio';
    -- Listar todos os filmes de 1 gênero
SELECT f.NOME FROM Filme f WHERE f.GENERO = 'Terror';

-- Consultas relacionadas a avaliações:

    -- Listar todas as avaliações feitas por 1 usuário
    -- Listar todas as avaliações de 1 filme
SELECT r.USERNAME, r.NOTA, r.DESCRICAO FROM Avaliacao r WHERE r.ID_FILME = 1;

-- Consultas relacionadas a usuários:


-- Consultas relacionadas a solicitações:
    -- Listar todas as solicitações de filmes pendentes de aprovação
SELECT s.ID_SOLICITACAO, s.NOME FROM Solicitacao_Filme s LEFT OUTER JOIN Aprova a ON s.ID_SOLICITACAO = a.ID_SOLICITACAO WHERE a.ID_SOLICITACAO is NULL;    
    -- Listar todas as solicitações de filmes aprovadas
SELECT s.ID_SOLICITACAO, s.NOME FROM Solicitacao_Filme s RIGHT OUTER JOIN Aprova a ON a.ID_SOLICITACAO = s.ID_SOLICITACAO;
-- RELATÓRIOS

-- Filmes mais assistidos por período:
-- Gêneros mais populares entre os usuários:
-- Filmes com melhor avaliação média:
-- Filmes com pior avaliação média:
-- Tags mais utilizadas em filmes:
SELECT TAG, COUNT(TAG) FROM Tags GROUP BY TAG ORDER BY COUNT(TAG) DESC;
-- Atores mais presentes em filmes assistidos:
-- Usuários mais ativos (avaliações, favoritos, assistidos):
-- Filmes assistidos por idioma:
-- ...