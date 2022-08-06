# HackBackpackers_ruvesh
Repository For WUElev8 Next Pathway HackBackpackers Hackathon


Problem Statements

## Problem Statement 1 - Lineage problem statement
# Description
Find the lineage of columns from an SQL query

# Prerequisite
1. python3
2. pip
3. command line tools like cmd/gitbash/terminal
4. sql to be parsed in a `.sql` file

# How to run

Steps
1. clone the codebase <br>
` git clone https://github.com/ruvesh/HackBackpackers_ruvesh.git `
2. navigate to Lineage Problem Statement directory
3. run `pip install`
4. navigate to Lineage Problem Statement/src folder
5. run `python3 main.py <path-to-sql-file>`

### Example Run
1. command-line <br>
`cd HackBackpackers_ruvesh/Lineage Problem Statement` <br>
`python3 main.py ../resources/sample1.sql`
2. Through PyCharm IDE (optional) <br>
   1. Create a run configuration for main.py and in parameters, add path to sql file <br>
   `../resources/sample1.sql`
   2. Run the `main.py` file 


### Approach

To find the lineage of a sql query, I have used the sqlparse library. The library is able to parse queries and provide tokens, identifiers, keywords, etc for processing.

With the above approach, I was able to successfully generate the lineage for the simple example query which was provided in the document. 

However, this does not work well with the complex queries. The approach would be able to solve it for complex queries as well, but due to time constraints, I wasn't able to optimize it for all the parsing scenarios.

Given a little more time, The approach taken should be able to solve the problem and extend out to all complexities of queries.
   

## Problem Statement 2 - Functions problem statement
# Description
Find the equivalent ADF functions for datastage functions

# Prerequisite
1. python3
2. command line tools like cmd/gitbash/terminal or some IDE

# How to run

Steps
1. clone the codebase <br>
` git clone https://github.com/ruvesh/HackBackpackers_ruvesh.git `
2. navigate to Function Conversion Problem Statement directory
4. navigate to each folder for each function type
5. run `python3 filename.py [<parameters required by the original function>]`

### Example Run
1. command-line <br>
`cd HackBackpackers_ruvesh/Function Conversion Problem Statement/Date_time_functions` <br>
`python3 currenttimestamp.py` <br>
`python3 datefromdaysince2.py 2 2022-08-04`
2. Through PyCharm IDE (optional) <br>
   1. Create a run configuration for each python script file and in parameters, add parameters required <br>
   2. Run the python file 


## Problem Statement 3 - XML problem statement
# Description
Find the lineage from Informatica XML

# Prerequisite
1. python3
2. command line tools like cmd/gitbash/terminal or some IDE

# How to run

Steps
1. clone the codebase <br>
` git clone https://github.com/ruvesh/HackBackpackers_ruvesh.git `
2. navigate to XML Problem Statement directory
3. run `python3 main.py`

### Example Run
1. command-line <br>
`cd HackBackpackers_ruvesh/XML Problem Statement`
2. Through PyCharm IDE (optional) <br>
   1. Run `main.py` file


### Approach

The XML file contains folder tags. Under each folder tag, there are tags for source and target. The target's NAME attribute is linked to the source's DBDNAME attribute.

In case of transformations, there are TRANSFORMATION tags under MAPPING Tags, where the TYPE attribute specifies the TRANSFORMATION TYPE.
The transformations can be mapped with the INSTANCE Tags on the basis of TYPE = "Source Qualifier". This parsing and mapping would be able to reveal the transformations applied to each field.

I have been able to find the source and target mappings programmatically. Due to time constraint, I wasn't able to complete the logic to find all the fields. 

This solution can be completed with the above approach with a little more time.