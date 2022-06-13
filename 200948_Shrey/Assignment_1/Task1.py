import datetime as dt
import random

class Member(object):
  # string name
  # string username
  # int id ## a unique id for every member
  # string phone_number
  # dob (you should decide how to implement dob)
  Idlist = []
  def __init__(self, id, name, username, phone_number, dob):
    # This is the constructor being talked about in the description
    self.id = id
    self.name = name
    self.username = username
    self.phone_number = phone_number
    self.dob = dob
    Member.Idlist.append(self)

  def update_info_by_id(id, name, username, phone_number, dob):
    # This function should update the information of the person spcified by the received id
    try:
      for i in range(0,len(Member.Idlist)):
        if(Member.Idlist[i].id == id):
          per = Member.Idlist[i]
          per.id,per.name,per.username,per.phone_number,per.dob = id,name,username,phone_number,dob  
          # print("Updated")
          return
      raise ValueError
    except:
      print("No member with this ID found.")
      exit()
    

  def display_info_by_id(id):
    # display member info who has the same id as received
    try:
      for i in range(0,len(Member.Idlist)):
        if(Member.Idlist[i].id == id):
          per = Member.Idlist[i]
          print("->ID:",per.id,"--Name:",per.name,"--Username:",per.username,"--Ph.No:",per.phone_number,"--DOB:",per.dob)
          return
      raise ValueError
    except:
      print("No member with this ID found.")  

  def contact_details(self):
    # diplay contact details of the member
    return self.phone_number

  def display_age(self):
    # displays the age of the member
    return  int(((dt.date.today()-self.dob).days)/365.2425)


class Professor(Member):
  # string field
  # bool attendance
  def __init__(self, id, name, username, phone_number, dob, field):
      Member.__init__(self,id, name, username, phone_number, dob)
      self.field = field
      self.attend = []

  def travel_ticket_discount(self, ticket_price):
    # age uptil 12 -> No money
    # between 13 to 25 -> half fare
    # above 26 -> Full money
    if(self.display_age() <= 12):
        return ticket_price*0
    elif(self.display_age()>=13 and self.display_age()<=25):
        return ticket_price/2
    else:
        return ticket_price

  def update_attend(self,present):
      if(present):
          self.attend.append(True)
      else:
          self.attend.append(False)
  def attendance_is_ok(self):
      working_days = len(self.attend)
      if(self.attend.count(True) >= 0.90*working_days):
        return True
      else:
        return False

class Student(Member):
  # string branch
  # bool attendance

  def __init__(self, id, name, username, phone_number, dob, branch):
      Member.__init__(self,id, name, username, phone_number, dob)
      self.branch = branch
      self.attend = []

  def travel_ticket_discount(self,ticket_price):
    # age uptil 12 -> No money
    # between 13 to 25 -> half fare
    # above 26 -> Full money
    if(self.display_age() <= 12):
        return ticket_price*0
    elif(self.display_age()>=13 and self.display_age()<=25):
        return ticket_price/2
    else:
        return ticket_price
    
  def update_attend(self,present):
      if(present):
          self.attend.append(True)
      else:
          self.attend.append(False)
  def attendance_is_ok(self):
      working_days = len(self.attend)
      if(self.attend.count(True) >= 0.75*working_days):
        return True
      return False

def startdate(semstart):
    return int(((dt.date.today()-semstart).days))


if __name__ == "__main__":

  him1 = Student(200100,'ABBA Waterloo','ABWater20',9876543210,dt.date(1974,3,4),'EECS')
  him2 = Student(200103, 'Daft Punk', 'DPunk20', 9876543120, dt.date(2021,2,22), 'EECS')
  him3 = Professor(100000, 'Led Zeppelin', 'Zepp',9087654321, dt.date(2000,1,1), 'CS')
  Personlist = [him1,him2,him3]


  today = startdate(dt.date(2022,6,1))
  for i in range(0,today):
    for person in Personlist:
      person.update_attend(random.choice([True,True,True,False]))

  # Member.update_info_by_id(100900,"who","who",8090980089,dt.date(1976,9,22)) ###Invalid INPUT
  # Member.update_info_by_id(100000,"who","who",8090980089,dt.date(1976,9,22)) ### Valid INPUT

  ilist = []
  for person in Personlist:
    ilist.append(str(person.id))

  ans = ''
  while (ans != '\\'):
    ans = input("Do you want to view a single record or all of them?(Enter 1, All, //(to exit)): ")
    if(ans == '1'):
        print("Possible ids are:", ' '.join(ilist))
        res = input("Enter ID: ")
        try:
          res = int(res)
          Member.display_info_by_id(res)
        except ValueError:
          print("That is not a valid ID")
    elif(ans == 'All'):
        print("--------------------------------------------")
        for person in Personlist:
          Member.display_info_by_id(person.id)
          if(isinstance(person,Student)):
            print("Branch:",person.branch)
          if(isinstance(person,Professor)):
            print("Branch:",person.field)
          print("Contact_Details:",person.contact_details(),)
          print("Age:", person.display_age())
          print("Ticket Price:",person.travel_ticket_discount(40.0))
          print("Working days attended by",person.id,"is",person.attend.count(True),"out of a total working days:",len(person.attend))
          if(person.attendance_is_ok()):
            print("Attendance is Okay.")
          else:
            print("Attendance is Not Okay.")
          print("--------------------------------------------")
    elif(ans == '//'):
        print("Exiting. Bye!")
        break;
    else:
        print("That is not a valid input.Try again.")
      


  








