
from collections import Counter
marks = [2,3,4,56,7,9,89,90,60]
even_list = [ x for x in marks if x % 2==0]
print(even_list)

square_list = [ x ** 2 for x in marks]
print(square_list)

listy = [99,55,22,22,22,22,22,22,22,222]
counts = Counter(listy)
print(counts)
top = counts.most_common(22)
print(top)

class Plant:
    def  __init__(self):
        self.name = 'plant'
        self.location = 'kiambu'
        
    def getFruit(self):
        print(self.name, self.location)
        
class Mango(Plant):
    def __init__(self):
        # super().__init__()
        print('mango, fruit')
    def mango(self):
        return 'i am a mango fruit'    
        
fruit = Mango()
print(fruit.mango())
        

he = (67, 89)
huu = (90, 55)

print(he + huu)
