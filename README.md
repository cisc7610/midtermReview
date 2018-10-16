# Midterm review Neo4j problem
### Brooklyn College org chart
### Prof Michael Mandel `mim@sci.brooklyn.cuny.edu`

For this review, you will be interacting with a set of JSON documents in 
Neo4j. The JSON documents are written by hand to reflect the [Brooklyn College organizational chart](http://www.brooklyn.cuny.edu/web/abo_administration_organization_chart/2017_OrganizationalChart_BrooklynCollege.pdf).

This code is based on the code for homework 2.  In fact, it is identical except for the queries.

This code includes both the query to populate the database from the JSON files as well as the code to query it.  Querying via this code produces large printouts, so it is more useful to run the queries in the Neo4j Browser environment once the database is populated.

## Install and setup Neo4j

1. Download Neo4j community edition for your platform from
   http://neo4j.com/download/ and unzip it.
1. Follow the guide on using the Neo4j browser:
   http://neo4j.com/developer/guide-neo4j-browser/ . When
   prompted, *set the password for user `neo4j` to `cisc7610`*
   so that eventually I can use your 
   code on my own neo4j database with the same settings.  It will
   guide you through the process of starting the server running locally
   on your computer and connecting to it through your laptop.
    * Note that if you initially use a different password, you can change your password using the cypher query `:server change-password`
1. Learn about Neo4j.  Run the following cypher queries in the Neo4j web interface, which generate sets of "slides" to get you familiar with Neo4j.
   1. `:play intro`
   1. `:play concepts`
   1. `:play movie graph`
1. You might also want to read this article to get started
   http://neo4j.com/developer/graph-db-vs-rdbms/
1. After running the movie graph example, open the sidebar by
   clicking on the three circles in the top left of the screen.  Select
   the entire database by clicking on the `*` button under "Node
   labels".  Take a screenshot of the graph to be included in your
   report.

## Install python-neo4j driver

Use `pip` to instlal the neo4j-driver package:

```bash
pip install neo4j-driver
```

The following code should run from the commandline and print "Worked!" without generating any errors.  If it doesn't, then you have a problem with your python configuration or the installation of the neo4j-driver package.

```bash
python -c 'import neo4j; print("Worked!")'
```

   
## Introduction to code   

All of the python code is contained in the file `runNeo4j.py`.
If you have all of the necessary dependencies installed, you should be able to run the script as it is to 
complete very basic versions of each of the tasks in the homework: 
 * Populate the database
 * Query the database

Running the code should produce the following output:

```
Deleted 116 nodes
Loading data/02_nbs.json into neo4j
Loading data/03_academicAffairs.json into neo4j
Loading data/04_bcPres.json into neo4j
Loading data/01_cis.json into neo4j

Loaded 4 JSON documents into Neo4j


Neo4j now contains

    MATCH (a) WITH DISTINCT LABELS(a) AS temp, COUNT(a) AS tempCnt
    UNWIND temp AS label
    RETURN label, SUM(tempCnt) AS cnt
    ORDER BY label
    
    Dept	20	
    Person	35	

Query 0

    match (n) return n
    
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	
    <Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	
    <Node id=74302 labels={'Dept'} properties={'name': 'Anthropology and Archaeology'}>	
    <Node id=74303 labels={'Dept'} properties={'name': 'Biology'}>	
    <Node id=74304 labels={'Dept'} properties={'name': 'Chemistry'}>	
    <Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	
    <Node id=74306 labels={'Dept'} properties={'name': 'Earth and Environmental Sciences'}>	
    <Node id=74307 labels={'Dept'} properties={'name': 'Health and Nutritional Sciences'}>	
    <Node id=74308 labels={'Dept'} properties={'name': 'Kinesiology'}>	
    <Node id=74309 labels={'Dept'} properties={'name': 'Mathematics'}>	
    <Node id=74310 labels={'Dept'} properties={'name': 'Physics'}>	
    <Node id=74311 labels={'Dept'} properties={'name': 'Psychology'}>	
    <Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	
    <Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	
    <Node id=74315 labels={'Dept'} properties={'name': 'School of Business'}>	
    <Node id=74316 labels={'Dept'} properties={'name': 'School of Humanities and Social Sciences'}>	
    <Node id=74317 labels={'Dept'} properties={'name': 'School of Visual, Media and Performing Arts'}>	
    <Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	
    <Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	
    <Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	
    <Node id=74321 labels={'Dept'} properties={'name': 'Brooklyn College'}>	
    <Node id=74322 labels={'Person'} properties={'name': 'Michelle J. Anderson'}>	
    <Node id=74323 labels={'Dept'} properties={'name': 'Finance'}>	
    <Node id=74324 labels={'Dept'} properties={'name': 'Special projects'}>	
    <Node id=74325 labels={'Dept'} properties={'name': 'Enrollment management'}>	
    <Node id=74326 labels={'Dept'} properties={'name': 'Student affairs'}>	
    <Node id=74327 labels={'Person'} properties={'name': 'Tony Thomas'}>	
    <Node id=74328 labels={'Person'} properties={'name': 'Michael Hewitt'}>	
    <Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	
    <Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	

Query 1

    match (n:Dept) return n
    
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	
    <Node id=74302 labels={'Dept'} properties={'name': 'Anthropology and Archaeology'}>	
    <Node id=74303 labels={'Dept'} properties={'name': 'Biology'}>	
    <Node id=74304 labels={'Dept'} properties={'name': 'Chemistry'}>	
    <Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	
    <Node id=74306 labels={'Dept'} properties={'name': 'Earth and Environmental Sciences'}>	
    <Node id=74307 labels={'Dept'} properties={'name': 'Health and Nutritional Sciences'}>	
    <Node id=74308 labels={'Dept'} properties={'name': 'Kinesiology'}>	
    <Node id=74309 labels={'Dept'} properties={'name': 'Mathematics'}>	
    <Node id=74310 labels={'Dept'} properties={'name': 'Physics'}>	
    <Node id=74311 labels={'Dept'} properties={'name': 'Psychology'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	
    <Node id=74315 labels={'Dept'} properties={'name': 'School of Business'}>	
    <Node id=74316 labels={'Dept'} properties={'name': 'School of Humanities and Social Sciences'}>	
    <Node id=74317 labels={'Dept'} properties={'name': 'School of Visual, Media and Performing Arts'}>	
    <Node id=74321 labels={'Dept'} properties={'name': 'Brooklyn College'}>	
    <Node id=74323 labels={'Dept'} properties={'name': 'Finance'}>	
    <Node id=74324 labels={'Dept'} properties={'name': 'Special projects'}>	
    <Node id=74325 labels={'Dept'} properties={'name': 'Enrollment management'}>	
    <Node id=74326 labels={'Dept'} properties={'name': 'Student affairs'}>	

Query 2

    match (n1:Dept {name: "Computer and Information Science"}) 
    match (n2:Dept {name: "Brooklyn College"}) 
    match path = shortestpath((n1)-[*..3]-(n2))
    return n1, n2, path
    
    <Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74321 labels={'Dept'} properties={'name': 'Brooklyn College'}>	<Path start=74305 end=74321 size=3>	

Query 3

    match (bns:Dept {name: "School of Natural and behavioral sciences"})
    match (d:Dept)-[:IS_PART_OF*..3]->(bns)
    match (bns)<-[:WORKS_AT]-(p1:Person) 
    match (d)<-[:WORKS_AT]-(p2:Person) 
    return bns, d, p1, p2
    
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	
    <Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	

Query 4

    match (aa:Dept)-[:LEAD_BY]->(lopes:Person {name: "Anne Lopes"})
    match (d:Dept)-[:IS_PART_OF*..3]->(aa)
    match (aa)<-[:WORKS_AT]-(p1:Person) 
    match (d)<-[:WORKS_AT]-(p2:Person) 
    return aa, d, p1, p2
    
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74312 labels={'Person'} properties={'name': 'Crystal Schloss'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74300 labels={'Dept'} properties={'name': 'School of Natural and behavioral sciences'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74301 labels={'Person'} properties={'name': 'Kleanthis Psarris'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74347 labels={'Person'} properties={'name': 'Mandel, Michael'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74346 labels={'Person'} properties={'name': 'Cox, James L.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74349 labels={'Person'} properties={'name': 'Thurm, Joseph'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74348 labels={'Person'} properties={'name': 'Schnabolk, Charles'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74351 labels={'Person'} properties={'name': 'Cogan, Eva'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74350 labels={'Person'} properties={'name': 'Chen, Hui'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74353 labels={'Person'} properties={'name': 'Kletenik, Devorah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74352 labels={'Person'} properties={'name': 'Halevi, Tzipora'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74354 labels={'Person'} properties={'name': 'Levitan, Rebecca'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74329 labels={'Person'} properties={'name': 'Yedidyah Langsam'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74332 labels={'Person'} properties={'name': 'Arnow, David M.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74333 labels={'Person'} properties={'name': 'Augenstein, Moshe'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74330 labels={'Person'} properties={'name': 'Parikh, Rohit'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74331 labels={'Person'} properties={'name': 'Raphan, Theodore'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74336 labels={'Person'} properties={'name': 'Langsam, Yedidyah'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74337 labels={'Person'} properties={'name': 'Rudowsky, Ira'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74334 labels={'Person'} properties={'name': 'Bar-Noy, Amotz'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74335 labels={'Person'} properties={'name': 'Dexter, Scott D.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74340 labels={'Person'} properties={'name': 'Weiss, Gerald'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74341 labels={'Person'} properties={'name': 'Whitlock, Paula'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74338 labels={'Person'} properties={'name': 'Sokol, Dina'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74339 labels={'Person'} properties={'name': 'Tenenbaum, Aaron'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74344 labels={'Person'} properties={'name': 'Zhou, Neng-Fa'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74345 labels={'Person'} properties={'name': 'Ziegler, Chaim'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74342 labels={'Person'} properties={'name': 'Yanofsky, Noson S.'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74314 labels={'Person'} properties={'name': 'Anne Lopes'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74319 labels={'Person'} properties={'name': 'Lisa Schwebel'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74318 labels={'Person'} properties={'name': 'Sara Crosby'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	
    <Node id=74313 labels={'Dept'} properties={'name': 'Academic affairs'}>	<Node id=74305 labels={'Dept'} properties={'name': 'Computer and Information Science'}>	<Node id=74320 labels={'Person'} properties={'name': 'Sabrina Cerezo'}>	<Node id=74343 labels={'Person'} properties={'name': 'Yarmish, Gabriel'}>	

```