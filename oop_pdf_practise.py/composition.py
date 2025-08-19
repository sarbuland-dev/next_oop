# class emploee:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def __str__(self):
#         return f"{self.name},{self.age},{self.id}"



# class company:
#     def __init__(self,name):
#      self.name=name
#      self.emploees=[]
#     def add_emploee(self,emploee):
#         self.emploees.append(emploee)
#     def show(self):
#         if not self.emploees:
#             print("no emploee") 
#         else:
#             for i in self.emploees:
#                 print(i)
    

            
            
# e1=emploee("sar",23,2345)
# e2=emploee("ahmad",21,2367)
# com=company("sb company")
# com.add_emploee(e1)
# com.add_emploee(e2)
# com.show()
            
# senrio 2
# class bankaccounts:
#     def __init__(self,account_balance,number):
#         self.account_balance=account_balance
#         self.number=number
#     def __str__(self):
#         return f"{self.account_balance},{self.number}"
        
        


# class bank:
#     def __init__(self,name):
        
#         self.name=name
        
#         self.accounts=[]
#     def add(self,bankaccounts):
#         self.accounts.append(bankaccounts)
#     def show(self):
#         if not self.accounts:
#             print("There is no account ")
#         else:
#             for i in self.accounts:
#                 print(i)
    
#     def bal(self):
       
#      Total=sum(i.account_balance for i in self.accounts)
#      print(Total)
                

        
# b1=bankaccounts(1000,3456) 
# b2=bankaccounts(2000,34589) 
# ba=bank("sb bank") 
# ba.add(b1)
# ba.add(b2)
# ba.show()
# ba.bal()
       

class Person:
    def __init__(self, name, home_town):
        self.person_name = name
        self.location = home_town
    
    def show(self, greet=""):
        print(f"{greet} {self.person_name} from {self.location}")

p = Person("Hassan", "Pattoki")

p.show()