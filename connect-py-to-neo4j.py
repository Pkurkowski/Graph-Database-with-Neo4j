from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "your_password"

# Create a Neo4j driver instance
driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to run queries
def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result

# Example query to get all customers and their viewed products
query = """
MATCH (c:Customer)-[:VIEWED]->(p:Product)
RETURN c.name AS customer, p.name AS product
"""

results = run_query(query)

# Display the results
for record in results:
    print(f"{record['customer']} viewed {record['product']}")
