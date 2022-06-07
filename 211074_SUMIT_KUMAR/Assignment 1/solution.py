from datetime import date
today = date.today()

class Member:
  # string name
  # string username
  # int id ## a unique id for every member
  # string phone_number
  # dob (you should decide how to implement dob)
  objects = []
  def __init__(self, id, name, username, phone_number, dob):
    self.id = id
    self.name = name
    self.username = username
    self.phone_number = phone_number
    self.dob = dob
    ## This is the constructor being talked about in the description
  def update_info_by_id(id, name, username, phone_number, dob):
    for obj in Member.objects:
      if obj.id == id:
        obj.id = id
        obj.name = name
        obj.username = username
        obj.phone_number = phone_number
        obj.dob = dob
    ## This function should update the information of the person spcified by the received id
  def display_info_by_id (id):
    for obj in Member.objects:
      if obj.id == id:
        print(f"{obj.id} {obj.name} {obj.username} {obj.phone_number} {obj.dob}")
    ## display member info who has the same id as received
  def contact_details(self):
    print(f"Phone number of {self.name} is {self.phone_number}")
    ## diplay contact details of the member 
  def display_age(self):
    age =  today.year - self.dob.year - ((today.month, today.day) - (self.dob.month, self.dob.day))
    print(f"Age of {self.name} is {age}")
    ## displays the age of the member

    
    
    class Student(Member):
  # string branch
  # int attendance

  def __init__(self, id, name, username, phone_number, dob, attendance, branch):
    self.attendance = attendance
    self.branch = branch
    Member.__init__(self, id, name, username, phone_number, dob)

  def travel_ticket_discount(ticket_price):
    age =  today.year - self.dob.year - ((today.month, today.day) - (self.dob.month, self.dob.day))
    if age <= 12:
      print("Free ticket")
    elif (age >=13 && age <= 25):
      print("Half fare for ticket")
    else:
      print("Full fare for ticket")
    ##age uptil 12 -> No money
    ##between 13 to 25 -> half fare
    ##above 26 -> Full money

  def attendance_is_ok():
    if self.attendance >= 75:
      print("Attendance criteria is complied")
    else:
      print("Attendance is less than minimum criteria")
    ## function to check if the member has complied with the attendance criteria
    
    
    
    class Professor(Member):
  # string field
  # int attendance

  def __init__(self, id, name, username, phone_number, dob, attendance, field):
    self.attendance = attendance
    self.field = field
    Member.__init__(self, id, name, username, phone_number, dob)
    
  def travel_ticket_discount(self, ticket_price):
    age =  today.year - self.dob.year - ((today.month, today.day) - (self.dob.month, self.dob.day))
    if age <= 12:
      print("Free ticket")
    elif (age >=13 && age <= 25):
      print("Half fare for ticket")
    else:
      print("Full fare for ticket")
    ##age uptil 12 -> No money
    ##between 13 to 25 -> half fare
    ##above 26 -> Full money

  def attendance_is_ok(self):
    if self.attendance >= 90:
      print("Attendance criteria is complied")
    else:
      print("Attendance is less than minimum criteria")
    ## function to check if the member has complied with the attendance criteria
