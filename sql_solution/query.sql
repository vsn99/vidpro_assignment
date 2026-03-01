WITH orders_items_joined AS
(SELECT 
	o.order_id AS order_id, 
	o.sales_id AS sales_id, 
	o.item_id AS item_id, 
	i.item_name AS item_name,
    o.quantity AS quantity 
FROM orders o
LEFT JOIN items i ON
o.item_id = i.item_id
WHERE quantity IS NOT NULL OR quantity != 0),
sales_customer_joined AS (SELECT
	s.sales_id AS sales_id,
    s.customer_id AS customer_id,
    c.age AS age
FROM sales s
LEFT JOIN customer c ON
c.customer_id = s.customer_id
WHERE age BETWEEN 18 AND 35
)
SELECT
customer_id AS Customer,
age AS Age,
item_name AS Item,
SUM(quantity) AS Quantity
FROM orders_items_joined oi
JOIN sales_customer_joined sc ON
oi.sales_id = sc.sales_id
GROUP BY customer_id, item_name;