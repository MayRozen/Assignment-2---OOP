import Users


class SocialNetwork:
    _active_network = None  # Singleton
    check_userName = {}

    def __new__(cls, new_name_network):
        if cls._active_network is None:  # If an instance does not exist -> create a new one
            cls._active_network = super().__new__(cls)  # super -> from Object class
            cls._active_network = new_name_network
            print(cls._active_network)
        return cls._active_network

    def sign_up(self, new_username, new_password):
        if new_username not in self.check_userName:
            if 4 <= len(new_password) <= 8:
                user = Users(new_username, new_password)
                self.check_userName.update(user)
        else:
            print("This name is already registered in the system.")
        return user

    def log_in(self, new_username, new_password):
        if new_username in self.check_userName:
            if new_password in self.check_userName:
                user = self.check_userName[new_username]
                user.isConnected = True
                print("The user is in")

    def log_out(self, new_username):
        if new_username in self.check_userName:
            user = self.check_userName[new_username]
            user.isConnected = False
            print("The user is out")
