import sys
import utils
import sql_parser

sql_string = utils.read_sql_from_file(sys.argv[1])

parsed_statement = sql_parser.get_parsed_statement_from_sql_query(sql_string)
columns = sql_parser.parse_columns_from_parsed_statement(parsed_statement)
sub_queries = sql_parser.find_sub_queries_from_parsed_query(parsed_statement)

print(columns)

for sub_query in sub_queries:
    clean = sub_query.replace('(', '').replace(')', '')
    print(clean)



