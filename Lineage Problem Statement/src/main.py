import sys
import utils
import sql_parser

sql_string = utils.read_sql_from_file(sys.argv[1])

parsed_statement = sql_parser.get_parsed_statement_from_sql_query(sql_string)

columns = sql_parser.parse_columns_from_parsed_statement(parsed_statement)
sub_queries_or_tables = sql_parser.find_sub_queries_from_parsed_query(parsed_statement)

table_alias = sql_parser.find_table_names_and_alias_from_subquery(sub_queries_or_tables)

utils.print_query_lineage(table_alias, columns)




