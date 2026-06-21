def Class_result():
    #class result
  z=input("Total no of students in class is 10")
  print(z)
  y=input("the names and mark percentage of the student are mentioned below")
  print(y)
  
  ROLLno1 = input("zia90%")
  ROLLno2 = input("mia85%")
  ROLLno3 = input("ken40%")
  ROLLno4 = input("sea51%")
  ROLLno5 = input("cane60%")
  ROLLno6 = input("lia23%")
  ROLLno7 = input("bav45%")
  ROLLno8 = input("ren52%")
  ROLLno9 = input("wein76%")
  ROLLno10 = input("nick91%")
   
  print("ROLL NO 1 mark %:",ROLLno1)
  print("ROLL NO 2 mark %:",ROLLno2)
  print("ROLL NO 3 mark %:",ROLLno3)
  print("ROLL NO 4 mark %:",ROLLno4)
  print("ROLL NO 5 mark %:",ROLLno5)
  print("ROLL NO 6 mark %:",ROLLno6)
  print("ROLL NO 7 mark %:",ROLLno7)
  print("ROLL NO 8 mark %:",ROLLno8)
  print("ROLL NO 9 mark %:",ROLLno9)
  print("ROLL NO 10 mark %:",ROLLno10)

  zia=90
  mia=85
  ken=96
  sea=79
  cane=91
  lia=83
  bav=98
  ren=92
  wein=76
  nick=97

  print(zia)
  print(mia)
  print(ken)
  print(sea)
  print(cane)
  print(lia)
  print(bav)
  print(ren)
  print(wein)
  print(nick)
  avg = (zia+mia+ken+sea+cane+lia+bav+ren+wein+nick)/10
  print("avg class percentage is :",avg)

  if avg>90 and avg<100:
    print("The class result is A")
  elif avg>80 and avg<90:
    print("The class result is b")
  elif avg>70 and avg<80:
    print("The class result is c")
  else:
    print("The class result is D")
    
def student_reportcard():
 #student  report card
 student_number=int(input("enter the serial number of student - "))
 student_name=input("enter the name of the student -")
 roll_no=input("enter the student roll number -")
 class_number=input("enter the class of the student -")
 print("student name is -",student_name)
 print("roll number is -",roll_no)
 print("student class -",class_number)
 M=float(input("enter the maths marks ="))
 print("maths marks are conducted for 100")
 C=float(input("enter the cs marks ="))
 print("cs marks are conducted for 100")
 E=float(input("enter the english marks ="))
 print("english marks are conducted for 100")
 P=float(input("enter the Physics marks ="))
 print("Physics marks are conducted for 100")
 Ch=float(input("enter the chemistry marks ="))
 print("chemistry marks are conducted for 100")
 K=(M+C+E+P+Ch)
 print("total marks obtained by the student is -",K)
 print("Total marks are conducted for exam is - 500")
 Q=K/5
 print("Average of the student is -",Q)
 if Q>90 and Q<=100:
  print("congratualtions your Grade is A")
 if Q>97 and Q<=100:
  print("you are a topper student and you will get topper medal")
 elif Q>80 and Q<=90:
  print("good your grade is B")
 elif Q>70 and Q<=80:
  print("keep it up Your grade is c")
 elif Q>60 and Q <=70:
  print("not bad get higher and your grade is D")
 elif Q<=50:
  print("sorry you are failed")
  
#display all students record
def display_studentrecord():
 name=input("enter student name=zia")
 print(name)
 rollno=input("roll no 1")
 print(rollno)
 #marks
 english=input("mark in english: 90")
 print(english)
 maths=input("mark in maths: 99")
 print(maths)
 chemistry=input("mark in chemistry: 85")
 print(chemistry)
 physics=input("mark in physics: 82")
 print(physics)
 computerscience=input("mark in computerscience: 95")
 print(computerscience)


 name=input("enter student name=mia")
 print(name)
 rollno=input("roll no 2")
 print(rollno)
 #marks
 english=input("mark in english: 80")
 print(english)
 maths=input("mark in maths: 90")
 print(maths)
 chemistry=input("mark in chemistry: 82")
 print(chemistry)
 physics=input("mark in physics: 85")
 print(physics)
 computerscience=input("mark in computerscience: 90")
 print(computerscience)

 name=input("enter student name=ken")
 print(name)
 rollno=input("roll no 3")
 print(rollno)
 #marks
 english=input("mark in english: 40")
 print(english)
 maths=input("mark in maths: 45")
 print(maths)
 chemistry=input("mark in chemistry: 40")
 print(chemistry)
 physics=input("mark in physics: 30")
 print(physics)
 computerscience=input("mark in computerscience: 45")
 print(computerscience)


 name=input("enter student name=sea")
 print(name)
 rollno=input("roll no 4")
 print(rollno)
 #marks
 english=input("mark in english: 60")
 print(english)
 maths=input("mark in maths: 45")
 print(maths)
 chemistry=input("mark in chemistry: 45")
 print(chemistry)
 physics=input("mark in physics: 49")
 print(physics)
 computerscience=input("mark in computerscience: 60")
 print(computerscience)

 name=input("enter student name=cane")
 print(name)
 rollno=input("roll no 5")
 print(rollno)
 #marks
 english=input("mark in english: 65")
 print(english)
 maths=input("mark in maths: 45")
 print(maths)
 chemistry=input("mark in chemistry: 70")
 print(chemistry)
 physics=input("mark in physics: 55")
 print(physics)
 computerscience=input("mark in computerscience: 65")
 print(computerscience)

 name=input("enter student name=lia")
 print(name)
 rollno=input("roll no 6")
 print(rollno)
 #marks
 english=input("mark in english: 30")
 print(english)
 maths=input("mark in maths: 25")
 print(maths)
 chemistry=input("mark in chemistry: 20")
 print(chemistry)
 physics=input("mark in physics: 15")
 print(physics)
 computerscience=input("mark in computerscience: 25")
 print(computerscience)

 name=input("enter student name=bav")
 print(name)
 rollno=input("roll no 7")
 print(rollno)
 #marks
 english=input("mark in english: 50")
 print(english)
 maths=input("mark in maths: 55")
 print(maths)
 chemistry=input("mark in chemistry: 45")
 print(chemistry)
 physics=input("mark in physics: 40")
 print(physics)
 computerscience=input("mark in computerscience: 35")
 print(computerscience)

 name=input("enter student name=ren")
 print(name)
 rollno=input("roll no 8")
 print(rollno)
 #marks
 english=input("mark in english: 65")
 print(english)
 maths=input("mark in maths: 45")
 print(maths)
 chemistry=input("mark in chemistry:45")
 print(chemistry)
 physics=input("mark in physics: 49")
 print(physics)
 computerscience=input("mark in computerscience: 60")
 print(computerscience)


 name=input("enter student name=wein")
 print(name)
 rollno=input("roll no 9")
 print(rollno)
 #marks
 english=input("mark in english: 80")
 print(english)
 maths=input("mark in maths: 80")
 print(maths)
 chemistry=input("mark in chemistry: 80")
 print(chemistry)
 physics=input("mark in physics: 85")
 print(physics)
 computerscience=input("mark in computerscience: 90")
 print(computerscience)

 name=input("enter student name=nick")
 print(name)
 rollno=input("roll no 10")
 print(rollno)
  #marks
 english=input("mark in english: 95")
 print(english)
 maths=input("mark in maths: 90")
 print(maths)
 chemistry=input("mark in chemistry: 80")
 print(chemistry)
 physics=input("mark in physics: 95")
 print(physics)
 computerscience=input("mark in computerscience: 95")
 print(computerscience)

#search students record
def search_studentrecord():
 rollno=int(input("enter a roll no (1-10):"))
 zia=("rollno:1,subject mark:marks in english:90"
                                 "marks in maths:99"
                                 "marks in chemistry:85"
                                 "marks in physics:82"
                                 "marks in computerscience:95")

 mia=("rollno:2,subject mark:marks in english:80"
                               "marks in maths:90"
                               "marks in chemistry:82"
                               "mark in physics:85"
                               "mark in computerscience:90")

 ken=("rollno:3,subject mark:mark in english: 40"
                               "mark in maths: 45"
                               "mark in chemistry: 40"
                               "mark in physics: 30"
                               "mark in computerscience: 45")

 sea=("rollno:4,subject mark:mark in english:60"
                               "mark in maths: 45"
                               "mark in chemistry: 45"
                               "mark in physics: 49"
                               "mark in computerscience: 60")

 cane=("rollno:5,subject mark:mark in english: 65"
                               "mark in maths: 45"
                               "mark in chemistry: 70"
                               "mark in physics: 55"
                               "mark in computerscience: 65")

 lia=("rollno:6,subject mark:mark in english: 30"
                               "mark in maths: 25"
                               "mark in chemistry: 20"
                               "mark in physics: 15"
                               "mark in computerscience: 25")
     
 bav=("rollno:7,subject mark:mark in english:50"
                               "mark in maths: 55"
                               "mark in chemistry: 45"
                               "mark in physics: 40"
                               "mark in computerscience: 35")

 ren=("rollno:8,subject mark:mark in english: 65"
                               "mark in maths: 45"
                               "mark in chemistry:45"
                               "mark in physics: 49"
                               "mark in computerscience: 60")

 wein=("rollno:9,subject mark:mark in english: 80"
                               "mark in maths: 80"
                               "mark in chemistry: 80"
                               "mark in physics: 85"
                               "mark in computerscience: 90")

 nick=("rollno:10,subject mark:mark in english: 95"
                               "mark in maths: 90"
                               "mark in chemistry: 80"
                               "mark in physics: 95"
                               "mark in computerscience: 95") 
 if rollno==1:
     print(zia)
 elif rollno==2:
     print(mia)
 elif rollno==3:
     print(ken)
 elif rollno==4:
     print(sea)
 elif rollno==5:
     print(cane)
 elif rollno==6:
     print(lia)
 elif rollno==7:
     print(bav)
 elif rollno==8:
     print(ren)
 elif  rollno==9:
     print(wein)
 elif rollno==10:
     print(nick)
 

#To modify student result
def modification():
 student={
     ("zia"):("rollno""1""english""90""maths""99""chemistry""85""physics""82""computerscience""95"),
     ("mia"):("rollno""2""english""80""maths""90""chemistry""82""physics""85""computerscience""90"),
     ("ken"):("rollno""3""english""40""maths""45""chemistry""40""physics""30""computerscience""45"),
     ("sea"):("rollno""4""english""60""maths""45""chemistry""45""physics""49""computerscience""60"),
     ("cane"):("rollno""5""english""65""maths""45""chemistry""70""physics""55""computerscience""65"),
     ("lia"):("rollno""6""english""30""maths""25""chemistry""20""physics""15""computerscience""25"),
     ("bav"):("rollno""7""english""50""maths""55""chemistry""45""physics""40""computerscience""35"),
     ("ren"):("rollno""8""english""65""maths""45""chemistry""45""physics""49""computerscience""60"),
     ("wein"):("rollno""9""english""80""maths""80""chemistry""80""physics""85""computerscience""90"),
     ("nick"):("rollno""10""english""95""maths""90""chemistry""80""physics""95""computerscience""95")}
 modify=input("enter a ""rollno""_""english""_""maths""_""chemistry""_""physics""_""computerscience""_"" to modify:")
 print(modify)
 name=input("enter the student name to modify:")
 print("The student name to modify him/her record")
 aftermodification=input("student[name]=modify:")
 print(aftermodification)
 print(student)

#to delete a student record
def delete_record():
 student={
    "zia":{"rollno":1,"english":"90","maths":"99","chemistry":"85","physics":"82","computerscience":"95"},
    "mia":{"rollno":2,"english":"80","maths":"90","chemistry":"82","physics":"85","computerscience":"90"},
    "ken":{"rollno":3,"english":"40","maths":"45","chemistry":"40","physics":"30","computerscience":"45"},
    "sea":{"rollno":4,"english":"60","maths":"45","chemistry":"45","physics":"49","computerscience":"60"},
    "cane":{"rollno":5,"english":"65","maths":"45","chemistry":"70","physics":"55","computerscience":"65"},
    "lia":{"rollno":6,"english":"30","maths":"25","chemistry":"20","physics":"15","computerscience":"25"},
    "bav":{"rollno":7,"english":"50","maths":"55","chemistry":"45","physics":"40","computerscience":"35"},
    "ren":{"rollno":8,"english":"65","maths":"45","chemistry":"45","physics":"49","computerscience":"60"},
    "wein":{"rollno":9,"english":"80","maths":"80","chemistry":"80","physics":"85","computerscience":"90"},
    "nick":{"rollno":10,"english":"95","maths":"90","chemistry":"80","physics":"95","computerscience":"95"}}
 name=input("enter the student name to delete his details:")
 if name=="zia":
  del student["zia"]
  print(student)
 if name=="mia":
  del student["mia"]
  print(student)
 if name=="ken":
  del student["ken"]
  print(student)
 if name=="sea":
  del student["sea"]
  print(student)
 if name=="cane":
  del student["cane"]
  print(student)
 if name=="lia":
  del student["lia"]
  print(student)
 if name=="bav":
  del student["bav"]
  print(student)
 if name=="ren":
  del student["ren"]
  print(student)
 if name=="wein":
  del student["wein"]
  print(student)
 if name=="nick":
  del student["nick"]
  print(student)

#Main menu
def main_menu():
    choice=int(input("choice from main menu and Admin menu(1-6) : ____1.Class_result,___2.student_reportcard ,___3.display_studentrecord,___4.search_studentrecord,___5.modification___6.delete_record:"))
    if choice==1:
        print("class result:",Class_result())
    if choice==2:
        print("student report card:",student_reportcard())
    if choice==3:
        print("display student record:",display_studentrecord())
    if choice==4:
        print("search student record:",search_studentrecord())
    if choice==5:
        print("modification of student record:",modification())
    if choice==6:
        print("delete student record:",delete_record())
    else:
        print("Not found")
main_menu()