import dotenv
import os
from neo4j import GraphDatabase

def connect_database():
    load_status = dotenv.load_dotenv("Neo4j-7f90cf43-Created-2026-06-11.txt")
    if load_status is False:
        raise RuntimeError('Environment variables not loaded.')

    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    # print("Connection established.")
    return driver
