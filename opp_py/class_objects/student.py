class Student:
    def __init__(self,name,roll_no,father_name,address):
        self.name=name
        self.roll_no=roll_no
        self.father_name=father_name
        self.address=address
    def info(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Father Name:",self.father_name)
        print("Address:",self.address)