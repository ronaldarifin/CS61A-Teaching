class Car:
    classAttribute = 0
    def __init__(self):
        #what is the difference between line 1 and 2?
        
        Car.classAttribute += 1
        self.classAttribute += 1
        # after everything. If I do print(a.mystery) will I see anything?
        self.thisIsAnInstanceAttribute = 0
        mystery = 1

a = Car("hello")
# this line will error because we don't have a mystery attribute for the instance.
# print(a.mystery)
b = Car()
c = Car()

# link: https://pythontutor.com/visualize.html#code=class%20CS61A%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.students%20%3D%20%5B%5D%0A%0A%20%20%20%20def%20add_student%28self,%20student_name%29%3A%0A%20%20%20%20%20%20%20%20if%20student_name%20not%20in%20self.students%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.students.append%28student_name%29%0A%0A%20%20%20%20def%20display_students%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22Students%3A%22,%20',%20'.join%28self.students%29%29%0A%0A%0Aclass%20Tutoring%28CS61A%29%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20CS61A.__init__%28self%29%0A%20%20%20%20%20%20%20%20%23%20super%28%29.__init__%28%29%0A%20%20%20%20%20%20%20%20self.tutoring_schedule%20%3D%20%7B%7D%0A%0A%20%20%20%20def%20set_tutoring_time%28self,%20student_name,%20time_slot%29%3A%0A%20%20%20%20%20%20%20%20if%20student_name%20in%20self.students%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.tutoring_schedule%5Bstudent_name%5D%20%3D%20time_slot%0A%0A%20%20%20%20def%20display_tutoring_schedule%28self%29%3A%0A%20%20%20%20%20%20%20%20for%20student,%20time%20in%20self.tutoring_schedule.items%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22%7Bstudent%7D%3A%20%7Btime%7D%22%29%0A%0A%0A%23%20Testing%20the%20classes%0Atutor_session%20%3D%20Tutoring%28%29%0A%0Astudents%20%3D%20%5B%22adam%22,%20%22mihir%22,%20%22morgan%22,%20%22carolyn%22,%20%22sammit%22,%20%22shahad%22%5D%0Afor%20student%20in%20students%3A%0A%20%20%20%20tutor_session.add_student%28student%29%0A%0Atutor_session.display_students%28%29%0A%0Atutor_session.set_tutoring_time%28%22carolyn%22,%20%22Monday%205pm%22%29%0Atutor_session.set_tutoring_time%28%22morgan%22,%20%22Monday%205pm%22%29%0A%0Atutor_session.display_tutoring_schedule%28%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false