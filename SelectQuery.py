from db import get_connection


def SelectQuery():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        pg_select = """ SELECT * FROM public.items """
        
        cursor.execute(pg_select)
        DB_records = cursor.fetchall()
        return DB_records

    except (Exception, Exception) as error:
        print("Error selecting data from table items", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
