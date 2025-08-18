class student:
    def __init__(self,name):
        self._name=name
    @property
    def show(self):
        return(self._name)
    @show.setter
    def name(self,new_name):
        self._name=new_name
        return(new_name)
        
        
         
s=student("ali")
print(s.show)
s.name="ahm"
print(s.show)
        