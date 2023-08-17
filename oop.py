class students:
    def __init__(self,name,gender,age):
        self.name=name
        self.age=age
        self.gender=gender
    def sayhello(self):
        print("my name is",self.name,"im",self.age,"years",self.gender)

myobje =students("farida","female",18)
myobje =students("mulla","female",20)
myobje =students("jasiri","male",26)
myobje.sayhello()

