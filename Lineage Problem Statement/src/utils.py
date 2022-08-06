def read_sql_from_file(file_name):
    sql_file = open(file_name, mode='r')
    sql_string = sql_file.read()
    sql_file.close()
    return sql_string



