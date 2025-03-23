from InsertQuery import *
from DeleteQuery import *
from SelectQuery import *
from SelectSizeQuery import *
from SelectPriceQuery import *
from db import get_connection
from flask import Flask, render_template, request

app = Flask(__name__)
#===================================================================
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS public.items (
        id SERIAL PRIMARY KEY,
        price int,
        size int
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    if (connection):
        cursor.close()
        connection.close()
        print("Table 'items' checked/created.")
#===================================================================


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods = ['POST'])
def query():
    value = request.form['add/delete/list']
    match value.lower():
        case 'add':
            return render_template('add.html')
        case 'delete':
            return render_template('delete.html')
        case 'list':
            DB_records = SelectQuery()
            return render_template('list.html', DB_records=DB_records)



@app.route('/add', methods = ['post'])
def add():
    price = request.form['price']
    size = request.form['size']
    InsertQuery(price, size)
    return render_template('add.html')


@app.route('/delete', methods = ['post'])
def delete():
    number = request.form['number']
    DeleteQuery(number)
    return render_template('delete.html')


@app.route('/sort_list', methods = ['post'])
def sort_list():
    value = request.form['List/Price/Size']
    DB_records = sort_list_(value)
    return render_template('list.html', DB_records=DB_records)


def sort_list_(sort_list):
    match sort_list.lower():
        case 'list':
            DB_records = SelectQuery()
            return DB_records
        case 'size':
            DB_records = SelectSizeQuery()
            return DB_records
        case 'price':
            DB_records = SelectPriceQuery()
            return DB_records


if __name__ == '__main__':
    print("Waiting for DB to be ready...")
    create_table()
    app.run(debug=True, host='0.0.0.0', port=5000)