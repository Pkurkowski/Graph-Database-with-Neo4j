// Create categories
CREATE (:Category {name: 'Electronics'})
CREATE (:Category {name: 'Clothing'})
CREATE (:Category {name: 'Home'})

// Create products and link them to categories
CREATE (p1:Product {name: 'Smartphone', price: 699})-[:BELONGS_TO]->(:Category {name: 'Electronics'})
CREATE (p2:Product {name: 'Laptop', price: 999})-[:BELONGS_TO]->(:Category {name: 'Electronics'})
CREATE (p3:Product {name: 'T-Shirt', price: 19})-[:BELONGS_TO]->(:Category {name: 'Clothing'})
CREATE (p4:Product {name: 'Blender', price: 99})-[:BELONGS_TO]->(:Category {name: 'Home'})

// Create customers and link them to product views or purchases
CREATE (c1:Customer {name: 'Alice', id: 'C001'})-[:VIEWED]->(p1)
CREATE (c2:Customer {name: 'Bob', id: 'C002'})-[:PURCHASED]->(p2)
CREATE (c1)-[:PURCHASED]->(p3)
CREATE (c2)-[:VIEWED]->(p1)
CREATE (c1)-[:VIEWED]->(p4)
