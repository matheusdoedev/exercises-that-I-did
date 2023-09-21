/* CREATING TABLES */
CREATE TABLE Position (
	id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
  	short_name VARCHAR(3) NOT NULL
);

CREATE TABLE Player (
	id 				INT PRIMARY KEY,
    first_name 		VARCHAR(20) NOT NULL,
    last_name		VARCHAR(20) NOT NULL,
    birthdate 		VARCHAR(10) NOT NULL,
  	id_position 	INT REFERENCES Position (id)
); 

CREATE TABLE Teams (
	id INT PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
  	short_name VARCHAR(20) NOT NULL,
  	state VARCHAR(2) NOT NULL,
  	city VARCHAR(20) NOT NULL
);

CREATE TABLE Contract (
	id	INT PRIMARY KEY,
  	player_id INT REFERENCES Player (id),
  	team_id INT REFERENCES Teams (id),
  	salary INT NOT NULL
);

/* POPULATING TABLES */
INSERT INTO Position (id, name, short_name) VALUES (1, "GOLEIRO", "GOL"), (2, "ZAGUEIRO", "ZAG"), (3, "MEIO CAMPISTA", "CAM"), (4, "ATACANTE", "ATA");

INSERT INTO Teams (id, full_name, short_name, state, city) VALUES (1, "Clube de Regatas Flamengo", "Flamengo", "RJ", "Rio de Janeiro"), (2, "Clube de Regatas Vasco da Gama", "Vasco da Gama", "RJ", "Rio de Janeiro"), (3, "Sociedade Esportiva Palmeiras", "Palmeiras", "SP", "São Paulo"), (4, "Esporte Clube Vitoria", "Vitoria", "BA", "Salvador"), (5, "Esporte Clube Bahia", "Bahia", "BA", "Salvador"), (6, "São Paulo Futebol Clube", "São Paulo", "SP", "São Paulo"), (7, "Santos Futebol Clube", "Santos", "SP", "Santos");

INSERT INTO Player (id, first_name, last_name, birthdate, id_position) VALUES (1, "Everton", "Ribeiro", "24/07/1986", 3), (2, "Gabriel", "Barbosa", "21/08/1996", 4), (3, "Dudu", "Santos", "27/09/1996", 3);

INSERT INTO Contract (id, player_id, team_id, salary) VALUES (1, 1, 1, 600000), (2, 3, 3, 400000), (3, 2, 1, 500000);

/* QUERIES */
SELECT * FROM Teams WHERE state = "BA";

SELECT * FROM Teams WHERE state in ("RJ", "BA");
                
SELECT * FROM Contract INNER JOIN Teams ON Teams.id = Contract.team_id;

SELECT * FROM Contract INNER JOIN Player ON Player.id = Contract.player_id;

SELECT * FROM Contract INNER JOIN Player ON Player.id = Contract.player_id INNER JOIN Teams ON Teams.id = Contract.team_id;

SELECT c.id as "ID do Contrato", p.first_name as "Nome", c.salary as "Salário", t.full_name as "Time" FROM Contract c INNER JOIN Player p ON p.id = c.player_id INNER JOIN Teams t ON t.id = c.team_id;

SELECT c.id as "ID do Contrato", p.first_name as "Nome", c.salary as "Salário", t.full_name as "Time" FROM Contract c INNER JOIN Player p ON p.id = c.player_id INNER JOIN Teams t ON t.id = c.team_id AND c.salary >= 500000;

SELECT * FROM Contract c INNER JOIN Player p ON p.id = c.player_id INNER JOIN Teams t ON t.id = c.team_id AND c.salary >= 500000;

SELECT AVG(c.salary) FROM Contract c;

SELECT c.id as "ID do Contrato", p.first_name as "Nome", c.salary as "Salário", t.full_name as "Time" FROM Contract c CROSS JOIN Player p ON p.id = c.player_id CROSS JOIN Teams t ON t.id = c.team_id AND c.salary >= 500000;

SELECT c.id as "ID do Contrato", p.first_name as "Nome", c.salary as "Salário", t.full_name as "Time" FROM Contract c LEFT OUTER JOIN Player p ON p.id = c.player_id LEFT OUTER JOIN Teams t ON t.id = c.team_id AND c.salary >= 500000;

SELECT c.id as "ID do Contrato", p.first_name as "Nome", c.salary as "Salário", t.full_name as "Time" FROM Contract c FULL OUTER JOIN Player p ON p.id = c.player_id FULL OUTER JOIN Teams t ON t.id = c.team_id AND c.salary >= 500000;