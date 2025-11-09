class Shubham:
    def __init__(self, p, d, s="shubham"):  
        self.p = p 
        self.d = d  
        self.s = s  
    
    def display(self):
        v=6
        print(f"Name: {self.s}, p = {self.p}, d = {self.d} v={v}")


obj = Shubham(2, 4)  


obj.display() 


obj2 = Shubham(10, 20, "Rama")
obj2.display()  
