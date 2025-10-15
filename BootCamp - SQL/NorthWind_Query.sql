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
-- Fazer exercicios amanhã, pq hoje já deu rsrsrs

-- 1. Faça a classificação dos produtos mais venvidos usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
-- Tabelas utilizadas: FROM order_details o JOIN products p ON p.product_id = o.product_id


-- 2. Listar funcionários dividindo-os em 3 grupos usando NTILE

-- 3. Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;


-- Desafio extra: questão intrevista Google
-- https://medium.com/@aggarwalakshima/interview-question-asked-by-google-and-difference-among-row-number-rank-and-dense-rank-4ca08f888486#:~:text=ROW_NUMBER()%20always%20provides%20unique,a%20continuous%20sequence%20of%20ranks.
-- https://platform.stratascratch.com/coding/10351-activity-rank?code_type=3
-- https://www.youtube.com/watch?v=db-qdlp8u3o

