from db import get_connection


def DeleteQuery(number):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        pg_delete = """ DELETE FROM public.items WHERE id = %s """

        delete_values = (number)
        cursor.execute(pg_delete, delete_values)
        connection.commit()

        count = cursor.rowcount
        print(f"Successfully deleted {count} row(s).")

    except (Exception, Exception) as error:
        print("Error in deleting the data:", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
