class A:
	def __init__(self):
		print('Its me A')

	# def __str__(self):
	# 	return f"{self.name} , {self.age}"
	
class A1:
	def __init__(self):
		print('Its me A1')

	# def __str__(self):
	# 	return f"{self.name} , {self.age}"
	
#class B for single inheritance

class B(A,A1):
	def __init__(self):
		# super().__init__()
		# A1()

		print('Its me instance of B')
	
	def getdetails(self,*arg):
		# x = lambda x,y:(name+' '+str(age))
		# print('values :'+x(name,age))
	    #for val in arg:
		"""This is the documentation string for my_function."""
		"""
		test documented code here..
		"""
		print(type (arg))
		vals = lambda x:(str(arg))
		print('Value :'+vals(arg))

	
if __name__ == "__main__":
	obj =B()
	obj.getdetails('test','entry',25)
	print(obj.getdetails.__doc__)


	

			
  
