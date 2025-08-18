import random
x=["eat", "tea", "tan", "ate", "nat", "bat"]
final1=[]
final2=[]
final3=[]
target="ant"

for word in x:
    if sorted(word)==sorted(target):
      final1.append(word)

print(final1)


    
    