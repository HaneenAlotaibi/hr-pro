from antigravity import geohash


class Employee:
   #Employee class here
    def __init__(self, name,age,salary,employment_years):
      self.name=  name
      self.age=age
      self.salary=salary
      self.employment_years=employment_years

    def get_annual_salary(self):
        return  self.salary * 12
    def __str__(self):
        return f' Name: {self.name} ,  Age:  {self.age}, salary: {self.salary}, employment years: {self.employment_years} and annual salary: {self.get_annual_salary()}'

#print(Employee('hamsd',22,500,8))
class Manager(Employee):
#     #Manager class here
    def __init__(self, name,age,salary,employment_years,bonus_percentage):
        super().__init__(name,age,salary,employment_years)
        self.bonus_percentage=bonus_percentage
    def get_bonus(self):
       return self.bonus_percentage * self.salary    
    def __str__(self):
        return f' Name: {self.name} ,  Age:  {self.age}, salary: {self.salary}, employment years: {self.employment_years} , annual salary: {self.get_annual_salary()} and bonus is {self.get_bonus()}'
#print(Manager('hamsd',22,500,8,5))

#Employee_list=[['Laila', 24, 9999,4],['Moh',27,999,2]]
Manager_list=[]
Employee_list=[]
Employee_list.append( Employee('Laila', 24, 9999,4) )
Employee_list.append( Employee('Moh',27,999,2) )
Manager_list.append(Manager('sammy', 52,4600, 119,4 ))
#Employee_list.append( Employee('Reaper', 44) )
  
# for obj in Employee_list:
#     print( obj.__str__())
for obj in Manager_list:
    print( obj.__str__())

#print(Employee(Employee_list))

def main():
# 	# main code here
  print("Welcome to HR Pro")
  print("Options:")
  print("1. Show Employees \n2. Show Managers \n3. Add An Employee \n4. Add A Manager \n5. Exit")
  user_Options=int(input("What would you like to do? "))
  while (user_Options !=5):
    # print("Options:")
    # print("1. Show Employees \n2. Show Managers \n3. Add An Employee \n4. Add A Manager \n5. Exit")
    # user_Options=int(input("What would you like to do? "))
    if user_Options ==1:
       print('-----------------') 
       print('Employee')
       for obj in Employee_list:
        print( obj.__str__())
       print('-----------------') 
    if user_Options ==2:
     print('-----------------')
     print('Managers')
     for obj in Manager_list:
      print( obj.__str__())
     print('-----------------') 
    if user_Options ==3: 
     print('-----------------') 
     print('Employee')
     user_name=input('name: ')
     user_age=int(input('age: '))
     user_salary=int(input('salary: '))
     user_Employement_years=int(input('Employement years: '))
     Employee_list.append( Employee(user_name, user_age, user_salary,user_Employement_years) )
     print("Employee added succesfully")

     print(Employee_list[len(Employee_list) -1].__str__())
     print('-----------------') 
    if user_Options ==4:
     print('-----------------') 
     print('Manager')  
     user_name=input('name: ')
     user_age=int(input('age: '))
     user_salary=int(input('salary: '))
     user_Employement_years=int(input('Employement years: '))
     user_Bonus=int(input('Bonus: '))
     Manager_list.append( Manager(user_name, user_age, user_salary,user_Employement_years,user_Bonus) )
     print("Manager added succesfully")
     print(Manager_list[len(Manager_list) -1].__str__())
     print('-----------------') 
     
    
    if user_Options ==5:
      break

    print("Options:")
    print("1. Show Employees \n2. Show Managers \n3. Add An Employee \n4. Add A Manager \n5. Exit")
    user_Options=int(input("What would you like to do? "))
if __name__ == '__main__':
 	main()
   