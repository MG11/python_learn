class student:
    # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    
    # inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student('Navin', 2)
s2 = student('Jenny', 3)
print(s1.lap.brand)

# creating inner class object
lap1 = student.Laptop()
print(s1.show())
