
# class GeeksPeople:
#         def __init__(self, name, email, phone):
#           self.name = name
#           self.email = email
#           self.phone = phone

#         def __str__(self):
#            return f"Your name {self.name}, Your email {self.email} Your phone {self.phone}"


# class Student(GeeksPeople):
#     def __init__(self, name, email, phone, student_id, group_where_study):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.student_id = student_id
#         self.group_where_study = group_where_study

#     def study(self):
#         return f"студент {self.name}, учится в группе {self.group_where_study}"

#     def __str__(self):
#         return f"студент {self.name}, email {self.email}, phone {self.phone}, student id {self.student_id}"


# class Teacher(GeeksPeople):
#     def __init__(self, name, email, phone, teacher_id, group_where_teach):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.teacher_id = teacher_id
#         self.group_where_teach = group_where_teach

#     def teach(self):
#         return f"преподаватель {self.name}, преподает в группе {self.group_where_teach}"

#     def __str__(self):
#         return f"преподаватель {self.name}, email {self.email}, phone {self.phone}, teacher id {self.teacher_id}"




# class Admin(GeeksPeople):
#     def __init__(self, name, email, phone, admin_id, create_group):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.admin_id = admin_id
#         self.create_group_name = create_group

#     def create_group(self, group_name):
#         return f"администратор {self.name}, создал новую группу {group_name}"

#     def __str__(self):
#         return f"администратор {self.name}, email {self.email}, phone {self.phone}, admin id {self.admin_id}"
    
# # class Mentor(Student,Teacher):
# #     def __init__(self, name, email, phone, student_id, group_where_study,teacher_id,group_where_teach):
# #         Student.__init__(name, email, phone, student_id, group_where_study)
# #         Teacher.__init__(name, email, phone, teacher_id,group_where_teach)
    
# #     def mentor_info(self):
# #         return f"Mentor {self.name}, {self.group_where_study},  {self.group_where_teach}"
    
# #     def __str__(self):
# #         return f"mentor {self.name},email {self.email}, phone {self.phone}, student id {self.student_id}, teacher id {self.teacher_id} "


# class Mentor(Student, Teacher):
#     def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
#         Student.__init__(self, name, email, phone, student_id, group_where_study)
#         Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
    


# student1 = Student("Nur", "nur@gmаil.com", "12356", "001", "Group   1")
# teacher1 = Teacher("Сыймык", "Сыймык@gmаil.com", "78012", "T001", "Group    1")
# admin1 = Admin("Сыймык", "syimyk@gmаil.com", "34578", "001", "Group   ")
# mentor1 = Mentor("Eliza", "eliza@gmаil.com", "9234", "00", "Group   1", "030")



# student1.study()
# teacher1.teach()
# admin1.create_group()
# mentor1.study()
# mentor1.teach()

















































class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя: {self.name}, емайл: {self.email}, номер телефона: {self.phone}"


class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"{self.name} учится в группе {self.group_where_study}")


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"{self.name} преподает в группе {self.group_where_teach}")


class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def create_group(self):
        print(f"Admin {self.name} создал новую группу")


class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)


# Create instances of each type of user
student1 = Student("Нурсейит", "suranbaev@gmail.com", "2342423", "001", "Group 17-1B")
teacher1 = Teacher("Cыймык", "Сыймык@gmail.com", "2342", "001", "Group 17-1B")
admin1 = Admin("Нурболот", "нурболот@gmail.com", "342", "00")
mentor1 = Mentor("eliza", "eliza@gmail.com", "111", "001", "Group ", "00", "Group 17-1B")


student1.study()
teacher1.teach()
admin1.create_group()
mentor1.study()
mentor1.teach()