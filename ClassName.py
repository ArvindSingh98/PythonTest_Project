import Models.ErrorLog as Logger

class A:
    def __init__(self):
        print('Object Initialize!!')

    @staticmethod
    def func_PrintDivision():
        try:
            TxtMsg = eval(input('Enter Num to display the Division Result:'))
            Div = eval(input('Enter Num to Divide the entered Num:'))
            if TxtMsg is not None:
                # Logger.func_Print('Printed')
                print('Entered No Division Is :', (TxtMsg) / Div)
            else:
                print('Nothing to display!')
        except Exception as err:
            # print('Error Occured As :')
            # print(logging.error(err, exc_info=True))
            print(Logger.func_logError(err))

if __name__ == "__main__":
    A().func_PrintDivision()



