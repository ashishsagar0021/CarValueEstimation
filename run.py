from flask import Flask
from database.dump_data import dump_data
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

if __name__ == "__main__":
    # create a MySQL connection
    mydb = mysql.connector.connect(**DB_CONFIG)

    # create a cursor object
    mycursor = mydb.cursor()

    # check if the T table exists
    mycursor.execute("SHOW TABLES LIKE 'CarData'")
    result = mycursor.fetchone()

    if not result:
        # if the T table doesn't exist, create it
        with open('database/VinData.sql', 'r') as f:
            mycursor.execute(f.read())

    # check if the T table is empty
    mycursor.execute("SELECT COUNT(*) FROM CarData")
    result = mycursor.fetchone()

    if result[0] == 0:
        # if the T table is empty, dump the data from data.txt to the T table
        dump_data()
    from controller import hello, get_car_value_bp

    app.register_blueprint(hello)
    app.register_blueprint(get_car_value_bp)
    app.run(unix_socket="/root/ashish/carValueEstimation/carValueEstimation.sock")
