class Member(object):
        def __init__(self, id, name, username, phone_number, dob):
            self.id=id
            self.name=name
            self.username=username
            self.phone_number=phone_number
            self.dob=dob
        def update_info_by_id(self, id, name, username, phone_number, dob):
            if((self.id)==id):
                self.name=name
                self.username=username
                self.phone_number=phone_number
                self.dob=dob
            else :
                print("Invalid Id")    
        def display_info_by_id (self, id):
            if((self.id)==id):
                print(self.name)
                print(self.username)
                print(self.dob)
                print(self.branch)
            else :
                print("Invalid Id")
        def contact_details(self):
            print(self.phone_number)
        def display_age(self):
            print("Age as on 1st January 2022 {}".format(2022-(self.dob/100000)))
class Professor(Member):
        def __init__(self, id, name, username, phone_number, dob, field, attendance):
            super().__init__(id, name, username, phone_number, dob)
            self.branch=field
            self.attendance=attendance
        def travel_ticket_discount(self, ticket_price):
            if(((2022-(self.dob/100000)))<=12):
                print("No money")
            elif((2022-(self.dob/100000))<=25):
                print(ticket_price/2)
            else:
                print(ticket_price)
        def attendance_is_ok(self):
            if(((self.attendance*100)/365)>=90):
                print("Has complied attendance criteria")
            else:
                print("Has not complied attendance criteria")
class Student(Member):
        def __init__(self, id, name, username, phone_number, dob, branch, attendance):
            super().__init__(id, name, username, phone_number, dob)
            self.branch=branch
            self.attendance=attendance
        def travel_ticket_discount(self, ticket_price):
            if(((2022-(self.dob/100000)))<=12):
                print("No money")
            elif((2022-(self.dob/100000))<=25):
                print(ticket_price/2)
            else:
                print(ticket_price)
        def attendance_is_ok(self):
            if(((self.attendance*100)/365)>=75):
                print("Has complied attendance criteria")
            else:
                print("Has not complied attendance criteria")
def main():
    Matthew = Professor(1, "Matthew Jason", "matt1", 1234567890, 19860101, "Physics", 300)
    Jhon = Student(10, "Jhon Tart", "jh10", 4567891230, 20000101, "mechanical", 300)
    Matthew.update_info_by_id(1, "Matthew Jason", "matt1", 1234567890, 19870101)
    Jhon.update_info_by_id(10, "Jhon Tart", "jh10", 4567891230, 20000101)
    Matthew.display_info_by_id(1)
    Matthew.contact_details()
    Matthew.display_age()
    Matthew.travel_ticket_discount(100)
    Matthew.attendance_is_ok()
    Jhon.travel_ticket_discount(100)
    Jhon.attendance_is_ok()
    
if (__name__=="__main__"):
    main()
