class Member:
  # string name
  # string username
  # int id ## a unique id for every member
  # string phone_number
  # dob (you should decide how to implement dob)

  def __init__(id, name, username, phone_number, dob):
    ## This is the constructor being talked about in the description
    id.name=name
    id.username=username
    id.phone_number
    id.dob
  def update_info_by_id(id, name, username, phone_number, dob):
    ## This function should update the information of the person spcified by the received id
   name="pinkesh"
   username="pinkeshm21"
   phone_number="6378697483"
   id.dob="01-12-2002"
  def display_info_by_id (id)
    ## display member info who has the same id as received
    print(id.name)
    print(id.username)
    print(id.phone_number)
    print(id.dob)
  def contact_details():
    ## diplay contact details of the member 
    print("contact no. is {}".format(id.phone_number))

  def display_age():
    ## displays the age of the member
    print("age is {}".format(id.phone_number))
class Professor(Member):
  # string field
  # int attendance
 def __init__(id, name, username, phone_number, dob,age,string_field,attendance):
     id.age=age
     id.attendance=attendance
     id.string_field=string_field
     Member.__init__(id, name, username, phone_number, dob)
    

  def travel_ticket_discount(ticket_price):
      t=(ticket_price)/2

    ##age uptil 12 -> No money
    ##between 13 to 25 -> half fare
    ##above 26 -> Full money
    if (age < 13) : print(ticket_price)
    elif(age >25) : print(0)
    else : print(t)



  def attendance_is_ok():
    ## function to check if the member has complied with the attendance criteria
    p=( attendance *100)/365
    if(p >=90)  : print("attendance Pass")
    else : print("attendance Fail")

class Student(Member):
  # string branch
  # int attendance
 def __init__(id, name, username, phone_number, dob,age,string_branch,attendance):
     id.age=age
     id.attendance=attendance
     id.string_field=string_branch
     Member.__init__(id, name, username, phone_number, dob)
    

    
 

  def travel_ticket_discount(ticket_price):
      t=(ticket_price)/2

    ##age uptil 12 -> No money
    ##between 13 to 25 -> half fare
    ##above 26 -> Full money
    if (age < 13) : print(ticket_price)
    elif(age >25) : print(0)
    else : print(t)



  def attendance_is_ok():
    ## function to check if the member has complied with the attendance criteria
    p=( attendance *100)/365
    if(p >=75)  : print("attendance Pass")
    else : print("attendance Fail")
    

   
