#!/usr/bin/python3

"""Insert data from collectData.py into a neo4j database and query it.
"""

import glob
import json
import neo4j
import neo4j.v1
import neo4j.exceptions
import os.path


dataDir = "data/"
jsonDir = dataDir

def main():
    populateNeo4j(jsonDir, True)
    queryNeo4j()


def populateNeo4j(jsonDir, clearDb=False):
    "Load the JSON results from google into neo4j"

    driver = neo4j.v1.GraphDatabase.driver(
        "bolt://localhost:7687", auth=neo4j.v1.basic_auth("neo4j", "cisc7610"))
    session = driver.session()

    # From: https://stackoverflow.com/a/29715865/2037288
    deleteQuery = """
    MATCH (n)
    OPTIONAL MATCH (n)-[r]-()
    WITH n,r LIMIT 50000
    DELETE n,r
    RETURN count(n) as deletedNodesCount
    """

    insertQuery = """
    WITH {json} as q
    MERGE (dept:Dept {name: q.name})
    MERGE (leader:Person {name: q.leader})
    MERGE (dept)-[:LEAD_BY]->(leader)
    MERGE (dept)<-[:WORKS_AT]-(leader)
    FOREACH (jsubdept in q.departments |
      MERGE (subdept:Dept {name: jsubdept.name})
      MERGE (subdept)-[:IS_PART_OF]->(dept))
    FOREACH (jworker in q.workers |
      MERGE (worker:Person {name: jworker.name})
      MERGE (worker)-[:WORKS_AT]->(dept))
    """

    # From: https://stackoverflow.com/a/30485232/2037288
    countQuery = """
    MATCH (a) WITH DISTINCT LABELS(a) AS temp, COUNT(a) AS tempCnt
    UNWIND temp AS label
    RETURN label, SUM(tempCnt) AS cnt
    ORDER BY label
    """

    if clearDb:
        result = session.run(deleteQuery)
        for record in result:
            print("Deleted", record["deletedNodesCount"], "nodes")

    loaded = 0
    for jsonFile in glob.glob(os.path.join(jsonDir, '*.json')):
        print("Loading", jsonFile, "into neo4j")
        with open(jsonFile) as jf:
            jsonData = json.load(jf)
            try:
                session.run(insertQuery, {"json": jsonData})
                loaded += 1
            except neo4j.exceptions.ClientError as ce:
                print(" ^^^^ Failed:", str(ce))

    print("\nLoaded", loaded, "JSON documents into Neo4j\n")

    queryNeo4jAndPrintResults(countQuery, session, "Neo4j now contains")

    session.close()


def queryNeo4j():
    driver = neo4j.v1.GraphDatabase.driver(
        "bolt://localhost:7687", auth=neo4j.v1.basic_auth("neo4j", "cisc7610"))
    session = driver.session()

    # Q0: Find all nodes
    query_0 = """
    match (n) return n
    """
    queryNeo4jAndPrintResults(query_0, session, title="Query 0")

    # Q1: Find all of the departments in Brooklyn College
    query_1 = """
    match (n:Dept) return n
    """
    queryNeo4jAndPrintResults(query_1, session, title="Query 1")

    # Q2: Find the path between the Computer and Information Science
    # department and Brooklyn College
    query_2 = """
    match (n1:Dept {name: "Computer and Information Science"}) 
    match (n2:Dept {name: "Brooklyn College"}) 
    match path = shortestpath((n1)-[*..3]-(n2))
    return n1, n2, path
    """
    queryNeo4jAndPrintResults(query_2, session, title="Query 2")

    # Q3: Find all of the people who work in the School of Natural and
    # Behavioral Sciences
    query_3 = """
    match (bns:Dept {name: "School of Natural and behavioral sciences"})
    match (d:Dept)-[:IS_PART_OF*..3]->(bns)
    match (bns)<-[:WORKS_AT]-(p1:Person) 
    match (d)<-[:WORKS_AT]-(p2:Person) 
    return bns, d, p1, p2
    """
    queryNeo4jAndPrintResults(query_3, session, title="Query 3")

    # Q4: Find all of the subordinates to Anne Lopes
    query_4 = """
    match (aa:Dept)-[:LEAD_BY]->(lopes:Person {name: "Anne Lopes"})
    match (d:Dept)-[:IS_PART_OF*..3]->(aa)
    match (aa)<-[:WORKS_AT]-(p1:Person) 
    match (d)<-[:WORKS_AT]-(p2:Person) 
    return aa, d, p1, p2
    """
    queryNeo4jAndPrintResults(query_4, session, title="Query 4")
    

    # All done!
    session.close()


def queryNeo4jAndPrintResults(query, session, title="Running query:"):
    print()
    print(title)
    print(query)

    for record in session.run(query):
        print(" " * 4, end="")
        for field in record:
            print(record[field], end="\t")
        print()


if __name__ == '__main__':
    main()
