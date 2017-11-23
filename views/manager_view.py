import os

from dependencies.texttable import Texttable, get_color_string, bcolors
from views.colorful_view import ColorfulView

STARTING_INDEX = 1
MENU_OPTIONS = {'1': 'Promote user to Mentor',
                '2': 'Remove Mentor',
                '3': 'Edit Mentor data',
                '4': 'Display list of Mentors',
                '5': 'Display list of Students',
                '6': 'Change user role',
                '0': 'Exit manager'}
COLORED_MENU_OPTIONS = {get_color_string(bcolors.PURPLE, k): get_color_string(bcolors.PURPLE, v)
                        for k, v in MENU_OPTIONS.items()}


class ManagerView:

    @staticmethod
    def display_manager_menu(user_login, role):
        greeting_message = get_color_string(bcolors.BLUE, 'Logged as {} ({})'.format(user_login, role))
        t = Texttable()
        t.set_deco(Texttable.HEADER)
        t.add_rows([['', greeting_message]] +
                   [[k, v] for k, v in COLORED_MENU_OPTIONS.items()])
        print(t.draw())

    @staticmethod
    def get_user_input(prompt: str):
        return input(prompt)

    @staticmethod
    def display_actual_list(users):
        print('')
        ManagerView.print_table(users)
        print('')

    @staticmethod
    def print_table(users):
        t = Texttable()
        t.set_cols_dtype(['a', 'a', 'a', 'a', 'i', 'a'])
        colored_titles = [get_color_string(bcolors.BLUE, i) for i in ['Index', 'Login', 'Name', 'Role',
                                                                      'Phone Number', 'E-mail']]
        t.add_rows([colored_titles] +
                   [[i + STARTING_INDEX, u.get_login(), u.get_name(), u.__class__.__name__, u.get_phone_number(),
                     u.get_email()] for i, u in enumerate(users)])
        print(t.draw())

    @staticmethod
    def display_empty_list_message():
        print('')
        print(ColorfulView.format_string_to_red('List is empty!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_users(users):
        print('')
        ManagerView.print_table(users)
        input('\nPress ENTER to continue')

    @staticmethod
    def display_mentor_information(mentor_data):
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('Login: ') + mentor_data.get_login()
              + ColorfulView.format_string_to_green('\nName: ') + mentor_data.get_name()
              + ColorfulView.format_string_to_green('\nPhone number: ') + mentor_data.get_phone_number()
              + ColorfulView.format_string_to_green('\nEmail: ') + mentor_data.get_email())

    @staticmethod
    def get_promotion_input():
        return input('Enter login of the user which do you want to promote to Mentor: ')

    @staticmethod
    def get_user_remove_input():
        return input('Enter login of the user which do you want to remove: ')

    @staticmethod
    def get_user_edit_input():
        return input('Enter login of the mentor which do you want to modify: ')

    @staticmethod
    def get_new_value():
        return input('Enter new value: ')

    @staticmethod
    def display_wrong_attribute():
        print(ColorfulView.format_string_to_red('There is no such attribute to change!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_promoted(user):
        print(ColorfulView.format_string_to_green('User: {} has been promoted'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_deleted(user):
        print(ColorfulView.format_string_to_red('User: {} has been deleted'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def get_value_to_change():
        return input('Enter what do you want to change('
                     + ColorfulView.format_string_to_green('login, phone, email, name') + '):')

    @staticmethod
    def display_user_not_found():
        print(ColorfulView.format_string_to_red('User with that name not found!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def get_user_login():
        return input('Enter login of the user: ')

    @staticmethod
    def get_new_role():
        return input('Choose new role: \033[91mS\033[0mtudent, \033[91mE\033[0mmployee, '
                     '\033[91mM\033[0mentor, \033[91mM\033[0manager')

    @staticmethod
    def display_wrong_role():
        print('There is no such role.')
        input('\nPress ENTER to continue')