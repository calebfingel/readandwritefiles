import csv

infile = open('EmployeePay.csv','r')

employee_file = csv.reader(infile,delimiter=',')

next(employee_file)



for record in employee_file:
    
    print("First Name:", record[1])
    print("Last Name:", record[2])
    salary = float(record[3])
    salaryformat = "${:,.2f}".format(salary)
    print("Salary:",salaryformat)
    bonus = float(record[4])*float(record[3])
    bonusformat = "${:,.2f}".format(bonus)
    print("Bonus:",bonusformat)
    total_pay=bonus+salary
    total_payformat = "${:,.2f}".format(total_pay)
    print("Total Pay:", total_payformat)
    input()
    


