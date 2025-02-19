from langchain_neo4j import Neo4jGraph
import os


# https://api.python.langchain.com/en/latest/graphs/langchain_community.graphs.neo4j_graph.Neo4jGraph.html
class Graph(Neo4jGraph):
    def __init__(self, **kwargs):
        url = os.getenv("NEO4J_CONNECTION_URL")
        password = os.getenv("NEO4J_PASSWORD")
        username = os.getenv("NEO4J_USER")
        database = kwargs.get('database', None)
        timeout = kwargs.get('timeout', None)
        # sanitize (bool) –
        # refresh_schema (bool) –
        # driver_config (Dict | None) –
        # enhanced_schema (bool) –
        super().__init__(url, username, password, database, timeout)

