class familymember:
    def __init__(self,eye_colour,hieght):
        self.eye_colour = eye_colour
        self.hieght = hieght
    def shholw_traits(self):
        print("eye colour:",self.eye_colour)
        print("hieght",self.hieght)
class kid(familymember):
    def __init__(self,name,age,eye_colour,hieght):
        self.name = name
        self.age = age
        super().__init__(eye_colour,hieght)
    def shholw_traits(self):
        print("name",self.name)
        print("age:",self.age)
        super().shholw_traits()
    def favourate_hobby(self,hobby):
        print(self.name,"loves",hobby)
child = kid("vedansh",10,"brown",144)
child.shholw_traits()
child.favourate_hobby("swimming")
print("is kid a part of family memeber?",issubclass(kid,familymember))

