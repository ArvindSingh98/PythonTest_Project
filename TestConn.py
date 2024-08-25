import os
from dotenv import load_dotenv
import argparse
from Models.sql import connectToDB, selectDataOp, insertDataOp
from datetime import datetime
from Models.Row import Row
import Models.ErrorLog as ErrLog


# Load Environment Vars
load_dotenv(override=True)


# Db information
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASS')
db = os.getenv('DB')
DATASOURCE = os.getenv('DATASOURCE')

# Establish db connection
try:
    connection = connectToDB(host, user, password, db,DATASOURCE)
except Exception as Err:
    ErrLog.func_logError(str(Err))



def selectDataHandler():
    data = selectDataOp(connection)
    print(data)


class A:

    def insertDataHandler():
    
        insert_data = Row(
                    date=datetime.now().date(), 
                    devId='DIV1258596896', 
                    alcConc='19' , 
                    humidity='35', 
                    temperature='35', 
                    distance='8', 
                    total=0 )

        try:
            rowsAffected = insertDataOp(connection, insert_data)

            response = {
                'message': 'Insert Succeeded',
                'rows_affected': rowsAffected
            }
            print(response)
            
        except Exception as Ex:
            print(Ex)

if __name__ == "__main__":
    selectDataHandler()
    #insertDataHandler()







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