from user import User

class UserManager:
    def __init__(self):
        return

    def __del__(self):
        pass

    def create_user(self, user_id):
        # creates a user object
        # adds a user to the users_list
        # open txt file containing users
        f = open('../data/users.txt', 'a')
        #self.users_list.append(user_id)
        f.write(user_id+'\n')
        user = User(user_id)
        self._library_controller.add_user(user)

    def set_library_controller(self, library_controller):
        # sets the library controller
        self._library_controller = library_controller

    def open_user_list(self):
        # opens user list
        pass
