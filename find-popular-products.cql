MATCH (p:Product)-[:BELONGS_TO]->(c:Category), (cust:Customer)-[:VIEWED]->(p)
RETURN c.name AS category, p.name AS product, COUNT(cust) AS views
ORDER BY views DESC
LIMIT 5
