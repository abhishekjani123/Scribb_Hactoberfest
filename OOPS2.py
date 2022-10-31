class Student:

    #class variables
    RollNO=""
    Name=""
    CourseName=""
    Fees=""

    #Method to add student record
    def AddStudentRecord(self):
        self.RollNO=input("Enter the roll number: ")
        self.Name=input("Enter the name of the student: ")
        self.CourseName=input("Enter the name of the course: ")
        self.Fees=input("Enter the fees for the course: ")

    #Method to display student record 
    def DisplayStudentRecord(self):
        print("--------Student's Record-------")
        print("RollNo: ",self.RollNO)
        print("Name: ",self.Name)
        print("CourseName: ",self.CourseName)
        print("Fees: ",self.Fees)


#Creating class object and calling methods of the class 
std = Student()
std.AddStudentRecord()
print()
std.DisplayStudentRecord()
print()

