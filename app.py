from flask import Flask
from database.dump_data import dump_data
import mysql.connector

app = Flask(__name__)

# create a MySQL connection
mydb = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="",
    database="CAR_VALUE_ESTIMATION"
)

# create a cursor object
mycursor = mydb.cursor()

# check if the T table exists
mycursor.execute("SHOW TABLES LIKE 'T'")
result = mycursor.fetchone()

# check if the T table exists
mycursor.execute("SHOW TABLES LIKE 'T'")
result = mycursor.fetchone()

if not result:
    # if the T table doesn't exist, create it
    with open('database/CarData.sql', 'r') as f:
        mycursor.execute(f.read())

# check if the T table is empty
mycursor.execute("SELECT COUNT(*) FROM T")
result = mycursor.fetchone()

if result[0] == 0:
    # if the T table is empty, dump the data from data.txt to the T table
    dump_data()

if __name__ == "__main__":
    from controller import hello, get_car_value_bp
    app.register_blueprint(hello)
    app.register_blueprint(get_car_value_bp)
    app.run(host='127.0.0.1')
