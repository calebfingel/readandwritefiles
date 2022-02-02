import csv

infile = open('EmployeePay.csv','r')

employee_file = csv.reader(infile,delimiter=',')

next(employee_file)

for record in employee_file:
    
    print("First Name:", record[1])
    #print("Last Name:", record[2])
    #salary = float(record[3])
    #print("Salary: $",salary,sep="")
    #bonus = float(record[4])
    #print("Bonus: $",bonus,sep="")
    #total_pay=(salary*bonus)+salary
    #print("Total Pay: $", total_pay,sep="")
    input()
    


