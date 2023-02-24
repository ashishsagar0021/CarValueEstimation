from datetime import datetime

import mysql.connector


def dump_data():
    # create a MySQL connection
    mydb = mysql.connector.connect(
        host="localhost",
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
        flag = 0
        # if the T table is empty, dump the data from data.txt to the T table
        with open('data.txt', 'r') as f:
            format_string = '%Y-%m-%d'
            for line in f:
                if flag == 0:
                    flag = 1
                    continue
                flag = 0
                data = line.strip().split('|')
                for x in data:
                    if x == '':
                        flag = 1
                        break
                if flag == 1:
                    continue
                print(f"data: {data}")
                vin = data[0]
                year = int(data[1])
                make = data[2]
                model = data[3]
                trim = data[4]
                dealer_name = data[5]
                dealer_street = data[6]
                dealer_city = data[7]
                dealer_state = data[8]
                dealer_zip = data[9]
                listing_price = float(data[10])
                listing_mileage = float(data[11])
                used = bool(data[12])
                certified = bool(data[13])
                style = data[14]
                driven_wheels = data[15]
                engine = data[16]
                fuel_type = data[17]
                exterior_color = data[18]
                interior_color = data[19]
                seller_website = data[20]
                first_seen_date = int((datetime.strptime(data[21], format_string)).year)
                last_seen_date = int((datetime.strptime(data[22], format_string)).year)
                dealer_vdp_last_seen_date = int((datetime.strptime(data[23], format_string)).year)
                listing_status = data[24]

                # define a list of datatypes for each value in the data.txt file
                dtypes = [str, int, str, str, str, str, str, str, str, str,
                          float, float, bool, bool, str, str, str, str, str,
                          str, str, int, int, int, str]

                # create a list of placeholders based on the datatype of each value
                placeholders = ', '.join(['%s'] * len(data))
                placeholders = placeholders.format(*[t.__name__ for t in dtypes])

                # create the SQL query with the placeholders
                sql = f"INSERT INTO CarData (vin, year, make, model, trim, dealer_name, dealer_street, dealer_city, dealer_state, dealer_zip, listing_price, listing_mileage, used, certified, style, driven_wheels, engine, fuel_type, exterior_color, interior_color, seller_website, first_seen_date, last_seen_date, dealer_vdp_last_seen_date, listing_status) VALUES ({placeholders})"

                # create a tuple of values to insert
                # create the values tuple with the converted data
                values = tuple(t(d) for t, d in zip(dtypes, data))
                try:
                    mycursor.execute(sql, values)
                except Exception as e:
                    print("Error:", e)

        mydb.commit()

    # close the database connection
    mydb.close()
