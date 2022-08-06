from pprint import pprint
import sqlparse
from sqlparse.sql import Where, Comparison, Parenthesis, Identifier
from sqlparse.tokens import Keyword, Punctuation


def get_parsed_statement_from_sql_query(sql_query):
    return sqlparse.parse(sql_query)[0]


def parse_columns_from_parsed_statement(parsed_statement):
    columns = []
    column_identifiers = []

    in_select = False
    for token in parsed_statement.tokens:
        if isinstance(token, sqlparse.sql.Comment):
            continue
        if str(token).lower() == 'select':
            in_select = True
        elif in_select and token.ttype is None:
            for identifier in token.get_identifiers():
                column_identifiers.append(identifier)
            break

    # get column names
    for column_identifier in column_identifiers:
        columns.append((str(column_identifier).split('.')[0], column_identifier.get_name()))

    return columns


def find_sub_queries_from_parsed_query(parsed_statement):
    sub_queries = []
    identifier_list = []
    in_select = False
    for token in parsed_statement.tokens:
        if isinstance(token, sqlparse.sql.Comment):
            continue
        if str(token).lower() in ['from', 'where', 'as', 'in']:
            in_select = True
        elif in_select and token.ttype is None:
            for identifier in token.get_identifiers():
                identifier_list.append(identifier)
            break

    for identifier in identifier_list:
        sub_queries.append(str(identifier))

    return sub_queries


# def find_table_names_from_parsed(parsed_statement):
