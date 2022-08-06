# Python program to execute
# main directly
print ("Always executed")
# Python program to execute
# function directly
def my_function():
	print ("I am inside function")

# We can test function by calling it.
# my_function()
print(__name__)
if __name__ == "__main__":
    print ("Executed when invoked directly")
    print ("Executed when invoked directly")
    my_function()
    
    my_function()   
else:
	print ("Executed when imported")
