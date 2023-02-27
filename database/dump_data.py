import mysql.connector
from config import DB_CONFIG

def dump_data():
    # create a MySQL connection
    mydb = mysql.connector.connect(**DB_CONFIG)

    # create a cursor object
    mycursor = mydb.cursor()

    # check if the T table is empty
    mycursor.execute("SELECT COUNT(*) FROM CarData")
    result = mycursor.fetchone()

    if result[0] == 0:
        line_number = 0
        # if the T table is empty, dump the data from data.txt to the T table
        with open('data.txt', 'r') as f:
            format_string = '%Y-%m-%d'
            for line in f:
                if line_number == 0:
                    line_number = 1
                    continue
                flag = 0
                data = line.strip().split('|')
                if data[0] == '' or data[1] == '' or data[2] == '' or data[3] == '' or data[10] == '' or data[11] == '':
                    continue
                print(f"data: {data}")
                vin = data[0]
                year = int(data[1])
                make = data[2]
                model = data[3]
                listing_price = float(data[10])
                listing_mileage = float(data[11])

                # create the SQL query with the placeholders
                sql = f"INSERT INTO CarData (vin, year, make, model, listing_price, listing_mileage) VALUES ('{vin}', {year}, '{make}', '{model}', {listing_price}, {listing_mileage})"

                try:
                    mycursor.execute(sql)
                except Exception as e:
                    print("Error:", e)

        mydb.commit()

    # close the database connection
    mydb.close()
