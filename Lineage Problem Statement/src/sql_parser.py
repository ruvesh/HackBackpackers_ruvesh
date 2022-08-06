import sqlparse

def get_parsed_statement_from_sql_query(sql_query):
    return sqlparse.parse(sql_query)[0]


def parse_columns_from_parsed_statement(parsed_statement):
    column_identifiers = []
    columns_dict = {}
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
        columns_dict[str(column_identifier).split('.')[0]] = column_identifier.get_name()

    return columns_dict


def find_sub_queries_from_parsed_query(parsed_statement):
    sub_queries = []
    identifier_list = []
    in_keyword = False
    for token in parsed_statement.tokens:
        if isinstance(token, sqlparse.sql.Comment):
            continue
        if str(token).lower() in ['from', 'where', 'in']:
            in_keyword = True
        elif in_keyword and token.ttype is None:
            if str(token).__contains__('('):
                for identifier in token.get_identifiers():
                    identifier_list.append(identifier)
                break

    for identifier in identifier_list:
        sub_queries.append(str(identifier))

    return sub_queries


def find_table_names_and_alias_from_subquery(sub_queries_or_tables):
    table_alias_dict = {}

    for item in sub_queries_or_tables:
        identifier_name = str(item).replace(' ', '')
        if identifier_name.__contains__('('):
            table_alias_dict[identifier_name.split(')')[1]] = identifier_name.split(')')[0].split('from')[1]
        else:
            table_alias_dict[identifier_name.split(' ')[1]] = identifier_name.split(' ')[0]

    return table_alias_dict

