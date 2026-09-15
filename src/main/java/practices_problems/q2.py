def parseStudentRecord(csvLine):
    fields = csvLine.split(",")

    if len(fields) != 3:
        print("Invalid Record")
    else:
        name = fields[0]
        rollNumber = fields[1]
        department = fields[2]

        print("Name:", name, "| Roll No:", rollNumber, "| Dept:", department)


csvLine = input("Enter student record: ")

parseStudentRecord(csvLine)