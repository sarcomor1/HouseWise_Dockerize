from db import get_connection


def SelectPriceQuery():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        pg_order_by_price = """ SELECT * FROM public."items" ORDER BY "price" """
        
        cursor.execute(pg_order_by_price)
        DB_records = cursor.fetchall()
        return DB_records

    except (Exception, Exception) as error:
        print("Error selecting data from table items", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()