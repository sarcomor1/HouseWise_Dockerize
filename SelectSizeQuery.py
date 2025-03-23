from db import get_connection


def SelectSizeQuery():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        pg_order_by_size = """ SELECT * FROM public."items" ORDER BY "size" """

        cursor.execute(pg_order_by_size)
        DB_records = cursor.fetchall()
        return DB_records

    except (Exception, Exception) as error:
        print("Error selecting data from table items", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()