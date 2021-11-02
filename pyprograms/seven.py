class juice:
    def__init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
    def__str__(self):
        return(self.name+'('+str(self.capacity)+'L)')
    def__add__(self,newjuice):
        self.name+="&" +str(newjuice.name)
        self.capacity+=newjuice.capacity
        return self.__str__
 a=juice('orange',1.5)
 b=juice('apple',3.5)
 print(a__add__b())
