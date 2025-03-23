from db import get_connection


def InsertQuery(price, size):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        pg_insert = """ INSERT INTO public."items" ("price", "size") VALUES(%s, %s)"""
        
        inserted_values = (price, size)
        cursor.execute(pg_insert, inserted_values)
        connection.commit()
        count = cursor.rowcount
        print("successfully inserting", count, "records.")

    except (Exception, Exception) as error:
        print("Error connection to PostgreSQL database", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()