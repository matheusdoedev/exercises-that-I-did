-- Problem link: https://www.beecrowd.com.br/judge/en/problems/view/2602

CREATE TABLE customers (
	id INT PRIMARY KEY NOT NULL,
	name varchar(60) NOT NULL,
	street varchar(60) NOT NULL,
	city varchar(50) NOT NULL,
	state char(2) NOT NULL,
	credit_limit number NOT NULL
);

INSERT INTO customers (id, name, street, city, state, credit_limit) VALUES (1, "Pedro Augusto da Rocha", "Rua Pedro Carlos Hoffman", "Porto Alegre", "RS", 700), (2, "Antonio Carlos Mamel", "Av. Pinheiros", "Belo Horizonte", "MG", 3500.50), (3, "Luiza Augusta Mhor", "Rua Salto Grande", "Niteroi", "RJ", 4000), (4, "Jane Ester", "Av 7 de setembro", "Erechim", "RS", 800), (5, "Marcos Antônio dos Santos", "Av Farrapos", "Porto Alegre", "RS", 4250.25);

-- BEECROWD SOLUTION
SELECT name FROM customers WHERE state = 'RS';