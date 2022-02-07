import csv

averages = open('Student_Scores.csv','r')
averages_file = csv.reader(averages,delimiter=',')
outfile = open("student_avg.csv","w")

for record in averages_file:
    student_average = "{:.2f}".format((int(record[1])+int(record[2])+int(record[3]))/3)
    #print(student_average)
    outfile.write(f"{record[0]}\'s average is {student_average}")
    outfile.write("\n")

outfile.close()
averages.close()
