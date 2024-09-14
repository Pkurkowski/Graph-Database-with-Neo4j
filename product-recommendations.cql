MATCH (c1:Customer)-[:VIEWED]->(p:Product)<-[:VIEWED]-(c2:Customer),
      (c2)-[:PURCHASED]->(other:Product)
WHERE c1 <> c2
RETURN p.name AS viewed_product, COLLECT(DISTINCT other.name) AS recommended_products
