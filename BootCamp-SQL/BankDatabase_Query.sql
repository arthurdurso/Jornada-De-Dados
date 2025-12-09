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



-- Aula 8
-- Procedures

CREATE OR REPLACE PROCEDURE see_extration(
    IN p_cliente_id INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    balance INTEGER;
    transac RECORD;
    count INTEGER := 0;
BEGIN
    -- Obtém o saldo atual do cliente
    SELECT saldo INTO balance
    FROM clients
    WHERE id = p_cliente_id;

    -- Retorna o saldo atual do cliente
    RAISE NOTICE 'Saldo atual do cliente: %', balance;

    -- Retorna as 10 últimas transações do cliente
    RAISE NOTICE 'Últimas 10 transações do cliente:';
    FOR transac IN
        SELECT *
        FROM transactions
        WHERE cliente_id = p_cliente_id
        ORDER BY realizada_em DESC
        LIMIT 10
    LOOP
        count := count + 1;
        RAISE NOTICE 'ID: %, Tipo: %, Descrição: %, Valor: %, Data: %', transac.id, transac.tipo, transac.descricao, transac.valor, transac.realizada_em;
        EXIT WHEN count >= 10;
    END LOOP;
END;
$$;


-- Aula 9
-- Triggers

-- Criar Banco de Dados
CREATE DATABASE empresa_db;

-- Criação da tabela Funcionario
CREATE TABLE Funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    salario DECIMAL(10, 2),
    dtcontratacao DATE
);

-- Criação da tabela Funcionario_Auditoria
CREATE TABLE Funcionario_Auditoria (
    id INT,
    salario_antigo DECIMAL(10, 2),
    novo_salario DECIMAL(10, 2),
    data_de_modificacao_do_salario TIMESTAMP DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'),
    FOREIGN KEY (id) REFERENCES Funcionario(id)
);

-- Inserção de dados na tabela Funcionario
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Maria', 5000.00, '2021-06-01');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('João', 4500.00, '2021-07-15');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Ana', 4000.00, '2022-01-10');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Pedro', 5500.00, '2022-03-20');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Lucas', 4700.00, '2022-05-25');


-- Funcao parar registrar auditoria de salario
CREATE OR REPLACE FUNCTION func_registrar_auditoria_salario()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Funcionario_Auditoria (id, salario_antigo, novo_salario)
    VALUES (NEW.id, OLD.salario, NEW.salario);
    RETURN NEW;
END;
$$;

-- Criação da Trigger Function

CREATE OR REPLACE TRIGGER trg_salario_modificado
AFTER UPDATE OF salario ON Funcionario
FOR EACH ROW
WHEN (OLD.salario IS DISTINCT FROM NEW.salario)
EXECUTE FUNCTION func_registrar_auditoria_salario();


-- Testando Trigger
UPDATE funcionario
SET salario = 5000.00
WHERE id = 1;

SELECT * FROM Funcionario_Auditoria;


-- Segundo Exemplo de Trigger

-- Criação da tabela Produto
CREATE TABLE Produto (
    cod_prod INT PRIMARY KEY,
    descricao VARCHAR(50) UNIQUE,
    qtde_disponivel INT NOT NULL DEFAULT 0
);

-- Inserção de produtos
INSERT INTO Produto VALUES (1, 'Basica', 10);
INSERT INTO Produto VALUES (2, 'Dados', 5);
INSERT INTO Produto VALUES (3, 'Verao', 15);

-- Criação da tabela RegistroVendas
CREATE TABLE RegistroVendas (
    cod_venda SERIAL PRIMARY KEY,
    cod_prod INT,
    qtde_vendida INT,
    FOREIGN KEY (cod_prod) REFERENCES Produto(cod_prod) ON DELETE CASCADE
);


-- Função para Verificar Estoque
CREATE OR REPLACE FUNCTION func_verificar_estoque()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    estoque_atual INT;
BEGIN
    SELECT qtde_disponivel INTO estoque_atual
    FROM Produto
    WHERE cod_prod = NEW.cod_prod;

    IF estoque_atual < NEW.qtde_vendida THEN
        RAISE EXCEPTION 'Estoque insuficiente para o produto %: disponível %, solicitado %', NEW.cod_prod, estoque_atual, NEW.qtde_vendida;
    ELSE
        UPDATE Produto
        SET qtde_disponivel = qtde_disponivel - NEW.qtde_vendida
        WHERE cod_prod = NEW.cod_prod;
    END IF;

    RETURN NEW;
END;
$$;

-- Trigger Function para Verificar Estoque
CREATE OR REPLACE TRIGGER trg_verificar_estoque
BEFORE INSERT ON RegistroVendas
FOR EACH ROW
EXECUTE FUNCTION func_verificar_estoque();

-- Verificando Produtos

SELECT * FROM Produto;

INSERT INTO RegistroVendas(cod_prod, qtde_vendida) VALUES (1, 3); -- Sucesso
INSERT INTO RegistroVendas(cod_prod, qtde_vendida) VALUES (2, 6); -- Falha - Estoque insuficiente