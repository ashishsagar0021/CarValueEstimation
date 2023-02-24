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
                first_seen_date = datetime.strptime(data[21], format_string)
                last_seen_date = datetime.strptime(data[22], format_string)
                dealer_vdp_last_seen_date = datetime.strptime(data[23], format_string)
                listing_status = data[24]

                # create the SQL query with the placeholders
                sql = f"INSERT INTO CarData (vin, year, make, model, trim, dealer_name, dealer_street, dealer_city, dealer_state, dealer_zip, listing_price, listing_mileage, used, certified, style, driven_wheels, engine, fuel_type, exterior_color, interior_color, seller_website, first_seen_date, last_seen_date, dealer_vdp_last_seen_date, listing_status) VALUES ('{vin}', {year}, '{make}', '{model}', '{trim}', '{dealer_name}', '{dealer_street}', '{dealer_city}', '{dealer_state}', '{dealer_zip}', {listing_price}, {listing_mileage}, {used}, {certified}, '{style}', '{driven_wheels}', '{engine}', '{fuel_type}', '{exterior_color}', '{interior_color}', '{seller_website}', '{first_seen_date}', '{last_seen_date}', '{dealer_vdp_last_seen_date}', '{listing_status}')"

                try:
                    mycursor.execute(sql)
                except Exception as e:
                    print("Error:", e)

        mydb.commit()

    # close the database connection
    mydb.close()
