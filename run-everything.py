from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "your_password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to run Cypher queries
def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result

# Query to find popular products by views
popular_products_query = """
MATCH (p:Product)-[:BELONGS_TO]->(c:Category), (cust:Customer)-[:VIEWED]->(p)
RETURN c.name AS category, p.name AS product, COUNT(cust) AS views
ORDER BY views DESC
LIMIT 5
"""

# Query to generate product recommendations based on purchase history
recommendation_query = """
MATCH (c1:Customer)-[:VIEWED]->(p:Product)<-[:VIEWED]-(c2:Customer),
      (c2)-[:PURCHASED]->(other:Product)
WHERE c1 <> c2
RETURN p.name AS viewed_product, COLLECT(DISTINCT other.name) AS recommended_products
"""

# Run popular products query
popular_products = run_query(popular_products_query)
print("Popular Products by Views:")
for record in popular_products:
    print(f"Category: {record['category']}, Product: {record['product']}, Views: {record['views']}")

# Run recommendation query
recommendations = run_query(recommendation_query)
print("\nProduct Recommendations:")
for record in recommendations:
    print(f"Viewed Product: {record['viewed_product']}, Recommended Products: {record['recommended_products']}")
