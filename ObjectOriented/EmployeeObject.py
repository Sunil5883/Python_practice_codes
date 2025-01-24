class Employee:
    company_name = "Code" # class Based Variables

    def __init__(self,name,age,dsg):
        self.name = name
        self.age = age
        self.dsg = dsg
    
    def login(self, time):
        print(f"{self.name} logged in at {time}")
    
    def logout(self,time):
        print(f"{self.name} loggedOut at {time}")

    def work(self,hours):
        print(f"{self.name} worked for {hours}")
    
    def employeeDetails(self):
        print(f"Employee Name: {self.name}")
        print("Employee Age:", self.age)
        print("Employee Designation:", self.dsg)

e1 = Employee("Sunil", 22, "SFD")
e1.employeeDetails()
print()
e1.login("10:15 AM")
e1.work("6 HRS")
e1.logout("4:15 PM")

print("----------------------")
e2 = Employee("Nikhil", 24, "WD")
e2.employeeDetails()
print()
e2.login("9:00 AM")
e2.work("8 HRS")
e2.logout("5:00 PM")

print("------------------------")
e3 = Employee("Hari", 30, "SE")
e3.employeeDetails()
print()
e3.login("9:00 AM")
e3.work("8 HRS")
e3.logout("5:00 PM")