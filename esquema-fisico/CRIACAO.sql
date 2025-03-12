CREATE TABLE Pessoa(
    USERNAME varchar(255) PRIMARY KEY,
    EMAIL varchar(255) NOT NULL,
    SENHA varchar(255) NOT NULL
);

CREATE TABLE U_Publico(
    USERNAME varchar(255) primary key references Pessoa(USERNAME)
);

CREATE TABLE U_Admin( 
    USERNAME varchar(255) primary key references Pessoa(USERNAME),
    NOME varchar(255) NOT NULL,
    CODIGO integer NOT NULL
);

CREATE TABLE Filme(
    NOME varchar(255) NOT NULL,
    ANO integer NOT NULL,
    ID_FILME integer PRIMARY KEY,
    DURACAO integer NOT NULL,
    GENERO varchar(255) NOT NULL,
    SINOPSE varchar(255) NOT NULL,
    DIRETOR varchar(255) NOT NULL,
    IDIOMA varchar(255) NOT NULL,
    NOTA_AGREGADA NUMERIC(3,1) NOT NULL // TODO - CONSTRAINT para numero ser entre dez e zero nota inicial 0?
);

CREATE TABLE Tags(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    TAG varchar(255) NOT NULL,
    PRIMARY KEY(ID_FILME, TAG)
);

CREATE TABLE Avaliação(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    NOTA NUMERIC(3,1) NOT NULL, // TODO - CONSTRAINT para numero ser entre dez e zero
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Membro( 
    NOME varchar(255) PRIMARY KEY,
    PAIS varchar(255) NOT NULL,
    DATA_NASCIMENTO date NOT NULL,
    DATA_FALECIMENTO date
);

CREATE TABLE Solicitacao_Filme(
    NOME varchar(255) NOT NULL,
    ANO integer NOT NULL,
    ID_SOLICITACAO integer PRIMARY KEY,
    DURACAO integer NOT NULL,
    GENERO varchar(255) NOT NULL,
    SINOPSE varchar(255) NOT NULL,
    DIRETOR varchar(255) NOT NULL,
    IDIOMA varchar(255) NOT NULL
);

CREATE TABLE Tags_Solicitacao(
    ID_SOLICITACAO integer references Solicitacao_Filme (ID_SOLICITACAO)
    TAG varchar(255) NOT NULL,
    PRIMARY KEY(ID_SOLICITACAO, TAG)
);

CREATE TABLE Escreve(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Classificado(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Solicita(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Aprova(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Admin(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Assistira(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Participou(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    NOME varchar(255) REFERENCES Membro(NOME),
    CARGO varchar(255) NOT NULL,
    PRIMARY KEY(ID_FILME, NOME)
);

CREATE TABLE Assistiu(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);

CREATE TABLE Favoritou(
    ID_FILME integer REFERENCES Filme(ID_FILME),
    USERNAME varchar(255) REFERENCES U_Publico(USERNAME),
    PRIMARY KEY(ID_FILME, USERNAME)
);