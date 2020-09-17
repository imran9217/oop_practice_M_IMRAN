class University:
    UniName=""
    UniCity=""
    UniAge=""

    def Uni_function(self):
        print("THE UNIVERSITY NAME IS " + str(self.UniName))
        print("THE UNIVERSITY IS IN " + str(self.UniCity))
        print("THE AGE OF UNIVERSITY IS" + str(self.UniAge))
        print("--------------------------------------------")

entery1 =University()
entery1.UniName = "Superior University"
entery1.UniCity ="LAHORE"
entery1.UniAge=100008

entery2 =University()

entery2.UniName = "lLAHORE University"
entery2.UniCity ="LAHORE"
entery2.UniAge=5

entery3 =University()
entery3.UniName = " University OF CENTRAL PUNJAB"
entery3.UniCity ="LAHORE"
entery3.UniAge=18

Universitylist= [entery1,entery2,entery3]


for eachuni in Universitylist:
    eachuni.Uni_function()
print("-------------------------------------------------------------------------------")



class Teacher:
    Name=""
    Subeject=""
    Salary=""

    def Teacher_function(self):
        print("THE TEACHER NAME IS " + str(self.Name))
        print("THE SUBJECT IS IN " + str(self.Subeject))
        print("THE SALARY  IS" + str(self.Salary))
        print("--------------------------------------------")

Tentery1 =Teacher()
Tentery1.Name = "PROF.QASIM RIAZ"
Tentery1.Subeject ="OBJECT ORIENTED PROGRAMING"
Tentery1.Salary=2000000000000

Tentery2 =Teacher()

Tentery2.Name = "IMRAN LIAQAT"
Tentery2.Subeject ="PUNJABI"
Tentery2.Salary=50000

Tentery3 =Teacher()
Tentery3.Name = " SIR ALI FAROOQ"
Tentery3.Subeject ="FARSI"
Tentery3.Salary=18000

TeacherList= [Tentery1,Tentery2,Tentery3]


for eachTeacher in TeacherList:
    eachTeacher.Teacher_function()	