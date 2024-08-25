
from pyodbc import connect, Error as err

import Models.ErrorLog as ErrLog


def connectToDB(host, user, password, db ,DATASOURCE):
  

   # connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host};DATABASE={db};UID={user}; PWD={password};TrustServerCertificate=yes'
    try:
        connection = ('DRIVER={ODBC Driver 17 for SQL Server};'
            'Server='+host+';'
            'Database='+db+';'
            'UID='+user+';'
            'PWD='+password+';')
        cnxn = connect(connection)

       # connection = connect(connectionString)
        return cnxn
    except Exception as err:
        print(err)
        ErrLog.func_logError(str(err))
        return None
    

def selectDataOp(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT SyncDate , DeviceID ,Humidity,AlcoholConcentration,Temperature ,Distance  FROM IOT_Data "
        cursor.execute(query)

        result = cursor.fetchall()

        response = []

        for index in result:

            response.append(
                {
                    'date': index[0],
                    'devId': index[1],
                    'humidity': index[2],
                    'alc_conc': index[3],
                    'temperature': index[4],
                    'distance': index[5]
                }
            )

        return response
    
    except err:  
        ErrLog.func_logError(str(err))      
        return err
    
    finally:
        cursor.close()
    
def insertDataOp(connection, data):
    cursor = connection.cursor()

    try:
        proc = '''
            DECLARE @TotalRowsAdded INT;
            EXEC dbo.Proc_IOTDATA
                @IN_SyncDate = ?,
                @IN_DeviceID = ?,
                @IN_Humidity = ?,
                @IN_AlcoholConcentration = ?,
                @IN_Temperature = ?,
                @IN_Distance = ?,
                @Total_RwAdded = @TotalRowsAdded OUTPUT;
            SELECT @TotalRowsAdded AS TotalRowsAdded;
        '''

        params = [ data.date, data.devId,  data.humidity,  data.alcConc, data.temperature, data.distance ]

        cursor.execute(proc, params)

        cursor.nextset() 
        row = cursor.fetchone()  
        
        total_rows_added = row[0]  


        # Commit the transaction
        connection.commit()
        
        print("[ SUCCESS ]", end="")
        print(": Data inserted successfully into the database")
        return total_rows_added
            

    except err: 
        print(err)
        ErrLog.func_logError(str(err))
        print("[ FAILURE ]", end="")
        print(": Data could not be inserted into the database")
        
        print("An error occurred:")
        print(f"Error Class: {type(err).__name__}")
        print(f"Error Details: {err}")
        print(f"Error Arguments: {err.args}")



    finally:
        cursor.close()


