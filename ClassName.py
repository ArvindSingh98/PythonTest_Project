import Models.ErrorLog as Logger 



class A:    
    
    def __init__(self):
        print('Object Initialize!!')        
        

    def func_PrintDivision(self):
        try:
            self.TxtMsg = eval(input('Enter Num to display the Division Result:'))
            self.Div = eval(input('Enter Num to Divide the entered Num:'))
            if(self.TxtMsg is not None ):
                #Logger.func_Print('Printed')
                print('Entered No Division Is :',(self.TxtMsg)/self.Div)
            else:
                print('Nothing to display!')
        except Exception as err:
             # print('Error Occured As :')
             #print(logging.error(err, exc_info=True))
             print(Logger.func_logError(err))


if __name__ == "__main__":

    objA = A()
    objA.func_PrintDivision()



