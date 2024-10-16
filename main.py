class CSStudent: 
    # Class Variable
    stream = 'cse'
    # The init method or constructor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll
    def setAddress(self, address):
        self.address = address
        # Retrieves instance variable
    def getAddress(self):
        return(self.address)
# Driver Code
add = CSStudent(701)
add.setAddress("Dhaka, Chattogram")
print(add.getAddress())
# Object of CSStudent
a = CSStudent(701)
b = CSStudent(702)
print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.roll) # prints 701
# Class Variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"