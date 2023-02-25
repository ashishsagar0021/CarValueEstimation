import mysql.connector
from config import DB_CONFIG

def fetchRelevantList(make, model, year):
    mydb = mysql.connector.connect(**DB_CONFIG)
    # create a cursor object
    mycursor = mydb.cursor()
    # retrieve all rows that match the query criteria
    query = f"select make,model,year,listing_price,listing_mileage from VinData where year={year} and make like '{make}' and model like '{model}' limit 100;"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result
