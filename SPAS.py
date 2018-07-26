'''
################################# STUDENT PERFORMANCE ANALYSIS SYSTEM ####################################

CT - 033    SOHA
CT - 064    REHAN SATTAR

* -- > Python based project
* -- > My SQL Data base system
* -- > Data extraction with MYSQLdb package of python
* -- > cloud based Admin

###########################################################################################################
'''''
import MySQLdb
def clear():
    print "\n" * 10
def printDict (dict):
    for x,y in dict.items():
        print (x,y)
    print 'Enter Course Code: '
class Admin():

    def check(self,name,password):
        if name =='rehan' or name == 'soha' and password == 'spas':
           return  True

        else:
            print 'Invalid name or password'
            return False

    def delete(self,id):
        import MySQLdb
        # Open database connection
        db = MySQLdb.connect("localhost", "root", "", "spas")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Prepare SQL query to DELETE required records
        sql = "DELETE FROM record WHERE student_id > '%d'" % (id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        # disconnect from server
        db.close()

    def View(self):

        import MySQLdb

        db = MySQLdb.connect("localhost", "root", "", "spas")

        cursor = db.cursor()

        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 1"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        cursor = db.cursor()
        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (1)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]
        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 2"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        cursor = db.cursor()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (2)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]

        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 3"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        cursor = db.cursor()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (3)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]
        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 4"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        cursor = db.cursor()
        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (4)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]

        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 5"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        cursor = db.cursor()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (5)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]
        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA,semester, year FROM record WHERE student_id = 13"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (13)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]
        cursor = db.cursor()

        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA, semester, year FROM record WHERE student_id = 15"

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (15)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ", row[0]
        db.close()


class Teacher():

    def teacherLogin(self):
        name = str(raw_input('Enter name: '))
        password = str(raw_input('Enter password: '))
        if name == 'MMK' and password == 'ned123':
            return True
        else:
            return False

    def teacherInput(self):
        classPerformance = raw_input("Enter Class Performance: ")
        classTest = int(raw_input("Enter Test Marks: "))
        midTerm = int(raw_input("Enter Mid Term Marks: "))
        labMarks = int(raw_input("Enter Lab Marks: "))
        projectMarks = int(raw_input("Enter Project Marks: "))
        sessionalMarks = int(raw_input("Enter Sessional MArks : "))
        attendenc = int(raw_input("Enter the attendance: "))
        finalMarks = int(raw_input("Enter Final Exams: "))
        print "Thank you ! You have Entered the data successfully !! "
        return classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks

    # def WRITE_IN_SQL(self):
    #     '''
    #     INSERT INTO TABLE_OF_STUDENT(ClassPerformance, midTerm, classTest, LabTest, Project, attendance, Sessional,Final)
    #     *---> ONCE INSERTED CAN NOT CHANGE!
    #     :return:
    # '''
    #     db = MySQLdb.connect("localhost", "root", "", "spas")
    #     cursor = db.cursor()
    #        # sql = "SELECT * from INSERT INTO record (class )"
    #     # sql = "INSERT INTO record course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA, semester, year"
    #        #SQL writing !

'''########################## CLASS END #################################'''

class Analysis():

    def reprot(self,gpa):
        '''
          * READ FROM SQL
          *--> THE MAIN GPA AND PROGRESS CALCULATION WILL BE THE ANALYSIS SYSTEM !

          ANALYSIS AND SUGGESSIONS HERE:

          *--> THINGS WHICH ARE BEST !
          *--> THINGS WHICH ARE GOOD !
          *--> THINGS WHICH ARE GOOD !

          *--> SHOW SPECIFIC DATA SUBJECT WISE ? OR OVER ALL DATA REPORT ? MEANS GENERAL FORMAT ?
          :return: TRUE IF STUDENT_REPORT == PERFECT ? FALSE : STUDENT_REPORT == NON_PERFECT !
          '''


        #open SQL SERVER
        #fetch data via id number :
        # Gpa = SQL QUERY
        if gpa >1.5 and gpa < 2:
            # clear()
            print "\n\n* Your GPA And all records show that you are little bit weak in some things: "
            print "\n*-These are some key points for you : \n\n"
            print "There is no short cut to success:\n2 - Be ambitious to attain success.\n3 - Forget the past and live in present.\n4 - Develop a positive outlook.\n5Respect criticism:"
        elif gpa >= 2  and gpa < 2.5 :
            # clear()
            print "\n\n* Your GPA And all records show that you are an average student "
            print "\n*-These are some key points for you : \n\n"
            print "1 - Don't wait for something outside of yourself to make you happy in the future so SET YOUR GOALS!\n2 - No one ever did it right all the time. But most that have experienced some success have failed at some point. \
                   \n3 - This point is, life is about balance. The good and the bad. The highs and the lows. The pina and the colada. Live a balanced one!   \n4 - Don't stop learning because life is so much more satisfying when we make a new friend every day.\
                   \n5  - Remember to thank your earliest mentors, your parents, teachers, and others, who inspired you to succeed and set you on your journey."
            print "Remember : \n\t\"If you have passion of learning you can bring 25th hour in a day ! never give up!  \""
        elif gpa >= 2.5 and gpa <= 3.5:
            # clear()
            print "\n\n* Your GPA And all records show that you are a good student and wants to be perfect. "
            print "\n*-These are some key points for you : \n\n"
            print "1 - You are a good student and try to be good !  \n2 - You need to spend time crawling alone through shadows to truly appreciate what it is to stand in the sun. \n3 - Try to learn online more and more and give your best \n" \
                  "\n4 - Best thing is you have a good enough scor to get a job so be confident! "
            print "Remember : \n\n\"PUSH YOUR SELF BECAUSE NO ONE IS HERE TO DO IT FOR YOU! \""
        elif gpa > 3.5 and gpa <= 4:
            print "\n* Your GPA And all records show that you are one of best student "
            print "\n*-These are some key points for you : \n\n"
            print "1 - You have a good GPA but do you have a great reason for this ? \n2 - Keep your mind active by doing some activities.\
            \n3 - Buil self confidence just like you marks.\n4 - Have a big reason to study great!  \n5 - Always be thankfull to your creator ! "
            print "REMEMBR: \n\t\"WHEN LIFE BECOMES HARDER , CHANGE YOURSELF TO BECOME STRONGER.\""

'''############################################################# MAIN STARTED ##################################################################################'''
def main():

    print '**************************************************'
    print 'WELCOME TO STUDENT PERFORMANCE ANAYLYSIS SYSTEM'
    print '**************************************************'
    print '1-Admin Login\n2-Teacher Login\n3-Student Login\n'
    option = int(input('Enter Your Choice: '))
    if option == 1:
        name = str(raw_input('Enter name: '))
        password = str(raw_input('Enter password: '))
        admin = Admin()
        isOk = admin.check(name.lower(), password.lower())
        clear()
        print 'Hello Sir/Mam'
        op = int(raw_input("1 - View Data \n2 - Delete Data"))
        if op == 1:
            admin.View()
        elif op == 2:
            id = input(raw_input("Enter Student_id: "))
            admin.delete(id)
        else:
            print "\n\n Please enter right option! "
            main()
    elif option == 2:
        print "Hello Sir/Mam"
        print "1-First Year \n2-Second year\n3-Third year\n4-Final Year"
        classCode = int(raw_input("Enter the Year : "))
        if classCode == 1:
            print '1-FALL SEMESTER\n2-SPRING SEMESTER\n'
            semester = int(raw_input("Enter the Semester" ))
            if semester == 1:
                fcitCourseListFall = {
                    "CT-153": "Programming Languages (Theory)",
                    "CT-153": "Programming Languages (Practical)",
                    "CT-174": "Fundamentals of Information Technology (Theory)",
                    "CT-174": "Fundamentals of Information Technology (Practical)",
                    "MT-171": "Differential and Integral Calculus",
                    "El-134": "Basic Electronics (Theory)",
                    "EL-134": "Basic Electronics (Practical)",
                    "HS-205": "Islamic Studies",
                    "HS-209": "Ethical Behaviour(For Non-Muslims)"
                }

                printDict(fcitCourseListFall)
                courseCode = raw_input('Enter course code: ')
                if courseCode in fcitCourseListFall :
                    t1= Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa

                        main()
                    else :
                        print "Invalid name or password! "
                        main()
            elif semester == 2:
                fcitCourseListSpring = {

                    "CT-157": "Data Structures Algorithms and Applications (Theory)",
                    "CT-157": "Data Structures Algorithms and Applications (Practical)",
                    "CT-162": "Discrete Structures",
                    "CT-251": "Object Oriented Programming(Theory)",
                    "CT-251": "Object Oriented Programming(Practical)",
                    "HS-104": "Functional English",
                    "HS-105": "Pakistan Studies",
                    "HS-127": "Pakistan Studies(For Foriegners)"
                }
                printDict(fcitCourseListSpring)
                courseCode = raw_input()
                if courseCode in fcitCourseListSpring :
                    t1= Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                    else :
                        print "Invalid name or password! "
                        main()
        elif classCode == 2:
            print '1-FALL SEMESTER\n2-SPRING SEMESTER\n'
            semester = int(raw_input("Enter the Semester"))
            if semester == 1:
                scitCourseList = {

                    "CS-251": "Login Design & Switching Theory (Theory)",
                    "CS-251": "Login Design & Switching Theory (Practical)",
                    "CT-352": "Computer Graphics(Theory)",
                    "CT-352": "Computer Graphics(Practical)",
                    "CT-258": "Financial & Cost Accounting ",
                    "CT-259": "System Analysis and Design",
                    "MT-273": "Differential Equations and Linear Algebra"
                }
                printDict(scitCourseList)
                courseCode = raw_input()
                if courseCode in scitCourseList:
                    t1 = Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        main()
                    else:
                        print "Invalid name or password! "
                        main()
            elif semester == 2:
                scitCourseListSpring = {

                    "CS-252": "Computer Architecture and Organization (Theory)",
                    "CS-252": "Computer Architecture and Organization (Practical)",
                    "CS-257": "Data Base Management System",
                    "CT-362": "Web Engineering (Theory)",
                    "CT-362": "Web Engineering (Practical)",
                    "HS-208": "Business Communications & Ethics",
                    "MT-331": "Probability & Statics"
                }
                printDict(scitCourseListSpring)
                courseCode = raw_input()
                if courseCode in scitCourseListSpring:
                    t1 = Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        main()
                    else:
                        print "Invalid name or password! "
                        main()
        elif classCode == 3:
            print '1-FALL SEMESTER\n2-SPRING SEMESTER\n'
            semester = int(raw_input("Enter the Semester"))
            if semester ==1 :
                tcitcourseListFall = {
                    "CT-360": "Visual Programming (Theory)",
                    "CT-360": "Visual Programming (Practical)",
                    "CS-353": "Microprocessors and thier Applications (Theory)",
                    "CS-353": "Microprocessors and thier Applications (Practical)",
                    "CT-363": "Operating Systems (Theory)",
                    "CT-363": "Operating Systems (Practical)",
                    "CT-462": "Distributed Computing (Theory)",
                    "CT-462": "Distributed Computing (Practical)"
                }
                printDict(tcitcourseListFall)
                courseCode = raw_input()
                if courseCode in tcitcourseListFall:
                    t1 = Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        main()
                    else:
                        print "Invalid name or password! "
                        main()
                elif semester == '2':
                    tcitcourseListSpring = {
                        "CS-351": "Computer Communication Networks(Theory)",
                        "CS-351": "Computer Communication Networks(Practical)",
                        "CT-365": "Software Engineering",
                        "CT-364": "Theory of Automated and Formated Languages",
                        "CT-361": "Artificial Inelligence & Expert systems (Theory)",
                        "CT-361": "Artificial Intelligence & Expert systems (Practical)",
                        "CT-366": "E-Commerce"
                    }
                    printDict(tcitcourseListFall)
                    courseCode = raw_input()
                    if courseCode in tcitcourseListFall:
                        t1 = Teacher()
                        if t1.teacherLogin():
                            classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                            print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        else :
                            print "Invalid Name or user .."
                            main()
        elif classCode == 4:
            print '1-FALL SEMESTER\n2-SPRING SEMESTER\n'
            semester = int(raw_input("Enter the Semester"))
            if semester == 1:
                bcitCourseListFall = {
                    "CT-460": "Network and Information Security(Theory)",
                    "CT-460": "Network and Information Security(Practical)",
                    "CT-464": "Modeling and Simulations",
                    "CT-463": "Data Warehousing & Mining (Theory)",
                    "CT-463": "Data Warehousing & Mining (Practical)",
                    "CT-442": "Numarical Methods",
                    "CT-499": "Software Based Project"
                }
                printDict(bcitCourseListFall)
                courseCode = raw_input()
                if courseCode in bcitCourseListFall:
                    t1 = Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        main()
                    else:
                        print "Invalid name or password! "
                        main()
            elif semester == 2:
                bcitCourseListSpring = {
                    "CT-451": "Parallel Processing (Theory)",
                    "CT-451": "Parallel Processing(Practical)",
                    "CT-465": "Compiler Design",
                    "CT-499": "Software Based Project",
                    "HS-403": "Enterpreneurships",
                    "Elective Courses": {

                        "CT-481": "Wireless Networks & Mobile Computing(Theory)",
                        "CT-481": "Wireless Networks & Mobile Computing(Practical)",
                        "CT-482": "Bio-Informatics(Theory)",
                        "CT-482": "Bio-Informatics(Practicals",
                        "CT-483": "System Administration(Theory)",
                        "CT-483": "System Administration(Practical)"
                    }
                }
                printDict(bcitCourseListSpring)
                courseCode = raw_input()
                if courseCode in bcitCourseListSpring:
                    t1 = Teacher()
                    if t1.teacherLogin():
                        classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa = t1.teacherInput()
                        print classPerformance, classTest, midTerm, labMarks, projectMarks, sessionalMarks, finalMarks, gpa
                        main()
                    else:
                        print "name or password! "
                        main()
    elif option == 3:

        year = int(raw_input("Enter your year : "))
        rollNumber = int(raw_input("Enter your id number: "))

        db = MySQLdb.connect("localhost", "root", "", "spas")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "SELECT course_id, class_per , class_test, mid_term, lab_test, project, attendance, ts_marks, tf_marks, ps_marks, pf_marks, t_marks, GPA, semester, year FROM record WHERE student_id ='%d'" %(rollNumber)

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print '\nYear: ', row[14]
            print 'Semester: ', row[13]
            print 'Course id: ', row[0]
            print "Class Performance:", row[1]
            print 'Class Test: ', row[2]
            print 'Mid Term: ', row[3]
            print 'Lab Test: ', row[4]
            print 'Project: ', row[5]
            print 'Attendence: ', row[6]
            print 'Theory Sessional: ', row[7]
            print 'Theory Final: ', row[8]
            print 'Practical Sessional: ', row[9]
            print 'Practical Final: ', row[10]
            print 'Total Marks: ', row[11]
            print 'GPA: ', row[12]
            print '\n**********'
            row = cursor.fetchone()

        sql_ = "SELECT AVG(GPA) FROM record WHERE student_id = '%d'" % (rollNumber)
        cursor.execute(sql_)
        # print sql_
        row = cursor.fetchone()
        print "CGPA: ",row[0]
        A = Analysis()
        A.reprot(row[0])
        db.close()
        main()
    else :
        main()
try :
    main()
except:
    clear()
    # print "OH sorry there is a bug in this option now  ! Developer will fix it in a while."
    main()


'''
###########################################============COMPLETED=================########################################
Database design and algorithm : Soha Moosa  CT - 033    
Project developer : Rehan Sattar            CT - 064    

Special thanks to: Engr.Abdul Sami Haroon Khan (BESE NED) for helping us in the best way.
#perfect ! 
'''