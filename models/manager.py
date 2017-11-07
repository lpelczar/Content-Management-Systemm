from user import User
from user_container import UserContainer
from student import Student
from mentor import Mentor


class Manager(User):

    def __init__(self, login, password, email, phone_number, group_names, name):
        super().__init__(login, password, email, phone_number)
        self.groups = group_names
        self.name = name

    def promote_user_to_mentor(self, user):
        pass

    def remove_mentor(self, mentor, mentors_list):
        if mentor in mentors_list:  # Operuje na liscie mentrowo, jesli sie nie przyda zmienic na IsInstance USerlist
            mentors_list.remove(mentor)

        return mentors_list

    def change_mentor_data(self, mentor):
        pass

    def get_mentors_list(self):
        user_list = UserContainer.get_instance().get_users_list()
        mentors_list = []

        for mentor in user_list:
            if isinstance(mentor, Mentor):
                mentor = mentor.__str__
                mentors_list.append

        return mentors_list

    def get_students_list(self):
        user_list = UserContainer.get_instance().get_users_list()
        students_list = []

        for student in user_list:
            if isinstance(student, Student):
                student = student.__str__
                students_list.append(student)

        return students_list

    def __str__(self):
        information = self.name + ': ' + self.email + ', ' + self.phone_number
        return information
