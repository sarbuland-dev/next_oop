class Book:
    def __init__(self,name,author,available):
        self.name=name
        self.author=author
        self.available=available
    def book_details(self):
        # print([f"Book: {self.name} By Author:{self.author} is {self.available}"])
        return([self.name,self.author,self.available])
        
class Member:
    def __init__(self,member_name):
        self.name=member_name
        self.borrowed=[]
    def show(self):
        print(f" Member : Mr.{self.name}")

class libary:
    def __init__(self):
        
        
        self.add=[]
        self.member=[]
        
    def add_book(self,name,author,available):
        book=Book(name,author,available)
        self.add.append(book)
        for b in self.add:
         return(b.book_details())
        
        

            
            
            
    
    
name=input("Enter book name ") 
author=input("Enter author name ") 
available=input("available yea or no ").capitalize()  
        
s1=Book(name,author,available) 
s1.book_details() 

name=input("Enter memeber name  ").capitalize()
s2=Member(name)    
s2.show()

s3=libary()
print(s3.add_book(name,author,available))