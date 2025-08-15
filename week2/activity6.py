class Employee:
    def __init__(self, name, salary, job_title):
        # Remember the employee's basic information
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        # Print the employee's details
        print(f"{self.name} works as a {self.job_title} and earns {self.salary}.")

    def give_raise(self, amount):
        # Add more money to the salary
        self.salary += amount
        print(f"{self.name} got a raise of {amount}!")
        print(f"New salary is {self.salary}.")


# HR hires two employees
ram = Employee("Ram", 30000, "Manager")
sita = Employee("Sita", 25000, "Accountant")
hari = Employee("hari", 6000, "Cashier")
# HR checks their records
ram.display_info()
sita.display_info()
hari.display_info()

# Ram is rewarded for his work
ram.give_raise(2000)

#update salary display
ram.display_info()


#In my program, HR hires two employees  Ram and Sita. Ram is a Manager with a salary of 30,000 and 
# Sita is an Accountant with a salary of 25,000.
# First, HR checks the records by calling display_info() for each employee.
#Then, Ram gets rewarded for his good work, so HR calls give_raise(2000), and 
# his salary updates