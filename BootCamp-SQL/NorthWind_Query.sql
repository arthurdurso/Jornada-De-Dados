-- Aula 2

-- 1. Obter todas as colunas das tabelas Clientes, Pedidos e Fornecedores
SELECT *
FROM public.customers;

SELECT *
FROM public.orders;

SELECT *
FROM public.suppliers;


-- 2. Obter todos os Clientes em ordem alfabética por país e nome
SELECT *
FROM public.customers
ORDER BY COUNTRY, CONTACT_NAME;


-- 3. Obter os 5 pedidos mais antigos
SELECT *
FROM public.orders
ORDER BY ORDER_DATE ASC
LIMIT 5;


-- 4. Obter a contagem de todos os Pedidos feitos durante 1997
SELECT COUNT(*)
FROM public.orders
WHERE EXTRACT(YEAR FROM ORDER_DATE) = 1997;


-- 5. Obter os nomes de todas as pessoas de contato onde a pessoa é um gerente, em ordem alfabética
SELECT contact_name
FROM public.customers
WHERE CONTACT_TITLE ILIKE '%Manager%'
ORDER BY CONTACT_NAME;


-- 6. Obter todos os pedidos feitos em 19 de maio de 1997
SELECT *
FROM public.orders
WHERE ORDER_DATE = '1997-05-19';





-- Aula 3

-- 1. Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)
SELECT *
FROM public.orders o
JOIN public.customers c ON o.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 1996;

-- 2. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT e.city, 
       COUNT(DISTINCT employee_id) AS num_employees,
       COUNT(DISTINCT customer_id) AS num_customers
FROM public.employees e
LEFT JOIN public.customers c ON e.city = c.city
GROUP BY e.city
ORDER BY e.city;

-- 3. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT c.city, 
       COUNT(DISTINCT e.employee_id) AS num_employees,
       COUNT(DISTINCT c.customer_id) AS num_customers
FROM public.customers c
LEFT JOIN public.employees e ON c.city = e.city
GROUP BY c.city
ORDER BY c.city;

-- 4.Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
SELECT COALESCE(e.city, c.city) AS city,
       COUNT(DISTINCT e.employee_id) AS num_employees,
       COUNT(DISTINCT c.customer_id) AS num_customers
FROM public.employees e
FULL JOIN public.customers c ON e.city = c.city
GROUP BY COALESCE(e.city, c.city)
ORDER BY city;

-- 5. Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
SELECT p.product_name,
       SUM(od.quantity) AS total_quantity_ordered
FROM public.products p
JOIN public.order_details od ON p.product_id = od.product_id
GROUP BY p.product_name
HAVING SUM(od.quantity) < 200
ORDER BY total_quantity_ordered DESC;

-- 6. Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)
SELECT c.customer_id,
       c.contact_name,
       COUNT(o.order_id) AS total_orders
FROM public.customers c
JOIN public.orders o ON c.customer_id = o.customer_id
WHERE o.order_date > '1996-12-31'
GROUP BY c.customer_id, c.contact_name
HAVING COUNT(o.order_id) > 15
ORDER BY total_orders DESC;



-- Aula 4

-- 1. Faça a classificação dos produtos mais venvidos usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
-- Tabelas utilizadas: FROM order_details o JOIN products p ON p.product_id = o.product_id

-- Versão sem subquery
SELECT 
       o.product_id,
       p.product_name,
       SUM(o.quantity) AS total_quantity
FROM order_details o
JOIN products p ON p.product_id = o.product_id
GROUP BY o.product_id, p.product_name
ORDER BY total_quantity DESC;

-- Versão com subquery
SELECT 
       o.product_id,
       p.product_name,
       SUM(o.quantity) AS total_quantity,
       RANK() OVER (ORDER BY SUM(o.quantity) DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY SUM(o.quantity) DESC) AS rank_dense,
       ROW_NUMBER() OVER (ORDER BY SUM(o.quantity) DESC) AS row_number
FROM order_details o
JOIN products p ON p.product_id = o.product_id
GROUP BY o.product_id, p.product_name
ORDER BY total_quantity DESC;


-- 2. Listar funcionários dividindo-os em 3 grupos usando NTILE

SELECT
       employee_id,
       first_name,
       last_name,
       hire_date,
       NTILE(3) OVER (ORDER BY hire_date) as hire_group
FROM employees
ORDER BY hire_date;


-- 3. Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:


SELECT customer_id,
       order_date,
       LAG(freight) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_freight,
       freight AS current_freight,
       LEAD(freight) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_freight
FROM orders o
ORDER BY customer_id, order_date;



-- Desafio extra: questão intrevista Google
-- https://medium.com/@aggarwalakshima/interview-question-asked-by-google-and-difference-among-row-number-rank-and-dense-rank-4ca08f888486

--Interview Question
--Find the email activity rank for each user. Email activity rank is defined by the total number of emails sent. The user with the highest number of emails sent will have a rank of 1, and so on. Output the user, total emails, and their activity rank. Order records by the total emails in descending order. Sort users with the same number of emails in alphabetical order.
--In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. For tie breaker use alphabetical order of the user usernames.

--Table: google_gmail_emails
--id — int
--from_user — varchar
--to_user — varchar
--day — int

SELECT
       from_user AS user,
       COUNT(*) AS total_emails,
       ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, from_user) AS activity_rank
FROM google_gmail_emails
GROUP BY from_user;



-- Aula 5

-- Project NorthWind Analysis
-- https://github.com/arthurdurso/Project-NorthWind-Analysis



-- Aula 6

-- Recriar as consultas do Project NorthWind Analysis em: CTE/Subqueries/Views/Materialized Views/Temporary Tables
-- Aula foi longa, vou fazer os exercicios na próxima semana.