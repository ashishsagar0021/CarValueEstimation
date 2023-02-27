import mysql.connector
from config import DB_CONFIG

def fetchRelevantList(make, model, year):
    mydb = mysql.connector.connect(**DB_CONFIG)
    # create a cursor object
    mycursor = mydb.cursor()
    # retrieve all rows that match the query criteria
    query = f"select make,model,year,listing_price,listing_mileage from CarData where year={year} and make like '{make}' and model like '{model}' limit 100;"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def getDefaultMileage(make, model, year):
    mydb = mysql.connector.connect(**DB_CONFIG)
    mycursor = mydb.cursor()
    query = f"select avg(listing_mileage) from CarData where year={year} and make like '{make}' and model like '{model}' group by make,model,year"
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result