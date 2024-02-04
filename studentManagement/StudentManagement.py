import sqlite3

def createDatabase():
    con = sqlite3.connect("studentManagement.db")
    con.execute("PRAGMA foreign_keys = 1")
    return con

def createTables(cur):
    cur.execute("CREATE TABLE  IF NOT EXISTS student(studentId Integer Primary Key AUTOINCREMENT, studentName text)")
    cur.execute("CREATE TABLE  IF NOT EXISTS subject(subjectId Integer Primary Key AUTOINCREMENT, subjectName text)")
    cur.execute("CREATE TABLE  IF NOT EXISTS result(studentId Integer, subjectId Integer , mark float, foreign Key(studentId) references student(studentId), foreign Key(subjectId) references subject(subjectId))")
    
def addStudent(cur):
    studentName = input("Enter Student Name:")
    cur.execute("Insert into student(studentName) values(?)", (studentName,))
    
def deleteStudent(cur):
    studentId = int(input("Enter Student id to be deleted:"))
    cur.execute("delete from result where studentId=?", (studentId,))
    cur.execute("delete from student where studentId=?", (studentId,))
    
def modifyStudentName(cur):
    studentId = int(input("Enter Student id to be Modified:"))
    studentName = input("Enter New Student Name:")
    cur.execute("update  student set studentName=? where studentId=?", (studentName,studentId,))
    
def addSubject(cur):
    subjectName = input("Enter Subject Name:")
    cur.execute("Insert into subject(subjectName) values(?)", (subjectName,))
    
def deleteSubject(cur):
    subjectId = int(input("Enter Subject id to be deleted:"))
    cur.execute("delete from result where subjectId=?", (subjectId,))
    cur.execute("delete from subject where subjectId=?", (subjectId,))
    
def modifySubject(cur):
    subjectId = int(input("Enter Subject id to be Modified:"))
    subjectName = input("Enter New Subject Name:")
    cur.execute("update  subject set subjectName=? where subjectId=?", (subjectName, subjectId,))
    
def addResult(cur):
    studentId = int(input("Enter Student Id:"))
    subjectId = int(input("Enter Subject id:"))
    mark = float(input("Enter Mark:"))
    cur.execute("Insert into result values(?,?,?)", (studentId, subjectId, mark,))
    
def viewStudents(cur):
    cur.execute("select * from student")
    print("**********STUDENT DETAILS****************")
    print("Student Id \t Student Name")
    for row in cur.fetchall():
        print(row[0], "\t\t", row[1])
    print("**********END***************************")
        
def viewSubjects(cur):
    cur.execute("select * from subject")
    print("**********SUBJECT DETAILS****************")
    print("Subject Id \t Subject Name")
    for row in cur.fetchall():
        print(row[0], "\t\t", row[1])
    print("**********END***************************")
        
def viewResults(cur):
    cur.execute("select student.studentName, subject.subjectName,result.mark from result join student, subject on student.studentId=result.studentId and subject.subjectId=result.subjectId")
    print("**********RESULT****************")
    print("Student Name \t Subject Name \t Mark")
    for row in cur.fetchall():
        print(row[0], "\t\t", row[1],  "\t", row[2])
    print("**********END***************************")
    
def viewMarkOfAStudent(cur):
    studentId = int(input("Enter Student Id:"))
    cur.execute("select studentName from student where studentId=?", (studentId,))
    studentData = cur.fetchall()
    cur.execute("select subject.subjectName, result.mark from result join subject on subject.subjectId=result.subjectId and result.studentId=?", (studentId,))
    print("**********RESULT****************")
    print("Student Name:", studentData[0])
    print("Subject Name \t Mark")
    for row in cur.fetchall():
        print(row[0], "\t", row[1])
    print("**********END***************************")
    
def toppersOfSubject(cur):
    cur.execute("select student.studentName,subject.subjectName, max(result.mark) from result  join student, subject on student.studentId=result.studentId and subject.subjectId=result.subjectId GROUP by result.subjectId")
    print("**********RESULT****************")
    print("StudentName \t Subject Name \t Mark")
    for row in cur.fetchall():
        print(row[0], "\t", row[1], "\t", row[2])
    print("**********END***************************")
    
def averageOfSubject(cur):
    cur.execute("select subjectName, avg(mark) from result join subject on subject.subjectId=result.subjectId GROUP by result.subjectId")
    print("**********RESULT****************")
    print("SubjectName \t Avg(Mark)")
    for row in cur.fetchall():
        print(row[0], "\t", row[1])
    print("**********END***************************")
    
def topFiveMarks(cur):
    cur.execute("select subjectName, studentName, mark from result JOIN subject, student on subject.subjectId = result.subjectId and student.studentId = result.studentId order by mark DESC LIMIT 5")
    print("**********RESULT****************")
    print("SubjectName \t Student Name\tMark")
    for row in cur.fetchall():
        print(row[0], "\t", row[1], "\t", row[2])
    print("**********END***************************")
    
connection = createDatabase()
cur = connection.cursor()
createTables(cur)

while(True) :
    option = input("""Please Enter option\n
               1:Add Student
               2:Add Subject
               3:Add Result
               4:Modify Student
               5:Modify Subject
               6:Delete Student
               7:Delete Subject
               8:View Student
               9:View Subject
               10:View Result
               11:View Result of a student
               12:Toppers of a subject
               13:Average of subject
               14:Top 5 Marks
               Q:Quit
               """)
    match option:
        case "1":
            addStudent(cur)

        case "2":
            addSubject(cur)

        case "3":
            addResult(cur)
    
        case "4":
            modifyStudentName(cur)

        case "5":
            modifySubject(cur)

        case "6":
            deleteStudent(cur)
        
        case "7":
            deleteSubject(cur)
            
        case "8":
            viewStudents(cur)
            
        case "9":
            viewSubjects(cur)
            
        case "10":
            viewResults(cur)
            
        case "11":
            viewMarkOfAStudent(cur)
            
        case "12":
            toppersOfSubject(cur)
            
        case "13":
            averageOfSubject(cur)
            
        case "14":
            topFiveMarks(cur)
        
        case "Q":
            break
    connection.commit()

connection.close()





