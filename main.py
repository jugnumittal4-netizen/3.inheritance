class bus:
    def __init__(self,colour):
        self.colour = colour
    def showtraits(self):
        print("colour",self.colour)
        
class kid(bus):
    def __init__(self,colour,size):
        self.size = size
        super().__init__(colour)
    def showtraits(self):
            print("colour",self.colour)
            print("size",self.size)
            super().showtraits
a = input("enter the colour of the bus")
b = input("enter the size of the bus")

child = kid(a,b)
child.showtraits()