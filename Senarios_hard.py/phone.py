class phone:
    def __init__(self):
        self.call_history=[]
        

    def call (self):
        
        while True:
            num=input("Enter your number  ")
            print(f"you want to call on that number {num} ")
            choice=input("(Yes/No) ").capitalize()
            if choice=="Yes":
              print(f"calling.....")
              end=input("you want to exit (yes/no)").capitalize()
              if end=="Yes":
                  self.call_history.append(num)
                  print(f"call end on {num}, thanks for using jazz network")
                  break
              else:
                  exit()
            
            elif choice=="No":
              print("OK! ")
    def text(self):
        while True:
            num=input("Enter phone number ")
            choice=input(f"You want to send text on that number {num} (Yes/No)  ").capitalize()
            if choice=="Yes":
                text=input("Enter your text:  ")
                print(f"{text} send to {num}")
                break
            else:
                exit()
            
my_phone=phone()            
while True:            
  choice=input("you want call or text").capitalize()
  if choice=="Call":
     my_phone.call()
  elif choice=="Text":
    my_phone.text()       
     


        

        
         

        
       