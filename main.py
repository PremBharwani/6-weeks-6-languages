class main (Professor,Student)
def _init_(id, name, username, phone_number, dob,age,attendance,string_field):
Professor._init_(id, name, username, phone_number, dob,age,attendance,string_field)
Student._init_(id, name, username, phone_number, dob,age,attendance,string_branch)
             def detail():
                      print("these information are available here")
object=main()
object.detail()