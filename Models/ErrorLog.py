import os
from pathlib import Path
from datetime import datetime
import logging



dirName ="D:\\Arvind\\TestProjects\\Pythons\\PythonTest_Project\\ErrorLogs"
current_datetime = datetime.now().date()

Err_date = current_datetime.strftime("%d_%m_%Y")
ErrfileName ='Error_'+Err_date+'.txt'
# class ErrorLogger:
          
#      def __init__(self):
#         self.dirFolderPath= dirName






def func_logError(Errmsg):

#check if directory exits for logger  
#open(fileName, 'rw')
    filepath = os.path.join(dirName, ErrfileName)

    
    if(os.path.isdir(dirName)):                
        if(os.path.isfile(filepath)):
                                        
            # f = open(filepath, "a")
            # f.write('Error Logged At :'+datetime.now().strftime("%H:%M:%S")+' ----------------- \n')
            # f.writelines(str(Errmsg)+'\n')
            # f.writelines('--------------------------------------------\n')
            # f.close()  

            logging.basicConfig(filename=filepath, level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(message)s')
            logging.error(Errmsg, exc_info=True)   
        else:
            #f = open(filepath, "a")

            # f.write('Error Logged At :'+datetime.now().strftime("%H:%M:%S")+' ----------------- \n')
            # f.writelines(str(Errmsg)+'\n')

            # f.writelines('--------------------------------------------\n')

            #f.close()
            logging.basicConfig(filename=filepath, level=logging.ERROR,
                            format='%(asctime)s %(levelname)s %(message)s')
            logging.error(Errmsg, exc_info=True)   

    else:
        os.makedirs(dirName)
        if(os.path.isfile(filepath)):
            f = open(filepath, "a")
            f.close()
        
        logging.basicConfig(filename=filepath, level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(message)s')
        logging.error(Errmsg, exc_info=True)   

    return "Error logged Successfully!"
    
    