import os
from pathlib import Path
from datetime import datetime

dirName ="D:\\Arvind\\TestProjects\\Pythons\\PythonTest_Project\\ErrorLogs"
current_datetime = datetime.now().date()

Err_date = current_datetime.strftime("%d_%m_%Y")
fileName ='Error_'+Err_date+'.txt'
# class ErrorLogger:
          
#      def __init__(self):
#         self.dirFolderPath= dirName

def func_logError(Errmsg):

#check if directory exits for logger  
#open(fileName, 'rw')
    filepath = os.path.join(dirName, fileName)

    if(os.path.isdir(dirName)):                
        if(os.path.isfile(filepath)):
                                        
            f = open(filepath, "a")
            f.write('Error Logged At :'+datetime.now().strftime("%H:%M:%S")+' ----------------- \n')
            f.writelines(Errmsg+'\n')
            f.writelines('--------------------------------------------\n')
            f.close()            
        else:
            f = open(filepath, "a")

            f.write('Error Logged At :'+datetime.now().strftime("%H:%M:%S")+' ----------------- \n')
            f.writelines(Errmsg+'\n')
            f.writelines('--------------------------------------------\n')

            f.close()

    else:
        os.makedirs(dirName)
        if(os.path.isfile(filepath)):
            f = open(filepath, "a")
            f.close()

    return "Error logged Successfully!"
    
    


# objErr =ErrorLogger()
# objErr.func_logError('Error fond for logging'+str(datetime.now()))
