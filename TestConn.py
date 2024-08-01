import os
from dotenv import load_dotenv
import argparse
from Models.sql import connectToDB, selectDataOp, insertDataOp
from datetime import datetime

# Load Environment Vars
load_dotenv(override=True)


# Db information
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASS')
db = os.getenv('DB')
DATASOURCE = os.getenv('DATASOURCE')

# Establish db connection
connection = connectToDB(host, user, password, db,DATASOURCE)


def selectDataHandler():
    data = selectDataOp(connection)
    print(data)



def insertDataHandler():
    dataobj = {'date':datetime.now().date(),
                'devId': 'DIV125896', 
                'alcConc':'22' ,
                'temperature':'26',
                 'distance':'6' 
            }

    try:
        rowsAffected = insertDataOp(connection, dataobj)

        response = {
            'message': 'Insert Succeeded',
            'rows_affected': rowsAffected
        }
        print(response)
        
    except Exception as Ex:
        print(Ex)

if __name__ == "__main__":
    selectDataHandler()







'''
Microsoft ODBC Driver for SQL Server Version 17.10.0006

Data Source Name: TestMSSql_Local
Data Source Description: 
Server: UFOMUM-ARVINDS
Use Integrated Security: No
Database: (Default)
Language: (Default)
Data Encryption: No
Trust Server Certificate: No
Multiple Active Result Sets(MARS): No
Translate Character Data: Yes
Log Long Running Queries: No
Log Driver Statistics: No
Use Regional Settings: No
Use ANSI Quoted Identifiers: Yes
Use ANSI Null, Paddings and Warnings: Yes
 '''