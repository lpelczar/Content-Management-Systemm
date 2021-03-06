import os
import pickle

from models.group import Group
from models.student import Student

STUDENT_ALREADY_IN_GROUP = 'This student already belongs to group {} !'

GROUP_DOES_NOT_EXIST = "Such group does not exist !"

GROUP_ALREADY_EXISTS = "Such group already exists !"

ALREADY_EXISTS = "An instantiation already exists!"

FILE_NAME = 'groups.csv'


class GroupContainer:

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError(ALREADY_EXISTS)
        self.groups = []
        self.load_groups_from_file()

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = GroupContainer()
        return cls.INSTANCE

    def save_groups_to_file(self):
        """
        Method saves groups list to file.
        :return: None
        """
        if self.groups:
            with open(FILE_NAME, 'wb') as output:
                pickle.dump(self.groups, output, pickle.HIGHEST_PROTOCOL)  # saves object to file

    def load_groups_from_file(self):
        """
        Method loads groups list from file
        :return: None
        """
        if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if self.groups:
            return  # checks if the list have been loaded before if so it does not load again
        with open(FILE_NAME, 'rb') as file:
            self.groups = pickle.load(file)  # load object from file

    def get_groups_list(self):
        """
        Getter of all groups.
        :return:
        """
        return self.groups

    def get_group(self, group_name: str):
        """
        Returns group instance by name
        :param group_name: str -> name of group instance to be returned
        :return: User -> an instance of group
        """
        for group in self.groups:
            if group.name.upper() == group_name.upper():
                return group
        return None

    def add_group(self, group_name: str):
        """
        Methods add group to groups and save to file.
        :param group_name: str -> group
        :return: None
        """
        self.__raises_error_if_group_exists(group_name)
        new_group = Group(group_name)
        self.groups.append(new_group)
        self.save_groups_to_file()

    def remove_group_by_name(self, group_name: str):
        """
        Methods remove group by name from groups and save updated groups list to file.
        :param group_name: str -> name of group to be removed
        :return: None
        """
        self.__raises_error_if_group_does_not_exist(group_name)
        self.remove_group_by_name(group_name)
        self.save_groups_to_file()

    def remove_group_by_instance(self, group: Group):
        """
        Methods remove group by name from groups and save updated groups list to file.
        :param group: User -> group object
        :return: None
        """
        self.__raises_error_if_group_does_not_exist(group.name)
        self.groups.remove(group)
        self.save_groups_to_file()

    def does_group_exist(self, group_name: str):
        """
        Method checks if group with given name already exists in the database.
        :param group_name: str -> the name of group to check
        :return: bool -> True if exists otherwise False
        """
        for group in self.groups:
            if group.name.upper() == group_name.upper():
                return True
        return False

    def get_student_group_name(self, student: Student):
        """
        Method returns student group name, otherwise it returns None
        :param student: Student -> Student instance
        :return: str -> name of the group to which student belongs
        """
        for group in self.groups:
            if student.login in group.student_login_list:
                return group.name

    def add_student_to_group(self, group_name: str, student: Student):
        """
        Methods add student to group.
        :param group_name: str -> name of group to which student should be added
        :param student: Student - > instance of student to be added to given group
        :return: None
        """
        self.__raises_error_if_group_does_not_exist(group_name)
        self.__raises_error_if_student_already_in_group(student)
        group = self.get_group(group_name)
        group.student_login_list.append(student.login)
        student.group = group_name
        self.save_groups_to_file()

    def remove_student_from_group(self, group_name: str, student: Student):
        """
        Remove add student from group.
        :param group_name: str -> name of group to which student should be added
        :param student: Student - > instance of student to be added to given group
        :return: None
        """
        self.__raises_error_if_group_does_not_exist(group_name)
        group = self.get_student_group_name(student)
        if not group:
            raise AttributeError('This user does not belong to any group !')
        student.group = None
        group.remove(student.login)
        self.save_groups_to_file()

    def __raises_error_if_group_does_not_exist(self, group_name: str):
        """
        Private method that raises an exception if group with given name does not exist.
        :param group_name: str -> the group name to check
        :return:
        """
        if not self.does_group_exist(group_name):
            raise AttributeError(GROUP_DOES_NOT_EXIST)

    def __raises_error_if_group_exists(self, group_name: str):
        """
        Private method that raises an exception if group with given name exists.
        :param group_name: str -> the group name to check
        :return:
        """
        if self.does_group_exist(group_name):
            raise AttributeError(GROUP_ALREADY_EXISTS)

    def __raises_error_if_student_already_in_group(self, student: Student):
        """
        Private method that raises an exception if given student is already in group.
        :param student: Student -> the Student instance to check
        :return:
        """
        current_student_group = self.get_student_group_name(student)
        if current_student_group:
            raise AttributeError(STUDENT_ALREADY_IN_GROUP.format(current_student_group))
