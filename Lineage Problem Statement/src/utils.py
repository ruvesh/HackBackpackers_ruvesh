def read_sql_from_file(file_name):
    sql_file = open(file_name, mode='r')
    sql_string = sql_file.read()
    sql_file.close()
    return sql_string


def print_query_lineage(table_alias, columns):
    print("Lineage Generated For Query::")
    for key in columns:
        print(columns[key] + ' => ' + table_alias[key])
