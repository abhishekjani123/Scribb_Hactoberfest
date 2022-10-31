class Employee:

    #Class Data Members
    EmpID = ""
    Name = ""
    Salary = 0

    #Method to fetch employee details
    def EmployeeRecord(self):

        self.EmpID = input("Enter the EmpID: ")
        self.Name = input("Enter the name of the Employee: ")
        self.Salary = int(input("Enter the salary of the Employee: "))


#Class FullTimeEmp inherits from class Employee
class FullTimeEmp(Employee):
    
    DA = 10000
    HRA = 5000
    TotalSalary = 0

    #Method to fetch Employee's TotalSalary
    def Total_Salary(self):
        self.TotalSalary = self.DA+self.HRA+self.Salary
        print("\nTotal Salary of the Employee "+self.EmpID+" is: ",self.TotalSalary)


#class object and method calls
FTE=FullTimeEmp()
FTE.EmployeeRecord()
FTE.Total_Salary()
