class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info():
        print("Last name - "+self.last_name )
        print("Eye color - "+self.eye_color )

class Child(Parent):
    def __init__(self, last_name, eye_color,number_of_toys ):
        print(" Beta appears")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    
#baapu = Parent("baapu","black")
#print(baapu.last_name)
don = Child("kaku", "black", 4)
don.show_info()

#print(don.last_name)
#print(don.number_of_toys)
