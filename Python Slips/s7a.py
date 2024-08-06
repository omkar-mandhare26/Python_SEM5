class complexNum:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def sum(self,num):
        return complexNum(self.real+num.real, self.imaginary+num.imaginary)
    
    def display(self):
        print(f"{self.real}+{self.imaginary}i")
    
num1 = complexNum(2,3)
num2 = complexNum(1,4)
num3 = num1.sum(num2)
num3.display()
