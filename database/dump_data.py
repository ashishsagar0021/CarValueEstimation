import mysql.connector

def dump_data():
    # create a MySQL connection
    mydb = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="",
        database="CAR_VALUE_ESTIMATION"
    )

    # create a cursor object
    mycursor = mydb.cursor()

    # check if the T table is empty
    mycursor.execute("SELECT COUNT(*) FROM CarData")
    result = mycursor.fetchone()







    

    if result[0] == 0:
        # if the T table is empty, dump the data from data.txt to the T table
        with open('data.txt', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                make = data[0]
                model = data[1]
                year = int(data[2])
                price = int(data[3])
                sql = "INSERT INTO CarData (make, model, year, price) VALUES (%s, %s, %s, %s)"
                val = (make, model, year, price)
                mycursor.execute(sql, val)

        mydb.commit()

    # close the database connection
    mydb.close()
