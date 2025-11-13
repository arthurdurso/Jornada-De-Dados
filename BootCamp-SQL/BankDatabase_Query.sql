-- Aula 7
-- Criação do Ambiente de Banco de Dados

-- Criar Banco de Dados
CREATE DATABASE bank_db;

-- Criar Tabelas
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY NOT NULL,
    limite INTEGER NOT NULL,
    saldo INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY NOT NULL,
    tipo CHAR(1) NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    valor INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    realizada_em TIMESTAMP NOT NULL DEFAULT NOW()
);


-- Criar Tabela (Modo UUID)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; --Apenas rodar uma vez para criar a extensão

CREATE TABLE IF NOT EXISTS clients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), -- Gerar um ID único aleatório automaticamente
    limite INTEGER NOT NULL,
    saldo INTEGER NOT NULL
);



-- Drop Tabela
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS transactions;



-- Inserção de Dados
INSERT INTO clients (limite, saldo)
VALUES
    (10000, 0),
    (80000, 0),
    (1000000, 0),
    (10000000, 0),
    (500000, 0);


-- Simulação de Transação
INSERT INTO transactions (tipo, descricao, valor, cliente_id)
VALUES ('d', 'Compra de carro', 80000, 1);

-- Atualização de Saldo do Cliente
UPDATE clients
SET saldo = saldo + CASE WHEN 'd' = 'd' THEN -80000 ELSE 80000 END
WHERE id = 1;

-- Consulta de Saldo do Cliente
SELECT saldo, limite
FROM clients
WHERE id = 1;


-- Deletar Dados
DELETE FROM transactions
WHERE id = 1;

UPDATE clients
SET saldo = 0
WHERE id = 1;